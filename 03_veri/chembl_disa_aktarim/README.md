# ChEMBL Web Dışa Aktarımları (çevrimdışı yedek)

Bu klasördeki dosyalar, ChEMBL'in **web arayüzünden** indirilmiş ham dışa
aktarımlardır. Amacı tek: **ChEMBL servisi yanıt vermediğinde Oturum 1'in
eksiksiz çalışmaya devam etmesi.**

Kurs hazırlığı sırasında ChEMBL'in isteklerin yaklaşık yarısını rastgele `500`
hatasıyla reddettiği bir dönem gözlendi. Hata sorgunun biçiminden bağımsızdı:
aynı istek bir denemede başarısız olurken bir sonrakinde çalışıyordu. Bu
dosyalar o riski tamamen ortadan kaldırır.

Oturum 1'in yapılandırma hücresinde `VERI_KAYNAGI = "depo_ham"` yapmanız
yeterlidir; ChEMBL'e hiç bağlanmadan bütün temizlik hattı bu dosyalardan
çalışır.

| Dosya | Kayıt | İçerik |
|---|---|---|
| `ntrk1_chembl_ic50.csv.zip` | 10.647 | Hedefin **bütün IC50** kayıtları (her ilişki ve birim) |
| `ntrk1_chembl_tum_aktiviteler.csv.zip` | 26.746 | Hedefin **bütün biyoaktivite** kayıtları (IC50, Ki, Kd, EC50 …) |

Sıkıştırılmış hâlleri 1,4 ve 2,8 MB; açıldıklarında 15,6 ve 38,3 MB olur.
Bu yüzden depoda zip olarak tutuluyorlar — pandas zip'li CSV'yi doğrudan
okuyabilir, açmanız gerekmez.

---

## Biçim

| | |
|---|---|
| **Ayırıcı** | noktalı virgül (`;`) |
| **Kodlama** | UTF-8 |
| **Kolon sayısı** | 49 |
| **Kaynak** | https://www.ebi.ac.uk/chembl/ → hedef sayfası → Activities → Download |

Okumak için:

```python
import pandas as pd

url = ("https://raw.githubusercontent.com/eygpcr/ebyusem2026-mlqsar/main/"
       "03_veri/chembl_disa_aktarim/ntrk1_chembl_ic50.csv.zip")
df = pd.read_csv(url, sep=";", compression="zip", low_memory=False)
```

---

## Kolon adları REST API'den farklıdır

Web dışa aktarımı insan-okunur başlıklar kullanır; REST API ise alt çizgili
alan adları. Oturum 1 bu eşlemeyi otomatik yapar:

| Web dışa aktarımı | REST API |
|---|---|
| `Molecule ChEMBL ID` | `molecule_chembl_id` |
| `Smiles` | `canonical_smiles` |
| `Standard Type` | `standard_type` |
| `Standard Relation` | `standard_relation` |
| `Standard Value` | `standard_value` |
| `Standard Units` | `standard_units` |
| `Assay ChEMBL ID` | `assay_chembl_id` |
| `pChEMBL Value` | `pchembl_value` |

`Standard Relation` alanı dışa aktarımda bazen `'='` biçiminde (tırnaklı)
gelir; Oturum 1 tırnakları temizleyerek normalleştirir.

---

## Doğrulama

Bu dosyadan başlanıp Oturum 1'in temizlik hattı uygulandığında, canlı REST API
yolunun ürettiği veri setinin **birebir aynısı** elde edilir:

| Adım | Sonuç |
|---|---|
| Dışa aktarımdaki IC50 kaydı | 10.647 |
| IC50 + kesin (`=`) + `nM` süzgeci | 8.414 |
| Temizlik hattı sonrası molekül | 4.599 |
| `03_veri/ntrk1_regresyon.csv` ile karşılaştırma | aynı 4.599 molekül, en büyük `pIC50` farkı **0,00000000** |

Yani çevrimdışı yol bir "idare eder" çözüm değil; tam eşdeğeridir.

---

## Lisans

Veriler ChEMBL'den alınmıştır (CC BY-SA 3.0):

> Zdrazil, B., Felix, E., Hunter, F. et al. (2024). The ChEMBL Database in
> 2023. *Nucleic Acids Research*, 52(D1), D1180–D1192.
