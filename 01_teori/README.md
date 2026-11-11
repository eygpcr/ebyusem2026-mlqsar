# Teorik Oturumlar

Kursta üç teorik oturum vardır. Her biri, ardından gelen uygulamalı oturumun
kavramsal zeminini kurar. Bu dosya oturumların içerik planını verir; sunum
dosyaları ders sırasında paylaşılacaktır.

| Oturum | Süre | Gün | Hazırladığı uygulama |
|---|---|---|---|
| [Teori 1](#teori-1--ilaç-keşif-süreci-ve-bilgisayar-destekli-tasarım) | 45 dk | 1. gün 09:30 | Oturum 1 |
| [Teori 2](#teori-2--qsar-ve-makine-öğrenmesinin-temelleri) | 45 dk | 1. gün 10:30 | Oturum 1–4 |
| [Teori 3](#teori-3--moleküler-temsil-açıklanabilirlik-ve-uygulanabilirlik-alanı) | 45 dk | 2. gün 09:30 | Oturum 5–6 |

---

## Teori 1 — İlaç keşif süreci ve bilgisayar destekli tasarım

### 1.1. İlaç keşfinin ölçeği ve darboğazı

- Bir ilacın pazara ulaşması: ortalama 10–15 yıl, milyar dolar mertebesinde
  maliyet
- Klinik aşamalarda başarısızlık oranları; neden "erken ve ucuz başarısızlık"
  bir hedeftir
- Kimyasal uzayın büyüklüğü: ilaç benzeri moleküllerin sayısı 10⁶⁰
  mertebesinde tahmin edilir — hiçbir deneysel yaklaşım bunu tarayamaz
- **Sonuç:** süzme (filtreleme) kaçınılmazdır; soru, süzmenin neye dayandığıdır

### 1.2. Hedef temelli ilaç tasarımı

- Hedef seçimi ve doğrulanması (target validation)
- Hit → lead → optimizasyon → aday zinciri
- Yapı-aktivite ilişkisi (SAR) kavramının doğuşu
- **Örnek olay: NTRK1.** Gen füzyonundan tümör-agnostik onaya; larotrektinib
  ve entrektinibin öyküsü; direnç mutasyonları ve ikinci nesil inhibitörler

### 1.3. Bilgisayar destekli ilaç tasarımının iki kolu

| | **Liganda dayalı** (ligand-based) | **Yapıya dayalı** (structure-based) |
|---|---|---|
| Ne gerekir? | Aktiviteleri bilinen moleküller | Proteinin 3B yapısı |
| Yöntemler | QSAR, farmakofor, benzerlik araması | Doklama, serbest enerji hesapları |
| Güçlü yanı | Yapı bilinmesine gerek yok; hızlı | Bağlanma modunu açıklar |
| Zayıf yanı | Yalnızca bilinen kimyaya yakın bölgede güvenilir | Yapı gerektirir; hesaplama pahalı |

**Bu kurs liganda dayalı yaklaşımı ele alır.** Oturum 6'da ürettiğimiz SDF
dosyaları, yapıya dayalı adıma (doklama) köprü kurar.

### 1.4. Verinin kaynağı: ChEMBL

- Biyoaktivite veri tabanlarının yapısı: hedef, tayin (assay), aktivite
- `standard_type` (IC50, Ki, Kd, EC50) ne anlatır, neden karıştırılmamalıdır
- `standard_relation` ve sansürlü (censored) veri sorunu
- Veri kalitesi: birim tutarsızlıkları, tekrarlı ölçümler, giriş hataları
- **Vurgulanacak nokta:** ChEMBL sürekli güncellenir; tekrarlanabilirlik için
  sürüm ve tarih bildirmek zorunludur

> **Uygulamaya geçiş.** Oturum 1'de bu kavramların her birini kodda
> göreceğiz: aktivite tiplerini sayacak, sansürlü veriyi süzecek, birim
> tutarlılığı sağlayacak ve gerçek bir giriş hatası yakalayacağız.

---

## Teori 2 — QSAR ve makine öğrenmesinin temelleri

### 2.1. QSAR nedir?

- Temel varsayım: **benzer yapılar benzer etki gösterir**
- Hansch ve Fujita'dan günümüze kısa tarihçe: lineer serbest enerji
  ilişkilerinden makine öğrenmesine
- QSAR'ın matematiksel biçimi: `aktivite = f(yapı)` — `f`'i veriden öğrenmek
- **Benzerlik varsayımının sınırları:** aktiflik uçurumları (activity cliffs) —
  neredeyse aynı iki molekülün aktivitesi 100 kat farklı olabilir

### 2.2. Hedef değişken: neden pIC50?

- IC50'den pIC50'ye logaritmik dönüşüm
- İki kazanç: yönün sezgiselleşmesi ve dağılımın simetrikleşmesi
- Yorum tablosu: pIC50 = 9 → 1 nM; 7 → 100 nM; 5 → 10 µM

### 2.3. Makine öğrenmesinin iki temel görevi

| | **Regresyon** | **Sınıflandırma** |
|---|---|---|
| Çıktı | Sürekli sayı (pIC50 = 7,8) | Sınıf + olasılık (aktif, 0,86) |
| QSAR'daki yeri | Potensi sıralamak, optimizasyon yönü | Büyük kütüphaneleri elemek |
| Metrikler | R², RMSE, MAE | Doğruluk, MCC, ROC-AUC, PR-AUC |

### 2.4. Aşırı öğrenme ve genelleme

- Ezberleme ile öğrenme arasındaki fark
- Yanlılık-varyans dengesi (bias–variance tradeoff), sezgisel anlatım
- **Eğitim/doğrulama/test ayrımı:** her birinin işi nedir, neden üçü gerekir
- **Çapraz doğrulama:** K-katlı CV nasıl çalışır, Q² ne söyler
- **Hiperparametre nedir?** Modelin öğrenmediği, bizim seçtiğimiz ayarlar

### 2.5. Veri sızıntısı — kursun en çok vurgulanan kavramı

Dört yaygın sızıntı biçimi ve her birinin çözümü:

| Sızıntı | Nasıl olur? | Çözüm |
|---|---|---|
| **Yapısal tekrar** | Aynı molekül farklı SMILES ile iki satırda; biri eğitimde biri testte | Kanonikleştirme (Oturum 1) |
| **Global ölçekleme** | `StandardScaler` bütün veriye uydurulur; test dağılımı eğitime sızar | `Pipeline` içinde ölçekleme (Oturum 2–3) |
| **Test setinin erken kullanımı** | Model seçimi test skoruna göre yapılır | Ayrı doğrulama seti (Oturum 3) |
| **Seri sızıntısı** | Aynı kimyasal serinin türevleri hem eğitimde hem testte | İskelet bazlı bölünme (Oturum 3) |

### 2.6. Model aileleri: sezgisel tanıtım

- **Lineer modeller** (Ridge, Lasso): yorumlanabilir, hızlı, ilişki doğrusal
  değilse zayıf
- **Komşuluk (kNN):** "en benzer moleküllere bak" — QSAR'ın temel varsayımının
  en doğrudan hâli
- **Destek vektör makineleri:** çekirdek hilesi ile doğrusal olmayan ilişkiler
- **Karar ağaçları ve toplulukları** (Random Forest, Extra Trees): eşikli
  kurallar, ölçeklemeye duyarsız
- **Gradyan artırma** (XGBoost): hataları sırayla düzeltmek; tablo verisinde
  genellikle en güçlü aile
- **Neden derin öğrenme kullanmıyoruz?** Birkaç bin molekülle, tablo
  biçiminde veri için ağaç toplulukları genellikle daha iyi ve çok daha hızlı
  sonuç verir. Derin öğrenme (GNN, MPNN) on binlerce molekülde ve ham
  grafik temsilinde öne çıkar.

### 2.7. Modelin öğrendiğini nasıl kanıtlarız?

- **y-randomizasyon (y-scrambling):** hedefi karıştır, yeniden eğit; iyi skor
  alıyorsa model gürültü öğrenmiş
- Şans korelasyonu: özellik sayısı molekül sayısına yaklaştığında kaçınılmaz
- **Temel çizgi (baseline) bildirmek:** "her şeye çoğunluk sınıfını söyle"
  modelinin doğruluğu aşılmalıdır

> **Uygulamaya geçiş.** Oturum 3 ve 4 bu protokolü adım adım kuracak:
> bölünme → tarama (LazyPredict) → optimizasyon (Optuna) → çapraz doğrulama
> → tek seferlik test → y-randomizasyon.

---

## Teori 3 — Moleküler temsil, açıklanabilirlik ve uygulanabilirlik alanı

### 3.1. Molekülü sayıya çevirmek

Temsil seçimi, QSAR'da model seçiminden daha belirleyici olabilir.

**Moleküler betimleyiciler (descriptors)**

- Aileler: kurucu, topolojik, fizikokimyasal, elektronik, fragman sayımları
- Örnekler ve kimyasal anlamları: `MolWt`, `MolLogP`, `TPSA`,
  `NumRotatableBonds`
- **Lipinski'nin Beşler Kuralı:** ne söyler, ne söylemez; kinaz
  inhibitörlerinin kuralı sıklıkla ihlal etmesi
- Çoklu-doğrusallık sorunu: birçok betimleyici aynı şeyi iki kez ölçer

**Moleküler parmak izleri (fingerprints)**

- Alt-yapı kodlaması mantığı
- **Morgan/ECFP:** yarıçap kavramı, hash işlemi, bit çakışması
  (ECFP4 = yarıçap 2)
- **MACCS anahtarları:** 167 elle tanımlanmış, anlamı bilinen yapısal soru
- Seyreklik (sparsity) ve sonuçları

**Tanimoto benzerliği**

- İki parmak izi arasındaki örtüşme: 1 = aynı, 0 = ilgisiz
- Kemoinformatikte eşik sezgileri ve bunların bağlama göre değişmesi

### 3.2. Açıklanabilir yapay zekâ (XAI)

- **Neden gerekli?** Medisinal kimyacı "hangi özellik yüzünden" diye sorar;
  açıklanamayan model karar vermekte kullanılamaz
- Özellik önemi yaklaşımları ve sınırları (ağaç önemi, permütasyon önemi)
- **SHAP:** Shapley değerlerinin oyun teorisinden gelişi
- **Toplamsallık özelliği:** `tahmin = ortalama + Σ katkılar` — SHAP'ı özel
  kılan nitelik
- İki okuma düzeyi: küresel (hangi özellikler önemli) ve yerel (bu molekül
  neden potent)
- **Üç uyarı:**
  1. SHAP nedensellik değildir — modelin ne gördüğünü söyler, doğanın ne
     yaptığını söylemez
  2. Korelasyonlu özellikler katkıyı paylaşır ve önem bölünür
  3. Model yanlış bir örüntü öğrenmişse SHAP onu sadakatle gösterir

### 3.3. Uygulanabilirlik alanı (Applicability Domain)

- **Temel ilke:** bir model yalnızca eğitildiği kimyasal uzayda güvenilirdir;
  dışında ürettiği sayı bir tahmin değil, **ekstrapolasyondur**
- **OECD QSAR doğrulama ilkeleri** — AD tanımı zorunlu bir maddedir
  (beş ilkenin üçüncüsü)

**Yöntem 1: kaldıraç (leverage) ve Williams grafiği**

- `h = xᵀ(XᵀX)⁻¹x` — özellik uzayında merkeze uzaklık
- Kritik kaldıraç `h* = 3(p+1)/n`
- Standartlaştırılmış artıklar ve ±3σ sınırı
- Williams grafiğinin dört bölgesi: AD içi, kaldıraç aykırısı, yanıt
  aykırısı, her ikisi
- **Sınırı:** `h*` formülü özellik sayısına duyarlıdır

**Yöntem 2: benzerlik tabanlı AD**

- Eğitim setine en yüksek Tanimoto benzerliği
- Kaldıraca göre iki avantajı: yorumlanabilirlik ve özellik sayısından
  bağımsızlık

**AD'yi sınamak**

- Asıl soru: AD içindeki moleküller gerçekten daha iyi tahmin ediliyor mu?
- Sınanmamış bir AD ölçütü işe yaramıyor olabilir

### 3.4. Sanal tarama ve sonuçların yorumu

- Elek mantığı: sınıflandırıcı eler, regresyon sıralar, AD güven verir
- **İlaç yeniden konumlandırma** (drug repurposing) yaklaşımı ve çekiciliği
- **Zenginleştirme (enrichment) kavramı:** bilinen aktifler üst sıralara
  çıkıyor mu? Oturum 6'da larotrektinib ve entrektinib ile doğrudan ölçeceğiz
- **Tahmin ölçüm değildir.** Modelin söylemediği şeyler: ADME, toksisite,
  seçicilik, *in vivo* etki
- **Aktif öğrenme:** model deneyi yönlendirir, deney modeli iyileştirir —
  döngüyü kapatmak

> **Uygulamaya geçiş.** Oturum 5 SHAP ve Williams grafiğini kuracak; Oturum 6
> bu sınırları kullanarak 3.311 onaylanmış ilacı tarayacak ve sonuçları SDF
> dosyaları olarak üretecek.

---

## Kaynaklar

Her oturumun dayandığı okuma listesi [ILERI_OKUMA.md](../ILERI_OKUMA.md)
dosyasındadır. Teorik oturumlarda özellikle şu kaynaklara atıf yapılmaktadır:

- Cherkasov, A. et al. (2014). *QSAR Modeling: Where Have You Been? Where Are
  You Going To?* J. Med. Chem., 57(12), 4977–5010.
- Tropsha, A. (2010). *Best Practices for QSAR Model Development, Validation,
  and Exploitation.* Mol. Inf., 29(6–7), 476–488.
- Sheridan, R. P. (2013). *Time-Split Cross-Validation.* JCIM, 53(4), 783–790.
- Lundberg, S. M. & Lee, S.-I. (2017). *A Unified Approach to Interpreting
  Model Predictions.* NeurIPS 30.
- Sahigara, F. et al. (2012). *Comparison of Different Approaches to Define
  the Applicability Domain of QSAR Models.* Molecules, 17(5), 4791–4810.
- Cocco, E., Scaltriti, M. & Drilon, A. (2018). *NTRK fusion-positive cancers
  and TRK inhibitor therapy.* Nat. Rev. Clin. Oncol., 15, 731–747.
