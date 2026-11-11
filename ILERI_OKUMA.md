# İleri Okuma ve Devam Yolları

Kurs sonrası çalışmak isteyenler için kaynaklar.

---

## 1. ML-QSAR: temel ve yöntem

### Kitaplar ve genel derlemeler

- **Cherkasov, A. et al. (2014).** *QSAR Modeling: Where Have You Been? Where
  Are You Going To?* Journal of Medicinal Chemistry, 57(12), 4977–5010.
  Alanın geniş ve eleştirel bir değerlendirmesi; kursta vurguladığımız
  değerlendirme sorunlarını ayrıntılı tartışır.
- **Tropsha, A. (2010).** *Best Practices for QSAR Model Development,
  Validation, and Exploitation.* Molecular Informatics, 29(6–7), 476–488.
  y-randomizasyon, uygulanabilirlik alanı ve dış doğrulama konularında
  referans metin.
- **Muratov, E. N. et al. (2020).** *QSAR without borders.* Chemical Society
  Reviews, 49, 3525–3564.

### Değerlendirme ve yaygın hatalar

- **Sheridan, R. P. (2013).** *Time-Split Cross-Validation as a Method for
  Estimating the Goodness of Prospective Prediction.* Journal of Chemical
  Information and Modeling, 53(4), 783–790.
  Rastgele bölünmenin neden iyimser olduğunu gösteren klasik çalışma.
- **Wallach, I. & Heifets, A. (2018).** *Most Ligand-Based Classification
  Benchmarks Reward Memorization Rather than Generalization.* JCIM, 58(5),
  916–932. Kursta iskelet bazlı bölünmeyi neden önemsediğimizin gerekçesi.
- **Walters, W. P. (2021).** *Comparability of mixed IC50 data.* Pat Walters'ın
  [Practical Cheminformatics](https://practicalcheminformatics.blogspot.com/)
  bloğu, bu alanda en yararlı pratik kaynaklardan biridir.

### Uygulanabilirlik alanı

- **Sahigara, F. et al. (2012).** *Comparison of Different Approaches to Define
  the Applicability Domain of QSAR Models.* Molecules, 17(5), 4791–4810.
- **OECD (2007).** *Guidance Document on the Validation of (Q)SAR Models.*
  Beş OECD ilkesi; AD tanımı üçüncü ilkedir.

### Açıklanabilir yapay zekâ

- **Lundberg, S. M. & Lee, S.-I. (2017).** *A Unified Approach to Interpreting
  Model Predictions.* NeurIPS 30. SHAP'ın özgün makalesi.
- **Jiménez-Luna, J., Grisoni, F. & Schneider, G. (2020).** *Drug discovery
  with explainable artificial intelligence.* Nature Machine Intelligence, 2,
  573–584.

---

## 2. Hedefimiz: NTRK ve tümör-agnostik onaylar

- **Cocco, E., Scaltriti, M. & Drilon, A. (2018).** *NTRK fusion-positive
  cancers and TRK inhibitor therapy.* Nature Reviews Clinical Oncology, 15,
  731–747.
- **Drilon, A. et al. (2018).** *Efficacy of Larotrectinib in TRK
  Fusion–Positive Cancers in Adults and Children.* New England Journal of
  Medicine, 378, 731–739.
- **Drilon, A. et al. (2017).** *What hides behind the MASC: clinical response
  and acquired resistance to entrectinib.* Annals of Oncology, 28(7),
  1527–1534. Direnç mutasyonlarının ortaya çıkışı.

---

## 3. Araçlar ve belgelendirme

| Araç | Belgelendirme | Not |
|---|---|---|
| **RDKit** | https://www.rdkit.org/docs/ | [RDKit Cookbook](https://www.rdkit.org/docs/Cookbook.html) pratik örnekler için çok yararlıdır |
| **scikit-learn** | https://scikit-learn.org/stable/user_guide.html | Özellikle *Model selection and evaluation* bölümü |
| **Optuna** | https://optuna.readthedocs.io/ | Pruning (erken durdurma) ile aramayı hızlandırma |
| **SHAP** | https://shap.readthedocs.io/ | |
| **XGBoost** | https://xgboost.readthedocs.io/ | Parametre ayarlama kılavuzu |
| **ChEMBL web servisi** | https://www.ebi.ac.uk/chembl/api/data/docs | |

### Kursta kullanmadığımız ama bilmeye değer araçlar

- **[DeepChem](https://deepchem.io/)** — moleküler makine öğrenmesi için
  derin öğrenme kütüphanesi; grafik sinir ağları (GNN) ile çalışmak isteyenler
  için başlangıç noktası.
- **[chemprop](https://github.com/chemprop/chemprop)** — mesaj geçiren sinir
  ağları (MPNN); moleküler özellik tahmininde güçlü sonuçlar verir.
- **[Mordred](https://github.com/mordred-descriptor/mordred)** — 1800'den
  fazla moleküler betimleyici (RDKit'in sunduğundan çok daha fazla).
- **[Datamol](https://docs.datamol.io/)** — RDKit üzerine kurulu, daha
  kullanıcı dostu bir arayüz.
- **[PapyrusScripts](https://github.com/OlivierBeq/Papyrus-scripts)** —
  standartlaştırılmış, büyük ölçekli biyoaktivite veri seti.

---

## 4. Veri kaynakları

| Kaynak | İçerik |
|---|---|
| [ChEMBL](https://www.ebi.ac.uk/chembl/) | Biyoaktivite verisi; kursta kullandığımız kaynak |
| [PubChem](https://pubchem.ncbi.nlm.nih.gov/) | Çok daha büyük ama daha heterojen |
| [BindingDB](https://www.bindingdb.org/) | Bağlanma afinitesine odaklı |
| [Papyrus](https://doi.org/10.1186/s13321-022-00672-x) | Standartlaştırılmış, modellemeye hazır |
| [MoleculeNet](https://moleculenet.org/) | Karşılaştırma (benchmark) veri setleri |
| [DUD-E](http://dude.docking.org/) | Sanal tarama değerlendirmesi için tuzak (decoy) setleri |
| [PDB](https://www.rcsb.org/) | Protein yapıları; doklamaya geçmek isterseniz |

---

## 5. Bir sonraki adım: yapıya dayalı tasarım

Bu kurs **liganda dayalı** (ligand-based) yaklaşımı ele aldı: yalnızca
moleküllerin yapısından ve ölçülmüş aktivitelerinden yararlandık. Tamamlayıcı
yaklaşım **yapıya dayalıdır** (structure-based): proteinin üç boyutlu yapısını
kullanır.

Oturum 6'da ürettiğimiz SDF dosyaları doğrudan bu adıma girdidir:

1. **Moleküler doklama** — [AutoDock Vina](https://vina.scripps.edu/),
   [smina](https://sourceforge.net/projects/smina/) veya
   [DiffDock](https://github.com/gcorso/DiffDock)
2. **Bağlanma modunun incelenmesi** — PyMOL, ChimeraX
3. **Moleküler dinamik** — [GROMACS](https://www.gromacs.org/),
   [OpenMM](https://openmm.org/)
4. **Serbest enerji hesapları** — MM/PBSA, FEP

NTRK1'in deneysel yapıları PDB'de mevcuttur (ör. `4AOJ`, `6D20`); larotrektinib
ve seçici inhibitörlerle kompleks yapılar da bulunur.

---

## 6. Aktif öğrenme: döngüyü kapatmak

Kursun Oturum 6'sında vurguladığımız nokta burada genişletilebilir. Modern
ilaç keşfinde model ve deney bir **döngü** oluşturur:

```
model tahmini  ──►  deneysel test  ──►  yeni veri  ──►  modeli yeniden egit
      ▲                                                          │
      └──────────────────────────────────────────────────────────┘
```

Bu yaklaşıma **aktif öğrenme** (active learning) denir ve hangi molekülleri
test edeceğinize karar vermenin sistematik yoludur.

- **Reker, D. & Schneider, G. (2015).** *Active-learning strategies in
  computer-assisted drug discovery.* Drug Discovery Today, 20(4), 458–465.
- **Graff, D. E., Shakhnovich, E. I. & Coley, C. W. (2021).** *Accelerating
  high-throughput virtual screening through molecular pool-based active
  learning.* Chemical Science, 12, 7866–7881.

---

## 7. Topluluk ve süregelen kaynaklar

- **[Practical Cheminformatics](https://practicalcheminformatics.blogspot.com/)**
  (Pat Walters) — alandaki en yararlı blog; yöntem eleştirileri ve kod
  örnekleriyle birlikte.
- **[RDKit blog](https://greglandrum.github.io/rdkit-blog/)** (Greg Landrum) —
  RDKit'in geliştiricisinden ayrıntılı teknik yazılar.
- **[TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/)** —
  bilgisayar destekli ilaç tasarımı için açık ders materyali; bu kursun
  yaklaşımına en yakın kapsamlı kaynaklardan biridir.
- **[Cheminformania](https://www.cheminformania.com/)** — uygulamalı
  öğreticiler.
