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
| **Dr. Öğr. Üyesi Ekrem Yaşar** | Erzincan Binali Yıldırım Üniversitesi, Biyofizik Anabilim Dalı |

---

## Kursun amacı ve kapsamı

Kurs, ilaç keşfi ve geliştirme süreçlerinde yapay zekâ ve makine öğrenmesi
tabanlı QSAR yaklaşımlarının temel ilkelerini **uçtan uca uygulamalı** biçimde
öğretmeyi amaçlar.

Kurs boyunca tek bir gerçek hedef üzerinde ilerlenir: **NTRK1 (TrkA)**. Veri
ChEMBL'den çekilir, temizlenir, moleküller sayısal temsillere çevrilir,
regresyon ve sınıflandırma modelleri kurulup optimize edilir, sonuçlar
açıklanabilir yapay zekâ (SHAP) ile yorumlanır, uygulanabilirlik alanı
belirlenir ve son olarak yeni moleküller taranarak aday listesi **SDF
dosyaları** hâlinde üretilir.

**Kapsam sınırı.** Kursta moleküler doklama ve dinamik simülasyon
yürütülmemektedir. Odak, bir ML-QSAR iş akışının doğru biçimde kurulması ve
**dürüst biçimde değerlendirilmesidir**. Üretilen SDF dosyaları, doklama
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
| 11:30–12:30 | **Oturum 1 — Biyoaktivite verisinin hazırlanması** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/01_veri_hazirlama.ipynb) |
| 12:30–13:30 | Öğle arası | |
| 13:30–14:45 | **Oturum 2 — Molekülü sayıya çevirmek: betimleyiciler ve parmak izleri** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/02_ozellik_uretimi.ipynb) |
| 14:45–15:00 | Ara | |
| 15:00–16:30 | **Oturum 3 — Regresyon modelleri** (I. bölüm: bölünme ve model taraması) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/03_regresyon_modelleri.ipynb) |

### 2. Gün — 29 Kasım 2026, Pazar

| Saat | Oturum | Not defteri |
|---|---|---|
| 09:30–10:15 | [Teori 3: Moleküler temsil, açıklanabilirlik ve uygulanabilirlik alanı](01_teori/) | |
| 10:15–10:30 | Ara | |
| 10:30–11:45 | **Oturum 3 — Regresyon modelleri** (II. bölüm: Optuna, çapraz doğrulama, y-randomizasyon) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/03_regresyon_modelleri.ipynb) |
| 11:45–12:00 | Ara | |
| 12:00–12:45 | **Oturum 4 — Sınıflandırma modelleri** (I. bölüm) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/04_siniflandirma_modelleri.ipynb) |
| 12:45–13:45 | Öğle arası | |
| 13:45–14:45 | **Oturum 4 — Sınıflandırma modelleri** (II. bölüm: metrikler, karar eşiği) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/04_siniflandirma_modelleri.ipynb) |
| 14:45–15:00 | Ara | |
| 15:00–15:45 | **Oturum 5 — Model karşılaştırma, SHAP ve uygulanabilirlik alanı** | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/05_karsilastirma_shap_ad.ipynb) |
| 15:45–16:30 | **Oturum 6 — Yeni molekülleri taramak ve SDF çıktısı** + değerlendirme | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/notebooks/06_tahmin_ve_sdf.ipynb) |

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
2. **Veri açısından zengin.** ChEMBL'de 8.400'den fazla kesin IC50 ölçümü
   bulunur — hem regresyon hem sınıflandırma için yeterli.
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

Bütün veri dosyaları [`veri/`](veri/) klasöründedir ve
[`araclar/veri_uret.py`](araclar/veri_uret.py) betiğiyle ChEMBL'den
üretilmiştir. Not defterleri bu dosyaları doğrudan GitHub'dan okuyabilir.

Veri setinin ayrıntılı künyesi, küratörlük adımları ve istatistikleri
[`veri/README.md`](veri/README.md) dosyasındadır.

### Künye

| | |
|---|---|
| **Kaynak** | ChEMBL web servisi (REST API) |
| **Üretim tarihi** | 11 Kasım 2026 |
| **Aktivite tipi** | IC50, yalnızca kesin (`=`) ilişki ve `nM` birimi |
| **Hedef değişken** | `pIC50 = −log₁₀(IC50 [M])` |
| **Sınıflandırma eşiği** | `pIC50 ≥ 7.5` (IC50 ≤ 32 nM) |

### Eşik seçimi

Sınıflandırma için moleküller **aktif** ve **inaktif** diye ikiye ayrılır. Bu
kursta eşik **`pIC50 ≥ 7.5`** (IC50 ≤ 32 nM) olarak seçilmiştir; seçim iki
ölçütü birlikte karşılar:

- **Farmakolojik olarak savunulabilir.** 32 nM, kinaz inhibitörü geliştirmede
  optimize edilmiş bileşik aralığıdır.
- **Sınıfları neredeyse tam ortadan böler.** Böylece Oturum 4'teki metrikler
  sınıf dengesizliğinden gölgelenmeden okunabilir.

Eşik seçiminin neden bilimsel bir karar olduğu ve farklı eşiklerin veri setini
nasıl böldüğü **Oturum 1 ve Oturum 4'te** uygulamalı olarak tartışılmaktadır.
Eşiği değiştirmek tek satırlık bir işlemdir: Oturum 1'de `AKTIFLIK_ESIGI`,
Oturum 4'te `ESIK`.

### Dosyalar

| Dosya | İçerik |
|---|---|
| `ntrk1_ham_chembl.csv` | ChEMBL'den çekilen 8.414 ham IC50 kaydı |
| `ntrk1_regresyon.csv` | `Smiles`, `pIC50` — regresyon veri seti |
| `ntrk1_siniflandirma.csv` | `Smiles`, `pIC50`, `Aktiflik` — sınıflandırma veri seti |
| `tarama_kutuphanesi.csv` | 3.311 onaylanmış küçük molekül (sanal tarama kütüphanesi) |
| `ntrk1_veri_kunyesi.json` | Üretim künyesi: tarih, filtreler, huni, sınıf dengesi |
| `ntrk1_aktivite_tipleri.csv` | Hedefteki aktivite tiplerinin dağılımı |

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

## Bilinen sorun: ChEMBL servisinin kararsızlığı

Kurs materyali hazırlanırken ChEMBL web servisinin, isteklerin yaklaşık
**yarısını** rastgele `500` hatasıyla reddettiği bir dönem gözlendi. Hata
sorgunun biçiminden bağımsızdır: aynı istek bir denemede başarısız olurken
bir sonrakinde çalışabilir.

Bu nedenle:

- Not defterlerindeki bütün ChEMBL sorguları **artan bekleme süreleriyle
  yeniden deneme** (exponential backoff) mantığı içerir.
- Canlı sorgular başarısız olduğunda oturum kesilmez: not defterleri
  depodaki **hazır veri dosyalarına** düşer.
- Oturum 1, iki yolu (canlı sorgu ve dondurulmuş veri) karşılaştırmalı olarak
  gösterir; bu, veri sürümü bildirmenin neden zorunlu olduğunu anlatan
  doğal bir örnektir.

Canlı sorgu derste çalışmazsa, bu bir kurulum hatası değildir — `VERI_KAYNAGI`
ayarını `"depo"` yapıp devam edin.

---

## Depo yapısı

```
ebyusem2026-mlqsar/
├── README.md                    bu dosya
├── KURULUM.md                   kurs öncesi hazırlık
├── ILERI_OKUMA.md               kaynaklar ve devam yolları
├── LICENSE                      CC BY 4.0
├── 01_teori/                    teorik oturumların içerik planı
├── notebooks/                   altı Colab not defteri
├── veri/                        hazır veri setleri ve künye
└── araclar/                     veri üretim betiği (eğitmen için)
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
