# Araçlar

Bu klasör, kurs materyalinin üretiminde kullanılan betiği içerir. Katılımcıların
kurs sırasında bu klasörü kullanması **gerekmez** — not defterleri hazır veri
dosyalarını doğrudan okur.

---

## `veri_uret.py`

[`veri/`](../veri/) klasöründeki referans veri setlerini ChEMBL web
servisinden üretir. Oturum 1'deki "canlı ChEMBL çekimi" ile **aynı temizlik
mantığını** uygular; böylece katılımcılar iki yolu karşılaştırabilir.

### Kullanım

```bash
python veri_uret.py --cikti ../veri --esik 7.0
```

| Seçenek | Açıklama |
|---|---|
| `--cikti` | Çıktı klasörü (varsayılan `../veri`) |
| `--esik` | Sınıflandırma eşiği, pIC50 (varsayılan 7.0) |
| `--ham-kullan` | Diskteki ham CSV'yi kullan, yeniden indirme |
| `--tarama-atla` | Onaylanmış ilaç kütüphanesini indirmeyi atla |

### Gereksinimler

```bash
pip install pandas rdkit
```

### Başka bir hedefle kullanmak

Betiğin başındaki sabitleri değiştirmek yeterlidir:

```python
TARGET_CHEMBL_ID = "CHEMBL2815"   # NTRK1
ACTIVITY_TYPE    = "IC50"
VARSAYILAN_ESIK  = 7.0
MANTIK_ARALIGI   = (3.0, 12.0)
SLUG             = "ntrk1"        # dosya adlarında kullanılır
```

Ardından not defterlerindeki `TARGET_CHEMBL_ID` ve dosya adlarını da
güncellemeniz gerekir.

### ChEMBL servisinin kararsızlığı

Betik, isteklerin rastgele `500` hatası vermesine karşı **20 denemeye kadar
artan beklemeli yeniden deneme** uygular. Tarama kütüphanesi indirilirken bir
sayfa alınamazsa işlem iptal edilmez: o sayfa atlanır ve sonunda kaç sayfanın
eksik kaldığı bildirilir. Kısmi bir kütüphane, hiç kütüphane olmamasından
iyidir.

Ana veri setinde ise bu tolerans **uygulanmaz**: bir sayfanın eksik kalması
eğitim verisini sessizce yanlı hâle getireceği için betik hata vererek durur.
