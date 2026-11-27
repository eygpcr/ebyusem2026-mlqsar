# Veri Setleri

Bu klasördeki bütün dosyalar [`../04_araclar/veri_uret.py`](../04_araclar/veri_uret.py)
betiğiyle ChEMBL web servisinden üretilmiştir.

| | |
|---|---|
| **Kaynak** | ChEMBL web servisi (REST API) |
| **Üretim tarihi** | 11 Kasım 2026 |
| **Hedef** | NTRK1 / TrkA — ChEMBL `CHEMBL2815`, UniProt `P04629` |
| **Aktivite tipi** | IC50 (yalnızca kesin `=` ilişki, `nM` birimi) |
| **Hedefteki IC50 kaydı** | ChEMBL'de toplam 10.647; kesin ve nM olan 8.414 |
| **Hedef değişken** | `pIC50 = −log₁₀(IC50 [M])` |
| **Sınıflandırma eşiği** | Kursta, Oturum 1'de dağılıma bakılarak seçilir. Buradaki dosyalar varsayılan seçimi taşır: dağılımın **medyanı** (`esik_secimi.json`). |

---

## Dosyalar

| Dosya | Satır | İçerik |
|---|---|---|
| `ntrk1_ham_ic50.csv` | 10.647 | ChEMBL'deki bütün IC50 kayıtları, hiç süzülmemiş. Oturum 1'in dokuz adımlı temizliği buradan başlar |
| `ntrk1_regresyon.csv` | 4.599 | `Smiles`, `pIC50` — Oturum 3'ün girdisi |
| `ntrk1_siniflandirma.csv` | 4.599 | `Smiles`, `pIC50`, `Aktiflik` — Oturum 4'ün girdisi |
| `tarama_kutuphanesi.csv` | 12.032 | Klinik aşama (faz 1–4) küçük molekülleri — Oturum 6'nın sanal tarama kütüphanesi |
| `esik_secimi.json` | — | Varsayılan sınıflandırma eşiği kararı; Oturum 2, 4, 5 ve 6 bunu okur |
| `ntrk1_aktivite_tipleri.csv` | 6 | Hedefteki aktivite tiplerinin dağılımı |
| `ntrk1_veri_kunyesi.json` | — | Üretim künyesi: tarih, filtreler, küratörlük adımları, sınıf dengesi |
| [`chembl_disa_aktarim/`](chembl_disa_aktarim/) | 10.647 + 26.746 | ChEMBL web arayüzünden indirilmiş ham dışa aktarımlar (zip'li). ChEMBL erişilemezse Oturum 1 bu dosyalardan çalışır. |

Veri setinin nasıl temizlendiği, hangi adımda kaç molekülün elendiği ve
dağılımın nasıl göründüğü **Oturum 1'de** adım adım üretilip tartışılmaktadır.
Aynı bilgiler `ntrk1_veri_kunyesi.json` dosyasında da kayıtlıdır.

---

## Tarama kütüphanesi

`tarama_kutuphanesi.csv`, ChEMBL'de **klinik aşamaya gelmiş** (`max_phase`
1, 2, 3 veya 4) küçük moleküllerden oluşur. Oturum 6'da bir **ilaç yeniden
konumlandırma** (drug repurposing) alıştırması için kullanılır.

| Faz | Molekül | Anlamı |
|---|---|---|
| 1 | 950 | İnsanda ilk deneme |
| 2 | 6.658 | Küçük hasta grubunda etkinlik |
| 3 | 1.113 | Geniş ölçekli doğrulama |
| **4** | **3.311** | **Onaylanmış ilaç** |

Yalnızca onaylı ilaçlarla sınırlı kalmamamızın nedeni: faz 4 havuzu kinaz
inhibitörü bakımından fakirdir, faz 1–3 ise zengindir — tam da modelimizin
tanıdığı kimyasal uzay.

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
python veri_uret.py --cikti ../03_veri
```

İndirilmiş ham dosyayı yeniden kullanarak yalnızca temizlik hattını
tekrarlamak için:

```bash
python veri_uret.py --cikti ../03_veri --ham-kullan
```

> ChEMBL sürekli güncellenir; yeniden ürettiğinizde sayılar bu belgedeki
> değerlerden farklı olabilir. Bu normaldir ve Oturum 1'de veri sürümü
> bildirmenin neden zorunlu olduğu bağlamında tartışılmaktadır.

---

## Lisans ve atıf

Veriler ChEMBL'den türetilmiştir (CC BY-SA 3.0):

> Zdrazil, B., Felix, E., Hunter, F. et al. (2024). The ChEMBL Database in
> 2023. *Nucleic Acids Research*, 52(D1), D1180–D1192.
