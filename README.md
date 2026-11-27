# Yapay Zekâ Destekli İlaç Tasarımı

**Makine öğrenmesi tabanlı QSAR (ML-QSAR) uygulamalı eğitimi**

Erzincan Binali Yıldırım Üniversitesi — Sürekli Eğitim Uygulama ve Araştırma Merkezi

- **Tarih:** 28–29 Kasım 2026 (Cumartesi – Pazar), 09:30–16:30
- **Süre:** 12 saat / 2 gün
- **Yer:** EBYÜ Sürekli Eğitim Merkezi Derslikleri
- **Kontenjan:** 15 kursiyer
- **Kurs sayfası:** https://sem.ebyu.edu.tr/ilac_tsrm/

Bu depo kursun bütün eğitim materyalini içerir: altı Google Colab not defteri,
hazır veri setleri, teorik oturum notları ve kurs sonrası çalışma kaynakları.

---

## Eğitim sorumlusu

| | |
|---|---|
| **Dr. Öğr. Üyesi Ekrem Yaşar** | Erzincan Binali Yıldırım Üniversitesi, Tıp Fakültesi, Biyofizik Anabilim Dalı |

---

## Kursun amacı ve kapsamı

Kurs, ilaç keşfi ve geliştirme süreçlerinde yapay zekâ ve makine öğrenmesi
tabanlı QSAR yaklaşımlarının temel ilkelerini **uçtan uca uygulamalı** biçimde
öğretmeyi amaçlar.

Kurs boyunca tek bir gerçek hedef üzerinde ilerlenir: **NTRK1 (TrkA)**. Veri
ChEMBL'den çekilir, temizlenir, moleküller sayısal temsillere çevrilir,
regresyon ve sınıflandırma modelleri kurulup optimize edilir, sonuçlar
açıklanabilir yapay zekâ (SHAP) ile yorumlanır, uygulanabilirlik alanı
belirlenir ve son olarak yeni moleküller taranarak aday listesi SDF
dosyaları hâlinde üretilir.

**Kapsam sınırı.** Kursta moleküler doklama ve dinamik simülasyon
yürütülmemektedir. Odak, bir ML-QSAR iş akışının doğru biçimde kurulması ve
değerlendirilmesidir. Üretilen SDF dosyaları, doklama
çalışmalarına girdi olacak biçimde hazırlanır.

### Öğrenim kazanımları

Kursun sonunda katılımcıların şunları yapabilmesi hedeflenir:

1. ChEMBL veritabanından programatik olarak biyoaktivite verisi çekmek ve
   modellenebilir hâle getirmek
2. Veri sızıntısına yol açan yaygın hataları (kanonikleştirme eksikliği,
   global ölçekleme, test setinin erken kullanımı) tanımak ve önlemek
3. Molekülleri betimleyici ve parmak izi temsillerine çevirmek, bu temsilleri
   karşılaştırmak
4. Regresyon ve sınıflandırma modelleri kurmak, LazyPredict ile eleme ve
   Optuna ile hiperparametre optimizasyonu yapmak
5. Bir QSAR modelini doğru metriklerle değerlendirmek: çapraz doğrulama,
   iskelet bazlı bölünme, y-randomizasyon, dengesiz veride metrik seçimi
6. SHAP ile model kararlarını küresel ve yerel düzeyde açıklamak
7. Williams grafiği ve Tanimoto benzerliği ile uygulanabilirlik alanı
   belirlemek
8. Yeni molekülleri tarayıp sonuçları SDF biçiminde raporlamak

**Ön koşul.** Bulunmamaktadır. İleri düzey programlama veya makine öğrenmesi
bilgisi gerekmez; Python söz dizimine aşinalık yararlıdır ancak zorunlu
değildir.

---

## Başlangıç

1. [KURULUM.md](KURULUM.md) dosyasındaki hazırlıkları **kurs gününden önce**
   tamamlayın. Yalnızca bir Google hesabı ve güncel bir tarayıcı gerekir;
   bilgisayarınıza hiçbir yazılım kurmanız gerekmez.
2. Kurs günü her oturum, aşağıdaki tablodaki Colab bağlantısı açılarak
   yürütülür.

---

## Program

### 1. Gün — 28 Kasım 2026, Cumartesi

| Saat | Oturum | Not defteri |
|---|---|---|
| 09:30–10:15 | [Teori 1: İlaç keşif süreci ve bilgisayar destekli tasarım](01_teori/) | |
| 10:15–10:30 | Ara | |
| 10:30–11:15 | [Teori 2: QSAR ve makine öğrenmesinin temelleri](01_teori/) | |
| 11:15–11:30 | Ara | |
| 11:30–12:30 | **Oturum 1 — Biyoaktivite verisinin hazırlanması** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/01_veri_hazirlama.ipynb) |
| 12:30–13:30 | Öğle arası | |
| 13:30–14:45 | **Oturum 2 — Molekülü sayıya çevirmek: betimleyiciler ve parmak izleri** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/02_ozellik_uretimi.ipynb) |
| 14:45–15:00 | Ara | |
| 15:00–16:30 | **Oturum 3 — Regresyon modelleri** (I. bölüm: bölünme ve model taraması) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/03_regresyon_modelleri.ipynb) |

### 2. Gün — 29 Kasım 2026, Pazar

| Saat | Oturum | Not defteri |
|---|---|---|
| 09:30–10:15 | [Teori 3: Moleküler temsil, açıklanabilirlik ve uygulanabilirlik alanı](01_teori/) | |
| 10:15–10:30 | Ara | |
| 10:30–11:45 | **Oturum 3 — Regresyon modelleri** (II. bölüm: Optuna, çapraz doğrulama, y-randomizasyon) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/03_regresyon_modelleri.ipynb) |
| 11:45–12:00 | Ara | |
| 12:00–12:45 | **Oturum 4 — Sınıflandırma modelleri** (I. bölüm) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/04_siniflandirma_modelleri.ipynb) |
| 12:45–13:45 | Öğle arası | |
| 13:45–14:45 | **Oturum 4 — Sınıflandırma modelleri** (II. bölüm: metrikler, karar eşiği) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/04_siniflandirma_modelleri.ipynb) |
| 14:45–15:00 | Ara | |
| 15:00–15:45 | **Oturum 5 — Model karşılaştırma, SHAP ve uygulanabilirlik alanı** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/05_karsilastirma_shap_ad.ipynb) |
| 15:45–16:30 | **Oturum 6 — Yeni molekülleri taramak ve SDF çıktısı** + değerlendirme | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/06_tahmin_ve_sdf.ipynb) |

> Not defterleri **sırayla** çalıştırılmak üzere tasarlanmıştır: her oturumun
> çıktısı bir sonrakinin girdisidir. Bir oturumu kaçıranlar, depodaki hazır
> veri dosyalarından devam edebilir.

---

## Hedef protein: NTRK1 (TrkA)

| | |
|---|---|
| **Protein** | High affinity nerve growth factor receptor |
| **Gen** | `NTRK1` |
| **UniProt** | [P04629](https://www.uniprot.org/uniprotkb/P04629) |
| **ChEMBL hedef** | [CHEMBL2815](https://www.ebi.ac.uk/chembl/target_report_card/CHEMBL2815/) |
| **Protein sınıfı** | Reseptör tirozin kinaz (RTK) |
| **Doğal ligandı** | Sinir büyüme faktörü (NGF) |

**Neden bu hedef seçildi?**

1. **Klinik olarak doğrulanmış ve güncel.** `NTRK` gen füzyonlarını hedefleyen
   **larotrektinib** ve **entrektinib**, FDA tarihinde ilk kez tümörün
   bulunduğu dokuya değil, taşıdığı genetik değişime göre onaylanan ilaçlar
   oldu (tümör-agnostik onay). Hedef, moleküler belirteç temelli ilaç
   tasarımının ders kitabı örneğidir.
2. **Veri açısından zengin.** ChEMBL'de bu hedef için **10.600'den fazla
   IC50 kaydı** bulunur; bunların **8.414'ü** kesin (`=`) ilişkili ve `nM`
   birimli ölçümdür — hem regresyon hem sınıflandırma için fazlasıyla yeterli.
   Kalan ~2.200 kayıt sansürlüdür (`>`, `<`); bunların neden regresyona
   katılmadığı Oturum 1'de tartışılmaktadır.
3. **Direnç sorunu gerçek.** Birinci nesil inhibitörlere karşı gelişen direnç
   mutasyonları (G595R, G667C) ikinci nesil ilaçların geliştirilmesini
   gerektirdi; aktiflik tahmininin neden sürekli yenilenen bir problem olduğunu
   gösterir.
4. **Sanal tarama için doğal bir sağlık kontrolü sunar.** Oturum 6'da
   taradığımız onaylanmış ilaç kütüphanesinde larotrektinib ve entrektinib
   zaten bulunur; modelin onları üst sıralara taşıyıp taşımadığı doğrudan
   ölçülebilir.

NTRK1 ayrıca ağrı biyolojisinde merkezi bir rol oynar (NGF–TrkA yolağı); bu
nedenle onkoloji dışında analjezik geliştirme çalışmalarının da hedefidir.

---

## Veri setleri

Bütün veri dosyaları [`03_veri/`](03_veri/) klasöründedir ve
[`04_araclar/veri_uret.py`](04_araclar/veri_uret.py) betiğiyle ChEMBL'den
üretilmiştir. Not defterleri bu dosyaları doğrudan GitHub'dan okur; ayrıca
indirmeniz gerekmez.

### Hangi dosya ne için?

Tablo **oturum sırasına** göre düzenlenmiştir: üstteki dosyalar kursun başında,
alttakiler sonunda kullanılır.

| Oturum | Dosya | Ne işe yarar? |
|---|---|---|
| **1** | `ntrk1_aktivite_tipleri.csv` | Hedefte hangi ölçüm tipinin (IC50, Ki, Kd, EC50) kaç kaydı olduğunu gösterir. Oturum 1'deki **"neden IC50 ile çalışıyoruz?"** kararının dayanağıdır. |
| **1** | `ntrk1_ham_chembl.csv` | **Temizlik hattının başlangıç noktası.** ChEMBL'den geldiği gibi, hiç işlenmemiş kayıtlar. Oturum 1 bu dosyayı temiz bir veri setine dönüştürür. |
| **1** | `chembl_disa_aktarim/` | **ChEMBL çökerse sigortanız.** ChEMBL'in web arayüzünden indirilmiş ham dışa aktarımlar (zip'li, değiştirilmemiş). Oturum 1 bunları Drive'ınıza indirip ChEMBL'e hiç bağlanmadan bütün hattı çalıştırabilir ve **birebir aynı** veri setini üretir. |
| **3** | `ntrk1_regresyon.csv` | **Oturum 3'ün girdisi.** Her satır bir molekül: SMILES yapısı ve ölçülmüş `pIC50` değeri. Regresyon modelleri aktiviteyi sayı olarak tahmin etmeyi bu dosyadan öğrenir. |
| **4** | `ntrk1_siniflandirma.csv` | **Oturum 4'ün girdisi.** Aynı moleküller, ek olarak `Aktiflik` etiketi (0/1). Sınıflandırma modelleri "aktif mi değil mi" sorusunu bu dosyadan öğrenir. |
| **6** | `tarama_kutuphanesi.csv` | **Oturum 6'nın girdisi.** Onaylanmış ilaçlardan oluşan sanal tarama kütüphanesi. Eğitilmiş modeller bu daha önce denenmemiş moleküller üzerinde tahmin üretir; aday listesi buradan çıkar. |
| — | `ntrk1_veri_kunyesi.json` | Veri setinin kimlik kartı: üretim tarihi, uygulanan filtreler, küratörlük adımları ve sınıf dengesi. Çalışmanın tekrar üretilebilmesi için saklanır. |

> **Oturum 2** ve **Oturum 5** bu klasörden dosya okumaz: Oturum 2 kendi özellik
> dosyalarını üretir, Oturum 5 ise Oturum 3 ve 4'ün çıktılarını kullanır. İkisi
> de sonuçlarını Google Drive'daki proje klasörünüze yazar.

Dosyaların ayrıntılı künyesi ve kolon şeması
[`03_veri/README.md`](03_veri/README.md) dosyasındadır.

---

## Hesaplama ortamı

Bütün uygulamalar **Google Colab** üzerinde yürütülür. Katılımcıların kendi
bilgisayarlarına yazılım kurmaları gerekmez; güncel bir tarayıcı yeterlidir.

- **GPU gereksinimi yoktur.** Kullanılan modeller (ağaç toplulukları, SVM,
  gradyan artırma) CPU üzerinde çalışır; ücretsiz Colab çalışma zamanı
  yeterlidir.
- Not defterleri Colab dışında, yerel bir Jupyter ortamında da çalışır: Drive
  bulunamazsa otomatik olarak yerel bir klasöre düşerler.

### Kullanılan kütüphaneler

| Kütüphane | Ne için? |
|---|---|
| [RDKit](https://www.rdkit.org/) | Kemoinformatik: SMILES işleme, betimleyiciler, parmak izleri, SDF |
| [scikit-learn](https://scikit-learn.org/) | Model kurma, çapraz doğrulama, metrikler, `Pipeline` |
| [LazyPredict](https://github.com/shankarpandala/lazypredict) | Onlarca modeli tek komutla tarayıp elemek |
| [Optuna](https://optuna.org/) | Hiperparametre optimizasyonu (TPE) |
| [XGBoost](https://xgboost.readthedocs.io/) | Gradyan artırmalı ağaçlar |
| [SHAP](https://shap.readthedocs.io/) | Açıklanabilir yapay zekâ |

### Çıktıların saklanması

Colab çalışma zamanı sonlandığında üretilen dosyalar silinir. Bu nedenle bütün
not defterleri çıktıları katılımcının kendi Google Drive hesabına kaydeder:

```
Drive'ım/
└── EBYUSEM2026_MLQSAR/
    ├── ntrk1_regresyon.csv                  Oturum 1
    ├── ntrk1_siniflandirma.csv              Oturum 1
    ├── ntrk1_descriptors.csv                Oturum 2
    ├── ntrk1_ecfp4.csv                      Oturum 2
    ├── ntrk1_maccs.csv                      Oturum 2
    ├── ntrk1_en_iyi_regresyon_modeli.joblib Oturum 3
    ├── ntrk1_en_iyi_siniflandirma_modeli.joblib  Oturum 4
    ├── ntrk1_ad_parametreleri.json          Oturum 5
    ├── ntrk1_secilen_adaylar.csv            Oturum 6
    └── sdf_ciktilari/                       Oturum 6
        ├── ntrk1_adaylar_top25.sdf          tek birleşik dosya
        ├── ntrk1_adaylar_sdf.zip            hepsi bir arşivde
        └── molekul_basina/                  molekül başına ayrı SDF
            ├── 01_Larotrectinib.sdf
            └── ...
```

Klasör, ilk not defterinin ikinci hücresi çalıştırıldığında otomatik
oluşturulur. **Bütün oturumlar aynı klasörü paylaşır** — bir oturumun çıktısı
bir sonrakinin girdisi olduğu için klasör adını değiştirmeyin.

---

## Depo yapısı

```
ebyusem2026-mlqsar/
├── README.md                    bu dosya
├── KURULUM.md                   kurs öncesi hazırlık
├── ILERI_OKUMA.md               kaynaklar ve devam yolları
├── LICENSE                      CC BY 4.0
├── 01_teori/                    teorik oturumların içerik planı
├── 02_notebooks/                altı Colab not defteri
├── 03_veri/                     veri setleri ve ham ChEMBL dışa aktarımları
└── 04_araclar/                  veri üretim betiği (eğitmen için)
```

---

## Kaynaklar ve atıf

Bu depodaki materyal aşağıdaki açık kaynaklardan yararlanılarak hazırlanmıştır.
Ayrıntılı okuma listesi [ILERI_OKUMA.md](ILERI_OKUMA.md) dosyasındadır.

- **ChEMBL** — Zdrazil, B. et al. (2024). *Nucleic Acids Research*, 52(D1),
  D1180–D1192. https://www.ebi.ac.uk/chembl/
- **RDKit** — Landrum, G. *RDKit: Open-source cheminformatics.*
  https://www.rdkit.org
- **scikit-learn** — Pedregosa, F. et al. (2011). *JMLR*, 12, 2825–2830.
- **Optuna** — Akiba, T. et al. (2019). *KDD '19*, 2623–2631.
- **SHAP** — Lundberg, S. M. & Lee, S.-I. (2017). *NeurIPS 30*.
- **OECD QSAR doğrulama ilkeleri** — OECD (2007). *Guidance Document on the
  Validation of (Q)SAR Models.*

Kurs materyali **CC BY 4.0** lisansı ile sunulmaktadır; bkz. [LICENSE](LICENSE).
Derslerinizde kullanabilir, uyarlayabilir ve dağıtabilirsiniz — kaynak
göstermeniz yeterlidir.

---

## İletişim

| | |
|---|---|
| **Dr. Öğr. Üyesi Ekrem Yaşar** | `ey.biophysics@gmail.com` |
| **Kurs kaydı ve EBYÜ SEM** | https://sem.ebyu.edu.tr/ilac_tsrm/ |

Depo içeriğine ilişkin teknik bildirimler için deponun *Issues* bölümünü
kullanabilirsiniz.
