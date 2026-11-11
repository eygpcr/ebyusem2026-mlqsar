# Veri Setleri

Bu klasördeki bütün dosyalar [`../araclar/veri_uret.py`](../araclar/veri_uret.py)
betiğiyle ChEMBL web servisinden üretilmiştir.

**Üretim tarihi:** 11 Kasım 2026
**Hedef:** NTRK1 / TrkA — ChEMBL `CHEMBL2815`, UniProt `P04629`
**Aktivite tipi:** IC50 (yalnızca kesin `=` ilişki, `nM` birimi)

---

## Dosyalar

| Dosya | Satır | İçerik |
|---|---|---|
| `ntrk1_ham_chembl.csv` | 8.414 | ChEMBL'den çekilen ham IC50 kayıtları, hiç işlenmemiş |
| `ntrk1_regresyon.csv` | 4.599 | `Smiles`, `pIC50` — Oturum 3'ün girdisi |
| `ntrk1_siniflandirma.csv` | 4.599 | `Smiles`, `pIC50`, `Aktiflik` — Oturum 4'ün girdisi |
| `tarama_kutuphanesi.csv` | 3.311 | Onaylanmış küçük moleküller — Oturum 6'nın sanal tarama kütüphanesi |
| `ntrk1_aktivite_tipleri.csv` | 6 | Hedefteki aktivite tiplerinin dağılımı |
| `ntrk1_veri_kunyesi.json` | — | Üretim künyesi: tarih, filtreler, huni, sınıf dengesi |

---

## Veri küratörlüğü hunisi

| Adım | Kalan molekül |
|---|---|
| Ham ChEMBL kayıtları | 8.414 |
| Kimlik + değer + SMILES tam olanlar | 8.414 |
| Sayısal ve pozitif değer | 8.414 |
| Molekül başına en potent ölçüm | 4.600 |
| Geçerli kanonik SMILES | 4.600 |
| Kanonik yapıya göre benzersiz | 4.600 |
| Mantıksal aralık filtresi (pIC50 3–12) | **4.599** |

### Elenen tek kayıt

`CHEMBL3671380` için IC50 = 9,8 × 10⁹ nM, yani **9,8 molar** olarak
girilmişti. Bu derişim deneysel olarak uygulanamaz; açık bir veri giriş
hatasıdır. Gerçek veride karşılaşılan kalite sorunu örneği olarak Oturum 1'de
tartışılmaktadır.

---

## Doğrulama

Hesapladığımız `pIC50` değerleri, ChEMBL'in kendi `pchembl_value` alanıyla
8.404 kayıtta karşılaştırıldı:

| | |
|---|---|
| Ortalama mutlak fark | 0,0023 |
| En büyük mutlak fark | 0,0055 |

Fark yalnızca yuvarlamadan kaynaklanmaktadır (ChEMBL iki ondalık basamak
saklar). Birim ve logaritma mantığı bağımsız bir kaynakla doğrulanmıştır.

---

## Özet istatistikler

| | |
|---|---|
| Molekül sayısı | 4.599 |
| pIC50 aralığı | 3,20 – 10,16 |
| pIC50 ortalama ± std | 7,32 ± 1,12 |
| Benzersiz Murcko iskeleti | 1.688 (%36,7) |
| Aktif / inaktif (eşik 7.0) | 2.899 / 1.700 (%63,0 aktif) |

---

## Tarama kütüphanesi

`tarama_kutuphanesi.csv`, ChEMBL'de `max_phase = 4` olan (yani **onaylanmış**)
küçük moleküllerden oluşur. Oturum 6'da bir **ilaç yeniden konumlandırma**
(drug repurposing) alıştırması için kullanılır.

| Kolon | İçerik |
|---|---|
| `molecule_chembl_id` | ChEMBL kimliği |
| `Isim` | İlacın adı |
| `Molekul_tipi` | `Small molecule` |
| `Smiles` | Kanonik SMILES |
| `Egitimde_var` | 1 ise bu molekül eğitim veri setinde de bulunuyor (14 molekül) |

`Egitimde_var` kolonu **silinmez, işaretlenir**: bilinen aktiflerin yüksek
tahmin alması modelin sağlık kontrolüdür.

> **Not.** Kütüphane indirilirken ChEMBL servisinin kararsızlığı nedeniyle
> son sayfa kısmen alınabilmiştir; bu, alıştırmanın amacını etkilemez.

---

## Veriyi yeniden üretmek

```bash
cd araclar
python veri_uret.py --cikti ../veri --esik 7.0
```

İndirilmiş ham dosyayı yeniden kullanarak yalnızca temizlik hattını
tekrarlamak için:

```bash
python veri_uret.py --cikti ../veri --esik 7.0 --ham-kullan
```

> ChEMBL sürekli güncellenir; yeniden ürettiğinizde sayılar bu belgedeki
> değerlerden farklı olabilir. Bu normaldir ve Oturum 1'de veri sürümü
> bildirmenin neden zorunlu olduğu bağlamında tartışılmaktadır.

---

## Lisans ve atıf

Veriler ChEMBL'den türetilmiştir (CC BY-SA 3.0):

> Zdrazil, B., Felix, E., Hunter, F. et al. (2024). The ChEMBL Database in
> 2023. *Nucleic Acids Research*, 52(D1), D1180–D1192.
