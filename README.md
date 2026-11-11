# Yapay Zekâ Destekli İlaç Tasarımı

**Makine öğrenmesi tabanlı QSAR (ML-QSAR) uygulamalı eğitimi**

Erzincan Binali Yıldırım Üniversitesi — Sürekli Eğitim Uygulama ve Araştırma Merkezi

- **Tarih:** 14–15 Kasım 2026 (Cumartesi – Pazar), 09:30–16:30
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

### 1. Gün — 14 Kasım 2026, Cumartesi

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

### 2. Gün — 15 Kasım 2026, Pazar

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
[`araclar/veri_uret.py`](araclar/veri_uret.py) betiğiyle üretilmiştir.
Not defterleri bu dosyaları doğrudan GitHub'dan okuyabilir.

### Künye

| | |
|---|---|
| **Kaynak** | ChEMBL web servisi (REST API) |
| **Üretim tarihi** | 11 Kasım 2026 |
| **Aktivite tipi** | IC50, yalnızca kesin (`=`) ilişki ve `nM` birimi |
| **Hedef değişken** | `pIC50 = −log₁₀(IC50 [M])` |
| **Sınıflandırma eşiği** | `pIC50 ≥ 7.0` (IC50 ≤ 100 nM) |

### Veri küratörlüğü hunisi

| Adım | Kalan molekül |
|---|---|
| Ham ChEMBL kayıtları | 8.414 |
| Molekül başına en potent ölçüm | 4.600 |
| Kanonik SMILES'a göre benzersiz yapı | 4.600 |
| Mantıksal aralık filtresi (pIC50 3–12) | **4.599** |

> Son adımda elenen tek kayıt (CHEMBL3671380) IC50 = 9,8 × 10⁹ nM, yani
> **9,8 molar** olarak girilmişti — deneysel olarak uygulanamaz bir derişim.
> Gerçek veride karşılaşılan bir giriş hatası örneği olarak Oturum 1'de
> tartışılmaktadır.

**Doğrulama.** Hesapladığımız pIC50 değerleri, ChEMBL'in kendi
`pchembl_value` alanıyla 8.404 kayıtta karşılaştırıldı; en büyük fark
**0,0055** (yuvarlama kaynaklı). Birim ve logaritma mantığı doğrulanmıştır.

### Özet istatistikler

| | |
|---|---|
| **Molekül sayısı** | 4.599 |
| **pIC50 aralığı** | 3,20 – 10,16 |
| **pIC50 ortalama ± std** | 7,32 ± 1,12 |
| **Benzersiz Murcko iskeleti** | 1.688 (%36,7 çeşitlilik) |
| **Aktif / inaktif (eşik 7.0)** | 2.899 / 1.700 (%63,0 aktif) |

### Sınıflandırma eşiği seçenekleri

Eşik seçimi bilimsel bir karardır; Oturum 1 ve 4'te tartışılmaktadır.

| Eşik (pIC50) | IC50 | Aktif | İnaktif | Aktif % |
|---|---|---|---|---|
| 6.0 | 1 µM | 4.019 | 580 | 87,4 |
| 6.5 | 316 nM | 3.448 | 1.151 | 75,0 |
| **7.0** | **100 nM** | **2.899** | **1.700** | **63,0** |
| 7.5 | 32 nM | 2.121 | 2.478 | 46,1 |
| 8.0 | 10 nM | 1.353 | 3.246 | 29,4 |

Kursta **7.0** kullanılmaktadır: 100 nM, kinaz inhibitörü geliştirmede yaygın
kabul gören bir "ilaç benzeri potens" sınırıdır. Daha dengeli bir sınıf
dağılımı isteyenler Oturum 4'te eşiği 7.5 yapıp sonuçları karşılaştırabilir.

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

## Kurs hazırlığında ölçülen örnek sonuçlar

Aşağıdaki değerler, bütün not defterleri uçtan uca çalıştırılarak elde
edilmiştir. **Kesin sayılar** Optuna deneme sayısına, rastgele tohuma ve
ChEMBL sürümüne göre değişir; buradaki amaç katılımcıların ne beklemesi
gerektiğini göstermektir.

### Oturum 3 — regresyon (`pIC50`, betimleyici temsili)

| Ölçüm | Değer |
|---|---|
| LazyPredict taraması (en iyi, doğrulama) | `HistGradientBoostingRegressor`, R² ≈ 0,62 |
| Eğitim R² (yeniden uyum) | ≈ 0,93 |
| **Çapraz doğrulama Q² (5 kat)** | **≈ 0,61** |
| **Test R² (tutulan set)** | **≈ 0,69** |
| Test RMSE | ≈ 0,65 `pIC50` birimi |
| Test MAE | ≈ 0,47 |

RMSE ≈ 0,65 demek, tipik tahminlerin aktivitede yaklaşık **4,5 kat** içinde
isabet ettiği anlamına gelir — ilaç keşfinde kullanışlı bir doğruluktur.
Karşılaştırma noktası olarak hedefin standart sapması 1,12'dir.

### Üç temsilin karşılaştırması

| Temsil | En iyi doğrulama R² |
|---|---|
| RDKit betimleyiciler (163 özellik) | ≈ 0,62 |
| MACCS anahtarları (167 bit) | ≈ 0,57 |

Yorumlanabilir fizikokimyasal betimleyicilerin, aynı boyuttaki yapısal
anahtarlardan daha iyi sonuç vermesi bu veri setinin öğretici bir bulgusudur.

### Doğrulama testleri — kursun asıl vurgusu

| Test | Sonuç | Yorum |
|---|---|---|
| **y-randomizasyon** (10 tekrar) | Gerçek CV R² ≈ 0,61 · karıştırılmış en iyi ≈ **−0,16** | Uçurum ≈ 0,77. Model gerçek bir yapı–aktivite ilişkisi öğrenmiş. |
| **İskelet bazlı bölünme** | Test R² 0,69 → **0,49** | Rastgele bölünme performansı ≈ 0,20 R² **fazla** gösteriyor. |
| **Eğitim − CV farkı** | 0,93 − 0,61 = **0,32** | Belirgin aşırı öğrenme; not defteri bunu uyarı olarak bildirir. |

Son iki satır kursun en önemli iki dersidir: rastgele bölünme iyimserdir ve
eğitim skoru yanıltıcıdır.

### Oturum 4 — sınıflandırma (eşik `pIC50 ≥ 7,0`)

| Ölçüm | Değer |
|---|---|
| LazyPredict taraması (en iyi) | `RandomForestClassifier` |
| Temel çizgi doğruluğu (çoğunluk sınıfı) | 0,63 |
| Doğruluk | ≈ 0,82 |
| Dengeli doğruluk | ≈ 0,80 |
| ROC-AUC | ≈ 0,88 |

Doğruluğun temel çizgiyi (%63) belirgin biçimde aşması ve dengeli doğruluğun
0,50'nin çok üstünde olması, modelin gerçekten öğrendiğini gösterir.

### Oturum 6 — sanal tarama doğrulaması

Onaylanmış ilaç kütüphanesi (2.999 küçük molekül) tarandığında, **gerçek NTRK
inhibitörleri listenin en üstüne çıkar**:

| İlaç | Sıralama (2.999 molekül içinde) | Tahmin `pIC50` |
|---|---|---|
| **Repotrektinib** | **1.** | 9,40 |
| **Entrektinib** | **2.** | 9,07 |
| **Larotrektinib** | **5.** | 8,45 |
| Krizotinib | 8. | 8,19 |
| Kabozantinib | 343. | 6,98 |

İlk dördü, bu hedef için geliştirilmiş ya da ona etki ettiği bilinen
inhibitörlerdir — ve model hepsini ilk sekiz sıraya yerleştirmiştir. Bu,
oturumun **zenginleştirme (enrichment)** doğrulamasıdır.

> **Dürüstlük notu.** Bu moleküller eğitim setinde de bulunur (ChEMBL'de bu
> hedefe karşı ölçülmüşlerdir), dolayısıyla yüksek tahmin almaları kısmen
> ezberdir. Not defteri bunu `Egitimde_var` kolonuyla açıkça işaretler ve aday
> listesinden çıkarır. Yine de doğru sağlık kontrolü budur: model bilinen
> aktifleri üste taşıyamıyorsa, bilinmeyenler için ürettiği sıralamaya hiç
> güvenilemez.

### Uygulanabilirlik alanı — ölçülen davranış

| Ölçüt | Sonuç |
|---|---|
| Test setinin AD içinde kalan oranı | %82,9 |
| Kaldıraç dilimlerine göre RMSE | 0,50 (en yakın) → 0,78 (en uzak), **+%56** |
| Tanimoto dilimlerine göre RMSE | 0,54 (en benzer) → 0,90 (en benzemez) |
| Tanimoto ile \|hata\| korelasyonu | r = −0,32 |

İki ölçüt de doğru yönde çalışır; **Tanimoto benzerliği kaldıraçtan daha güçlü
bir sinyal verir** (r = −0,32'ye karşı r = 0,09). Oturum 5 bu karşılaştırmayı
veriyle yapar ve neden böyle olduğunu tartışır.

Onaylanmış ilaç kütüphanesinin **Tanimoto medyanı yalnızca 0,22**'dir: bu
kütüphane modelin eğitildiği kimyasal uzaydan belirgin biçimde uzaktır. Oturum
6 bunu açıkça gösterir ve tahminlerin neden temkinli yorumlanması gerektiğini
somutlaştırır.

> **Not.** Bu değerler bir makale sonucu değil, bir **ders alıştırmasının**
> çıktısıdır. Kursun amacı yüksek skor elde etmek değil, bir skorun ne zaman
> güvenilir olduğunu anlamaktır.

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
