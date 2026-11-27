#!/usr/bin/env python3
"""
NTRK1 (TrkA, CHEMBL2815) referans veri setlerini uretir.

Bu betik, kurs deposundaki `03_veri/` klasorundeki hazir CSV dosyalarini uretir ve
notebook 01'deki "canli ChEMBL cekimi" ile AYNI temizlik mantigini uygular;
boylece katilimcilar iki yolu karsilastirabilir.

Kullanim:
    python veri_uret.py --cikti ../03_veri
    python veri_uret.py --cikti ../03_veri --esik 7.5

Uretilen dosyalar:
    ntrk1_ham_chembl.csv       Ham IC50 kayitlari (ChEMBL'den geldigi gibi)
    ntrk1_regresyon.csv        Smiles, pIC50
    ntrk1_siniflandirma.csv    Smiles, pIC50, Aktiflik
    ntrk1_veri_kunyesi.json    Uretim tarihi, kayit sayilari, sinif dengesi
    tarama_kutuphanesi.csv     Onayli ilaclar (sanal tarama kutuphanesi)
"""

from __future__ import annotations

import argparse
import json
import math
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

import pandas as pd
from rdkit import Chem, RDLogger

RDLogger.DisableLog("rdApp.*")

API = "https://www.ebi.ac.uk/chembl/api/data"

TARGET_CHEMBL_ID = "CHEMBL2815"   # NTRK1 / TrkA  (UniProt P04629)
TARGET_ADI = "High affinity nerve growth factor receptor (NTRK1 / TrkA)"
UNIPROT = "P04629"
ACTIVITY_TYPE = "IC50"
VARSAYILAN_ESIK = 7.5             # pIC50 >= 7.5  ->  Aktif   (IC50 <= 32 nM)

# Fiziksel olarak makul pIC50 araligi. Alt sinir 3.0 -> IC50 = 1 mM.
# Bunun disindaki degerler veri giris hatasi kabul edilir.
MANTIK_ARALIGI = (3.0, 12.0)

RAPOR_ESIKLERI = [6.0, 6.5, 7.0, 7.5, 8.0]
SLUG = "ntrk1"


# ---------------------------------------------------------------------------
# ChEMBL REST yardimcilari
# ---------------------------------------------------------------------------
def _get(endpoint: str, params: dict, retries: int = 20) -> dict:
    """ChEMBL REST istegi, artan beklemeli yeniden denemeyle.

    ChEMBL web servisi zaman zaman ciddi bicimde kararsizlasir: ayni istek
    sorgu bicimine bakilmaksizin rastgele 500 dondurebilir (kurs hazirligi
    sirasinda isteklerin yaklasik yarisi basarisiz olacak kadar kotu bir
    donem gozlendi). Bu yuzden yeniden deneme sayisi yuksek tutulmustur.
    """
    url = f"{API}/{endpoint}.json?" + urllib.parse.urlencode(params)
    bekleme, son = 1.0, None
    for deneme in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=180) as resp:
                return json.load(resp)
        except Exception as exc:
            son = exc
            if deneme < retries - 1:
                time.sleep(bekleme)
                bekleme = min(bekleme * 1.5, 20)
    raise RuntimeError(f"ChEMBL istegi {retries} denemede basarisiz:\n  {url}\n  {son}")


def aktivite_tipi_sayilari(target_id: str, tipler: list[str]) -> pd.DataFrame:
    """Her aktivite tipi icin kayit sayisi (veriyi indirmeden)."""
    satirlar = []
    for tip in tipler:
        kesin = _get("activity", {
            "target_chembl_id": target_id, "standard_type": tip,
            "standard_relation": "=", "standard_units": "nM", "limit": 1,
        })["page_meta"]["total_count"]
        satirlar.append({"Aktivite tipi": tip, "Kesin (=) ve nM kayit": kesin})
    return (pd.DataFrame(satirlar)
            .sort_values("Kesin (=) ve nM kayit", ascending=False)
            .reset_index(drop=True))


def aktiviteleri_indir(target_id: str, tip: str) -> pd.DataFrame:
    """Hedefe ait, verilen tipteki kesin (=) ve nM birimli tum kayitlari indirir."""
    kayitlar, offset = [], 0
    while True:
        veri = _get("activity", {
            "target_chembl_id": target_id,
            "standard_type": tip,
            "standard_relation": "=",
            "standard_units": "nM",
            "limit": 1000,
            "offset": offset,
            "only": ("molecule_chembl_id,canonical_smiles,standard_type,"
                     "standard_relation,standard_value,standard_units,"
                     "assay_chembl_id,pchembl_value"),
        })
        sayfa = veri.get("activities", [])
        kayitlar.extend(sayfa)
        toplam = veri["page_meta"]["total_count"]
        print(f"    offset {offset:>6}  +{len(sayfa):<5} / {toplam}", flush=True)
        if len(sayfa) < 1000:
            break
        offset += 1000
    return pd.DataFrame(kayitlar)


def onayli_ilaclari_indir(en_fazla_sayfa: int = 12) -> pd.DataFrame:
    """ChEMBL'de max_phase=4 (onayli) molekuller: sanal tarama kutuphanesi.

    Derin sayfalama (buyuk offset) ChEMBL'de ozellikle kirilgandir. Bu yuzden
    bir sayfa butun denemelerden sonra da alinamazsa islem IPTAL EDILMEZ:
    o sayfa atlanir, kalanlar denenir ve sonunda kac sayfanin eksik kaldigi
    bildirilir. Kismi bir kutuphane, hic kutuphane olmamasindan iyidir.
    """
    kayitlar, atlanan = [], []
    sayfa_boyu = 1000
    for sayfa_no in range(en_fazla_sayfa):
        offset = sayfa_no * sayfa_boyu
        try:
            veri = _get("molecule", {
                "max_phase": 4, "limit": sayfa_boyu, "offset": offset,
                "only": ("molecule_chembl_id,pref_name,molecule_structures,"
                         "molecule_type"),
            })
        except RuntimeError:
            atlanan.append(offset)
            print(f"    offset {offset:>6}  ATLANDI (sunucu yanit vermedi)",
                  flush=True)
            continue

        sayfa = veri.get("molecules", [])
        for m in sayfa:
            yapi = m.get("molecule_structures") or {}
            smi = yapi.get("canonical_smiles")
            if not smi:
                continue
            kayitlar.append({
                "molecule_chembl_id": m.get("molecule_chembl_id"),
                "Isim": (m.get("pref_name") or "").title() or None,
                "Molekul_tipi": m.get("molecule_type"),
                "Smiles": smi,
            })
        print(f"    offset {offset:>6}  +{len(sayfa):<5}", flush=True)
        if len(sayfa) < sayfa_boyu:
            break

    if atlanan:
        print(f"    !! {len(atlanan)} sayfa alinamadi (offset: {atlanan})")
    return pd.DataFrame(kayitlar)


# ---------------------------------------------------------------------------
# Temizlik hatti  (notebook 01 ile ayni adimlar, ayni sirada)
# ---------------------------------------------------------------------------
def kanonik_smiles(smiles) -> str | None:
    if not isinstance(smiles, str) or not smiles:
        return None
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol, canonical=True) if mol else None


def temizle(ham: pd.DataFrame, tip: str, esik: float):
    hedef_kolon = f"p{tip}"
    huni: list[tuple[str, int]] = [("Ham ChEMBL kayitlari", len(ham))]

    df = ham.dropna(subset=["molecule_chembl_id", "standard_value",
                            "canonical_smiles"]).copy()
    huni.append(("Kimlik + deger + SMILES tam olanlar", len(df)))

    df["standard_value"] = pd.to_numeric(df["standard_value"], errors="coerce")
    df = df.dropna(subset=["standard_value"])
    df = df[df["standard_value"] > 0]
    huni.append(("Sayisal ve pozitif deger", len(df)))

    # Ayni molekulun birden cok olcumu varsa en potent (en kucuk IC50) kayit
    df = df.loc[df.groupby("molecule_chembl_id")["standard_value"].idxmin()].copy()
    huni.append(("Molekul basina min deger (benzersiz ChEMBL ID)", len(df)))

    # Kanoniklestirme: ayni yapinin farkli SMILES yazimlarini birlestirir
    df["Smiles"] = df["canonical_smiles"].apply(kanonik_smiles)
    gecersiz = int(df["Smiles"].isna().sum())
    df = df.dropna(subset=["Smiles"])
    huni.append((f"Gecerli kanonik SMILES (elenen: {gecersiz})", len(df)))

    df = df.loc[df.groupby("Smiles")["standard_value"].idxmin()].copy()
    huni.append(("Kanonik SMILES'a gore benzersiz yapi", len(df)))

    df[hedef_kolon] = df["standard_value"].apply(lambda v: -math.log10(v * 1e-9))

    # 7) Mantiksal aralik (plausibility) filtresi.
    #    ChEMBL'de nadiren fiziksel olarak imkansiz degerler bulunur; ornegin bu
    #    hedefte IC50 = 9.8e9 nM (= 9.8 MOLAR) olarak girilmis bir kayit vardir.
    #    Boyle bir derisim deneysel olarak uygulanamaz: acik bir veri giris hatasi.
    alt, ust = MANTIK_ARALIGI
    disarida = int(((df[hedef_kolon] < alt) | (df[hedef_kolon] > ust)).sum())
    df = df[(df[hedef_kolon] >= alt) & (df[hedef_kolon] <= ust)].copy()
    huni.append((f"Mantiksal aralik {alt}-{ust} (elenen: {disarida})", len(df)))

    df["Aktiflik"] = (df[hedef_kolon] >= esik).astype(int)

    df = (df[["molecule_chembl_id", "Smiles", "standard_value", hedef_kolon, "Aktiflik"]]
          .rename(columns={"standard_value": f"{tip}_nM"})
          .sort_values(hedef_kolon, ascending=False)
          .reset_index(drop=True))
    huni.append(("NIHAI veri seti", len(df)))
    return df, huni


def pchembl_capraz_kontrol(ham: pd.DataFrame, tip: str) -> dict | None:
    """Kendi hesapladigimiz p-degeri ile ChEMBL'in pchembl_value alanini karsilastirir.

    Bu, birim ve logaritma mantigimizin dogrulugunu bagimsiz bir kaynakla
    sinamanin en kolay yoludur.
    """
    if "pchembl_value" not in ham.columns:
        return None
    d = ham.copy()
    d["v"] = pd.to_numeric(d["standard_value"], errors="coerce")
    d["p_chembl"] = pd.to_numeric(d["pchembl_value"], errors="coerce")
    d = d[(d["v"] > 0) & d["p_chembl"].notna()]
    if d.empty:
        return None
    bizim = -(d["v"] * 1e-9).apply(math.log10)
    fark = (bizim - d["p_chembl"]).abs()
    return {"karsilastirilan": int(len(d)),
            "ortalama_fark": float(fark.mean()),
            "max_fark": float(fark.max())}


def denge_tablosu(df: pd.DataFrame, hedef_kolon: str) -> pd.DataFrame:
    n = len(df)
    satir = []
    for e in RAPOR_ESIKLERI:
        aktif = int((df[hedef_kolon] >= e).sum())
        satir.append({"Esik (pIC50)": e, "IC50 (nM)": round(10 ** (9 - e), 1),
                      "Aktif": aktif, "Inaktif": n - aktif,
                      "Aktif %": round(100 * aktif / n, 1)})
    return pd.DataFrame(satir)


# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cikti", default="../03_veri", help="Cikti klasoru")
    ap.add_argument("--esik", type=float, default=VARSAYILAN_ESIK,
                    help=f"Siniflandirma esigi (varsayilan {VARSAYILAN_ESIK})")
    ap.add_argument("--tarama-atla", action="store_true",
                    help="Onayli ilac kutuphanesini indirmeyi atla")
    ap.add_argument("--ham-kullan", action="store_true",
                    help="Varsa diskteki ham CSV'yi kullan (yeniden indirme)")
    args = ap.parse_args()

    cikti = Path(args.cikti).expanduser().resolve()
    cikti.mkdir(parents=True, exist_ok=True)
    hedef_kolon = f"p{ACTIVITY_TYPE}"

    print(f"Hedef           : {TARGET_CHEMBL_ID}  {TARGET_ADI}")
    print(f"UniProt         : {UNIPROT}")
    print(f"Aktivite tipi   : {ACTIVITY_TYPE}")
    print(f"Siniflama esigi : {hedef_kolon} >= {args.esik}\n")

    print("Aktivite tipleri sayiliyor...")
    sayim = aktivite_tipi_sayilari(
        TARGET_CHEMBL_ID, ["IC50", "Ki", "Kd", "EC50", "Potency", "Inhibition"])
    print(sayim.to_string(index=False), "\n")
    sayim.to_csv(cikti / f"{SLUG}_aktivite_tipleri.csv", index=False)

    ham_yolu = cikti / f"{SLUG}_ham_chembl.csv"
    if args.ham_kullan and ham_yolu.exists():
        ham = pd.read_csv(ham_yolu)
        print(f"Mevcut ham dosya kullaniliyor: {ham_yolu.name}  ({len(ham)} kayit)")
    else:
        print(f"{ACTIVITY_TYPE} kayitlari indiriliyor...")
        ham = aktiviteleri_indir(TARGET_CHEMBL_ID, ACTIVITY_TYPE)
        print(f"  indirilen ham kayit: {len(ham)}")
        ham.to_csv(ham_yolu, index=False)

    df, huni = temizle(ham, ACTIVITY_TYPE, args.esik)
    print("\nTemizlik hunisi:")
    for ad, n in huni:
        print(f"  {ad:<52} {n:>6}")

    # Capraz kontrol: kendi hesapladigimiz pIC50, ChEMBL'in pchembl_value alaniyla
    # ortusuyor mu? Ortusmuyorsa hesap ya da birim mantiginda hata vardir.
    kontrol = pchembl_capraz_kontrol(ham, ACTIVITY_TYPE)
    if kontrol:
        print(f"\npchembl_value capraz kontrolu "
              f"({kontrol['karsilastirilan']} kayit):")
        print(f"  ortalama |fark| : {kontrol['ortalama_fark']:.4f}")
        print(f"  en buyuk |fark| : {kontrol['max_fark']:.4f}"
              f"   -> {'TUTARLI' if kontrol['max_fark'] < 0.02 else 'DIKKAT'}")

    denge = denge_tablosu(df, hedef_kolon)
    print("\nSiniflandirma esigi secenekleri:")
    print(denge.to_string(index=False))

    df[["Smiles", hedef_kolon]].to_csv(cikti / f"{SLUG}_regresyon.csv", index=False)
    df[["Smiles", hedef_kolon, "Aktiflik"]].to_csv(
        cikti / f"{SLUG}_siniflandirma.csv", index=False)

    aktif = int(df["Aktiflik"].sum())
    kunye = {
        "hedef_chembl_id": TARGET_CHEMBL_ID,
        "hedef_adi": TARGET_ADI,
        "uniprot": UNIPROT,
        "aktivite_tipi": ACTIVITY_TYPE,
        "siniflandirma_esigi": args.esik,
        "uretim_tarihi": date.today().isoformat(),
        "ham_kayit": len(ham),
        "nihai_molekul": len(df),
        "aktif": aktif,
        "inaktif": len(df) - aktif,
        "aktif_yuzde": round(100 * aktif / len(df), 1),
        f"{hedef_kolon}_min": round(float(df[hedef_kolon].min()), 2),
        f"{hedef_kolon}_max": round(float(df[hedef_kolon].max()), 2),
        f"{hedef_kolon}_ortalama": round(float(df[hedef_kolon].mean()), 2),
        f"{hedef_kolon}_std": round(float(df[hedef_kolon].std()), 2),
        "mantik_araligi": list(MANTIK_ARALIGI),
        "pchembl_capraz_kontrol": kontrol,
        "temizlik_hunisi": [{"adim": a, "molekul": n} for a, n in huni],
        "esik_secenekleri": denge.to_dict(orient="records"),
    }

    if not args.tarama_atla:
        print("\nOnayli ilac kutuphanesi indiriliyor (sanal tarama icin)...")
        try:
            lib = onayli_ilaclari_indir()
        except Exception as exc:
            print(f"  !! Kutuphane indirilemedi: {exc}")
            print("     Ana veri setleri yazildi; kutuphane olmadan devam.")
            lib = pd.DataFrame()
    else:
        lib = pd.DataFrame()

    if not lib.empty:
        lib["Smiles"] = lib["Smiles"].apply(kanonik_smiles)
        lib = lib.dropna(subset=["Smiles"]).drop_duplicates(subset="Smiles")
        lib = lib[lib["Molekul_tipi"] == "Small molecule"].reset_index(drop=True)
        # Egitim setindeki molekuller silinmez, ISARETLENIR: bilinen aktiflerin
        # yuksek tahmin almasi modelin iyi bir saglik kontroludur.
        lib["Egitimde_var"] = lib["Smiles"].isin(set(df["Smiles"])).astype(int)
        lib.to_csv(cikti / "tarama_kutuphanesi.csv", index=False)
        kunye["tarama_kutuphanesi"] = {
            "molekul": len(lib),
            "egitim_setiyle_ortak": int(lib["Egitimde_var"].sum()),
        }
        print(f"  kutuphane molekul sayisi : {len(lib)}")
        print(f"  egitim setiyle ortak     : {int(lib['Egitimde_var'].sum())}")

    (cikti / f"{SLUG}_veri_kunyesi.json").write_text(
        json.dumps(kunye, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\nTamam. Dosyalar: {cikti}")
    print(f"  nihai molekul : {len(df)}")
    print(f"  aktif/inaktif : {aktif} / {len(df) - aktif}  "
          f"(%{kunye['aktif_yuzde']} aktif)")


if __name__ == "__main__":
    main()
