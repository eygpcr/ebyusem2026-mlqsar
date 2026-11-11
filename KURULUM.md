# Kurs Öncesi Hazırlık

Bu belgedeki hazırlıkların **kurs gününden önce** tamamlanması gerekir.
Tamamı 15 dakikadan kısa sürer.

Kurs boyunca bilgisayarınıza **hiçbir yazılım kurmanız gerekmez**. Bütün
uygulamalar tarayıcı üzerinden, Google Colab ortamında yürütülür.

---

## 1. Zorunlu hazırlıklar

### 1.1. Google hesabı ve Colab erişimi

Bütün uygulamalar Google Colab üzerinde çalışacaktır.

- Adres: https://colab.research.google.com
- **Kurumsal (üniversite) Google hesaplarında Colab erişimi kurum politikası
  gereği kapalı olabilir.** Bu nedenle **kişisel bir Google hesabı**
  kullanmanız önerilir.
- Not defterleri çıktıları Google Drive'ınıza kaydedeceği için hesabınızda
  **en az 200 MB boş alan** bulunmalıdır.

**Doğrulama adımı.** Aşağıdakileri kurs gününden önce yapın:

1. https://colab.research.google.com adresini açın.
2. *Dosya → Yeni not defteri* ile yeni bir not defteri oluşturun.
3. Bir hücreye şunu yazıp çalıştırın (Shift+Enter):

   ```python
   print("test")
   ```

4. Ardından Drive bağlantısını da sınayın:

   ```python
   from google.colab import drive
   drive.mount("/content/drive")
   ```

   Açılan pencereden hesabınızı seçip izin verin. `Mounted at /content/drive`
   çıktısını görüyorsanız hazırsınız.

> 2. adımda izin penceresi açılmıyor ya da hata alıyorsanız, tarayıcınızın
> açılır pencere (pop-up) engelleyicisini bu site için kapatın.

### 1.2. Donanım

- Güncel bir tarayıcı (Chrome, Firefox, Edge veya Safari) çalıştırabilen
  herhangi bir dizüstü bilgisayar
- Kararlı internet bağlantısı
- **GPU gerekmez.** Kursta kullanılan modeller CPU üzerinde çalışır.

---

## 2. Önerilen hazırlıklar

### 2.1. Python'a hızlı bakış

Ön koşul değildir, ancak Python söz dizimine aşinalık oturumları daha akıcı
izlemenizi sağlar. Hiç Python görmediyseniz şu iki kavrama bakmanız yeterlidir:

- **Değişken atama ve fonksiyon çağırma:** `x = 5`, `print(x)`
- **Kütüphane içe aktarma:** `import pandas as pd`

Kısa bir başlangıç için: https://colab.research.google.com/notebooks/intro.ipynb

### 2.2. Moleküler görselleştirme yazılımı

Oturum 6'da ürettiğimiz **SDF dosyalarını** kendi bilgisayarınızda açıp
incelemek isterseniz:

- [PyMOL](https://pymol.org/) — akademik kullanım için ücretsiz sürüm mevcuttur
- [ChimeraX](https://www.cgl.ucsf.edu/chimerax/) — ücretsiz
- [Avogadro](https://avogadro.cc/) — ücretsiz, hafif

Bu kurs için zorunlu değildir; SDF dosyalarını daha sonra da inceleyebilirsiniz.

### 2.3. Kurs deposunu önceden gözden geçirmek

Bu depodaki [README.md](README.md) dosyasını ve hedef protein bölümünü kurs
öncesinde okumanız, oturumların bağlamını kurmanızı kolaylaştırır.

---

## 3. Gerekmeyen hazırlıklar

Aşağıdakilerin **hiçbirine** ihtiyacınız yoktur:

- Python, Anaconda veya herhangi bir kütüphanenin yerel kurulumu
- GitHub hesabı (depo herkese açıktır, kayıt gerekmez)
- ChEMBL hesabı (veri açık erişimlidir)
- GPU veya güçlü bir bilgisayar
- Önceden makine öğrenmesi veya QSAR deneyimi

---

## 4. Kurs günü

Her oturumda [README.md](README.md) dosyasındaki program tablosundaki
**Colab bağlantısına** tıklamanız yeterlidir. Not defteri doğrudan Colab'da
açılır.

**Önerilen çalışma biçimi.** Not defterini açtıktan sonra
*Dosya → Drive'a kopya kaydet* seçeneğini kullanın. Böylece kendi
kopyanız üzerinde çalışır, notlarınızı ve değişikliklerinizi
saklayabilirsiniz.

### Sorun giderme

| Sorun | Çözüm |
|---|---|
| Drive bağlanmıyor | Açılır pencere engelleyicisini kapatın; kişisel Google hesabı kullanın |
| ChEMBL sorgusu hata veriyor | Beklenen bir durumdur; `VERI_KAYNAGI = "depo"` yapıp devam edin (bkz. README) |
| Hücre çok uzun sürüyor | Oturum 3 ve 4'te `OPTUNA_DENEME` değerini düşürün (ör. 15) |
| "Dosya bulunamadı" hatası | Önceki oturumun not defterini **aynı Drive klasörüyle** çalıştırdığınızdan emin olun |
| Çalışma zamanı koptu | *Çalışma zamanı → Tümünü çalıştır* ile baştan çalıştırın; Drive'daki çıktılar korunur |
