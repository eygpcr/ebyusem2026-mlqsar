# Google Colab Not Defterleri

Aşağıdaki bağlantılar not defterlerini doğrudan Google Colab'da açar.
Bilgisayarınıza yazılım kurmanız gerekmez.

| Oturum | Dosya | Konu | Colab |
|---|---|---|---|
| 1 | `01_veri_hazirlama.ipynb` | ChEMBL'den veri çekme, temizlik, pIC50 | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/01_veri_hazirlama.ipynb) |
| 2 | `02_ozellik_uretimi.ipynb` | Betimleyiciler, ECFP4, MACCS | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/02_ozellik_uretimi.ipynb) |
| 3 | `03_regresyon_modelleri.ipynb` | LazyPredict, Optuna, CV, y-randomizasyon | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/03_regresyon_modelleri.ipynb) |
| 4 | `04_siniflandirma_modelleri.ipynb` | Dengesizlik, ROC/PR, MCC, karar eşiği | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/04_siniflandirma_modelleri.ipynb) |
| 5 | `05_karsilastirma_shap_ad.ipynb` | Model karşılaştırma, SHAP, Williams grafiği | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/05_karsilastirma_shap_ad.ipynb) |
| 6 | `06_tahmin_ve_sdf.ipynb` | Sanal tarama, uygulanabilirlik alanı, SDF çıktısı | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/eygpcr/ebyusem2026-mlqsar/blob/main/02_notebooks/06_tahmin_ve_sdf.ipynb) |

---

## Kullanım notları

### Not defterleri sırayla çalıştırılır

Her oturumun çıktısı bir sonrakinin girdisidir:

```
01 → ntrk1_regresyon.csv, ntrk1_siniflandirma.csv
      ↓
02 → ntrk1_descriptors.csv, ntrk1_ecfp4.csv, ntrk1_maccs.csv
      ↓
03 → en iyi regresyon modeli + eğitim/test bölünmesi
      ↓
04 → en iyi sınıflandırma modeli (03'ün bölünmesini kullanır)
      ↓
05 → SHAP grafikleri + uygulanabilirlik alanı parametreleri
      ↓
06 → aday listesi + SDF dosyaları
```

Bir oturumu kaçırırsanız, not defterleri depodaki **hazır veri
dosyalarına** düşerek çalışmaya devam eder (Oturum 1 ve 2 için). Oturum 3–6
ise önceki oturumun Drive çıktısına ihtiyaç duyar ve bulamazsa hangi
not defterini çalıştırmanız gerektiğini açıkça söyler.

### Çıktılar Google Drive'a kaydedilir

Her not defterinin ikinci hücresi Drive'ı bağlar ve
`Drive'ım/EBYUSEM2026_MLQSAR/` klasörünü oluşturur. **Bütün oturumlar bu aynı
klasörü paylaşır** — `DRIVE_PROJE_KLASORU` ayarını değiştirmeyin.

Colab çalışma zamanı sonlanırsa `/content/` altındaki her şey silinir, ama
Drive'daki çıktılar korunur.

### Kendi kopyanız üzerinde çalışın

Not defterini açtıktan sonra *Dosya → Drive'a kopya kaydet* seçeneğini
kullanın. Böylece notlarınızı ve değişikliklerinizi saklayabilirsiniz.

### Yapılandırma tek hücrede toplanmıştır

Her not defterinin birinci kod hücresi bütün ayarları içerir. Başka bir hedef
proteinle çalışmak isterseniz Oturum 1'deki `TARGET_CHEMBL_ID` değerini
değiştirip bütün defterleri sırayla çalıştırmanız yeterlidir — kod hedefe
özel hiçbir varsayım yapmaz.

### Süre beklentileri

| Not defteri | Yaklaşık süre | Notlar |
|---|---|---|
| 01 | 3–8 dk | Canlı ChEMBL indirmesi yavaş olabilir |
| 02 | 1–3 dk | Betimleyici hesabı ~1 dk |
| 03 | 15–25 dk | En uzun oturum; `OPTUNA_DENEME` ile ayarlanabilir |
| 04 | 10–20 dk | |
| 05 | 5–10 dk | SHAP hesabı `SHAP_ORNEK` ile ayarlanabilir |
| 06 | 5–12 dk | 3B koordinat üretimi en yavaş adım |

Süreler Colab'ın ücretsiz CPU çalışma zamanı içindir. Ders akışı sıkışırsa
Oturum 3 ve 4'te `OPTUNA_DENEME = 10` ve `Y_RANDOM_TEKRAR = 5` yapmak toplam
süreyi yarıdan aza indirir; kavramlar aynı kalır.

### ChEMBL yanıt vermezse

Oturum 1'in yapılandırma hücresinde `VERI_KAYNAGI = "depo_ham"` yapın.
ChEMBL'e hiç bağlanmadan, depodaki ham dışa aktarımdan bütün temizlik hattı
çalışır ve canlı sorgunun ürettiği veri setinin birebir aynısı elde edilir.

### GPU gerekmez

Kullanılan modeller (ağaç toplulukları, SVM, gradyan artırma) CPU üzerinde
çalışır. *Çalışma zamanı → Çalışma zamanı türünü değiştir* ayarına
dokunmanız gerekmez.
