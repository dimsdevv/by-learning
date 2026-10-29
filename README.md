# 🧠 Machine Learning & Data Science Journey (BY LEARNING)

Repository ini mendokumentasikan proses belajar terstruktur dari konsep dasar Machine Learning, pemahaman filosofis & etika data, hingga implementasi koding eksplorasi data (*Exploratory Data Analysis*) dan visualisasi data tingkat lanjut menggunakan Python.

---

## 🎨 Showcase: Dashboard Eksekutif Tragedi Kapal Titanic

Berikut adalah hasil eksplorasi data keselamatan penumpang kapal Titanic (14 April 1912) yang divisualisasikan dalam bentuk **Dark-Theme Bento Grid** presisi tinggi:

![Dashboard Titanic](PYTHON-LEARNING/HARI-KE1/dashboard_titanic.png)

---

## 📚 Struktur Pembelajaran

### 1. Fondasi Machine Learning
* **[Modul 1: Pengenalan Machine Learning](MODUL1-PENGENALAN-MACHINE-LEARNING.md)**: Intuisi dasar, perbedaan pemrograman tradisional vs Machine Learning, dan taksonomi pembelajaran mesin.
* **[Modul 1 (Pelajaran 2): Sejarah Machine Learning](MODUL1-PELAJARAN-02-SEJARAH-MACHINE-LEARNING.md)**: Dari era Alan Turing, masa keemasan, AI Winter, hingga ledakan Big Data & Deep Learning.
* **[Modul 1 (Pelajaran 3): Etika & Bias dalam AI](MODUL1-PELAJARAN-03-ETIKA-DAN-BIAS-DALAM-AI.md)**: Kasus bias algoritma peminjaman modal, keadilan data, dan prinsip akuntabilitas model.
* **[Modul 1 (Pelajaran 4): Persiapan Lingkungan Koding](MODUL1-PELAJARAN-04-DAN-PERSIAPAN-KODING.md)**: Setup Python, VS Code, virtual environment, dan library utama data science.

### 2. Algoritma Machine Learning (Regresi)
* **[Modul 2 (Pelajaran 1): Praktik Regresi Linier](MODUL2-PELAJARAN-01-PRAKTIK-REGRESI-LINIER.md)**: Mengolah data panen labu (*US Pumpkins*), eksplorasi korelasi, dan melatih model regresi linier pertama.
* **Script Koding**: [`latihan_regresi_labu.py`](latihan_regresi_labu.py) & grafik output [`grafik_prediksi_labu.png`](grafik_prediksi_labu.png).

### 3. Eksplorasi Data & Data Storytelling (Titanic Case Study)
Terletak di dalam folder `PYTHON-LEARNING/HARI-KE1/`:
* **Panduan Materi**:
  * [`PANDUAN-10-DATASET-DAN-ROADMAP-PYTHON-PEMULA.md`](PYTHON-LEARNING/HARI-KE1/PANDUAN-10-DATASET-DAN-ROADMAP-PYTHON-PEMULA.md): Rekomendasi 10 dataset dunia nyata untuk pemula.
  * [`PANDUAN-BELAJAR-DATA-TITANIC.md`](PYTHON-LEARNING/HARI-KE1/PANDUAN-BELAJAR-DATA-TITANIC.md): Panduan cerita data dan logika investigasi Titanic.
  * [`PANDUAN-LANGKAH4-VISUALISASI.md`](PYTHON-LEARNING/HARI-KE1/PANDUAN-LANGKAH4-VISUALISASI.md): Bedah data storytelling & desain aesthetic dark mode.
* **Script Python**:
  * [`step1_titanic.py`](PYTHON-LEARNING/HARI-KE1/step1_titanic.py): Membaca dan memeriksa ringkasan data penumpang.
  * [`step2_titanic.py`](PYTHON-LEARNING/HARI-KE1/step2_titanic.py): Analisis tingkat keselamatan berdasarkan jenis kelamin (Gender).
  * [`step3_titanic.py`](PYTHON-LEARNING/HARI-KE1/step3_titanic.py): Analisis pengaruh kelas tiket (Kasta sosial).
  * [`visualisasi_titanic.py`](PYTHON-LEARNING/HARI-KE1/visualisasi_titanic.py): Script penghasil dashboard 6 panel resolusi tinggi.

---

## 🚀 Cara Menjalankan Kode Secara Lokal

### 1. Kloning Repository
```bash
git clone https://github.com/dimsdevv/by-learning.git
cd by-learning
```

### 2. Buat & Aktifkan Virtual Environment (Opsional namun Disarankan)
```bash
python -m venv .venv
# Di Windows:
.venv\Scripts\activate
# Di Mac/Linux:
source .venv/bin/activate
```

### 3. Pasang Dependensi
```bash
pip install pandas matplotlib seaborn scikit-learn numpy
```

### 4. Jalankan Visualisasi Titanic
```bash
cd "PYTHON-LEARNING/HARI-KE1"
python visualisasi_titanic.py
```
Grafik akan tersimpan otomatis sebagai `dashboard_titanic.png`.

---

Dikelola dan dipelajari oleh **Dimas Sholihul Hadi** (@dimsdevv)
