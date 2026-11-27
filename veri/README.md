# Veri Setleri

Bu klasördeki bütün dosyalar [`../araclar/veri_uret.py`](../araclar/veri_uret.py)
betiğiyle ChEMBL web servisinden üretilmiştir.

| | |
|---|---|
| **Kaynak** | ChEMBL web servisi (REST API) |
| **Üretim tarihi** | 11 Kasım 2026 |
| **Hedef** | NTRK1 / TrkA — ChEMBL `CHEMBL2815`, UniProt `P04629` |
| **Aktivite tipi** | IC50 (yalnızca kesin `=` ilişki, `nM` birimi) |
| **Hedef değişken** | `pIC50 = −log₁₀(IC50 [M])` |
| **Sınıflandırma eşiği** | `pIC50 ≥ 7.5` (IC50 ≤ 32 nM) |

---

## Dosyalar

| Dosya | Satır | İçerik |
|---|---|---|
| `ntrk1_ham_chembl.csv` | 8.414 | ChEMBL'den çekilen ham IC50 kayıtları, hiç işlenmemiş |
| `ntrk1_regresyon.csv` | 4.599 | `Smiles`, `pIC50` — Oturum 3'ün girdisi |
| `ntrk1_siniflandirma.csv` | 4.599 | `Smiles`, `pIC50`, `Aktiflik` — Oturum 4'ün girdisi |
| `tarama_kutuphanesi.csv` | 3.311 | Onaylanmış küçük moleküller — Oturum 6'nın sanal tarama kütüphanesi |
| `ntrk1_aktivite_tipleri.csv` | 6 | Hedefteki aktivite tiplerinin dağılımı |
| `ntrk1_veri_kunyesi.json` | — | Üretim künyesi: tarih, filtreler, küratörlük adımları, sınıf dengesi |

Veri setinin nasıl temizlendiği, hangi adımda kaç molekülün elendiği ve
dağılımın nasıl göründüğü **Oturum 1'de** adım adım üretilip tartışılmaktadır.
Aynı bilgiler `ntrk1_veri_kunyesi.json` dosyasında da kayıtlıdır.

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
| `Egitimde_var` | 1 ise bu molekül eğitim veri setinde de bulunuyor |

> **Not.** Kütüphane indirilirken ChEMBL servisinin kararsızlığı nedeniyle son
> sayfa kısmen alınabilmiştir; bu, alıştırmanın amacını etkilemez.

---

## Veriyi yeniden üretmek

```bash
cd araclar
python veri_uret.py --cikti ../veri --esik 7.5
```

İndirilmiş ham dosyayı yeniden kullanarak yalnızca temizlik hattını
tekrarlamak için:

```bash
python veri_uret.py --cikti ../veri --esik 7.5 --ham-kullan
```

> ChEMBL sürekli güncellenir; yeniden ürettiğinizde sayılar bu belgedeki
> değerlerden farklı olabilir. Bu normaldir ve Oturum 1'de veri sürümü
> bildirmenin neden zorunlu olduğu bağlamında tartışılmaktadır.

---

## Lisans ve atıf

Veriler ChEMBL'den türetilmiştir (CC BY-SA 3.0):

> Zdrazil, B., Felix, E., Hunter, F. et al. (2024). The ChEMBL Database in
> 2023. *Nucleic Acids Research*, 52(D1), D1180–D1192.
