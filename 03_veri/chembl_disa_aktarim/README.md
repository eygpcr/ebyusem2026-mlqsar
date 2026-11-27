# ChEMBL Web Dışa Aktarımları (çevrimdışı yedek)

Bu klasördeki dosyalar, ChEMBL'in **web arayüzünden** indirilmiş ham dışa
aktarımlardır. Amacı **ChEMBL servisi yanıt vermediğinde Oturum 1'in
eksiksiz çalışmaya devam etmesi.**

Kurs hazırlığı sırasında ChEMBL'in isteklerin yaklaşık yarısını rastgele `500`
hatasıyla reddettiği bir dönem gözlendi. Hata sorgunun biçiminden bağımsızdı:
aynı istek bir denemede başarısız olurken bir sonrakinde çalışıyordu. Bu
dosyalar o riski tamamen ortadan kaldırır.

Oturum 1'in yapılandırma hücresinde `VERI_KAYNAGI = "depo_ham"` yapmanız
yeterlidir; ChEMBL'e hiç bağlanmadan bütün temizlik hattı bu dosyalardan
çalışır.

## Dosyalar — indirmek için dosya adına tıklayın

| Dosya | Kayıt | İçerik |
|---|---|---|
| [**`ntrk1_chembl_ic50.csv.zip`**](https://raw.githubusercontent.com/eygpcr/ebyusem2026-mlqsar/main/03_veri/chembl_disa_aktarim/ntrk1_chembl_ic50.csv.zip) | 10.647 | Hedefin **bütün IC50** kayıtları (her ilişki ve birim) |
| [**`ntrk1_chembl_tum_aktiviteler.csv.zip`**](https://raw.githubusercontent.com/eygpcr/ebyusem2026-mlqsar/main/03_veri/chembl_disa_aktarim/ntrk1_chembl_tum_aktiviteler.csv.zip) | 26.746 | Hedefin **bütün biyoaktivite** kayıtları (IC50, Ki, Kd, EC50 …) |

Bağlantılar dosyayı **doğrudan indirir** (tarayıcıda açılmaz). Alternatif
olarak dosyanın GitHub sayfasını açıp sağ üstteki indirme düğmesini de
kullanabilirsiniz.

---

## Doğrulama

Bu dosyadan başlanıp Oturum 1'in temizlik hattı uygulandığında, canlı REST API
yolunun ürettiği veri setinin **birebir aynısı** elde edilir:

| Adım | Sonuç |
|---|---|
| Dışa aktarımdaki IC50 kaydı | 10.647 |
| IC50 + kesin (`=`) + `nM` süzgeci | 8.414 |
| Temizlik hattı sonrası molekül | 4.599 |
| `03_veri/ntrk1_regresyon.csv` ile aynı sayıda molekül |

Yani çevrimdışı yol bir "idare eder" çözüm değil; tam eşdeğeridir.

---

## Lisans

Veriler ChEMBL'den alınmıştır (CC BY-SA 3.0):

> Zdrazil, B., Felix, E., Hunter, F. et al. (2024). The ChEMBL Database in
> 2023. *Nucleic Acids Research*, 52(D1), D1180–D1192.
