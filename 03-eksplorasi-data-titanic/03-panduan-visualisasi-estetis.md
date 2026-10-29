# PANDUAN LANGKAH 4: DATA STORYTELLING & VISUALISASI PRESISI TINGGI TITANIC

Selamat datang kembali! Pada versi terbaru ini, kita telah menyempurnakan visualisasi data menjadi **Dashboard Eksekutif Presisi Tinggi (High-Precision Bento Grid)**. 🎨🚢

---

## 1. Perbaikan Presisi & Tata Letak (Layout Engineering)

Masalah umum yang sering terjadi saat membuat visualisasi multi-panel adalah **elemen bertabrakan, margin sesak, atau teks terpotong**. Pada versi penyempurnaan ini:

1. **Eliminasi Tabrakan Garis & Judul**:
   - Garis pembatas yang sebelumnya memotong judul grafik telah disesuaikan dengan `GridSpec(top=0.84)`.
   - Memberikan ruang bernapas (*breathing room*) vertikal sebesar 16% di area header.
2. **Headroom Vertikal & Penempatan Legend**:
   - Pada panel Distribusi Usia (Panel 4) dan Interaksi Gender (Panel 5), batas atas sumbu-Y diperluas secara proporsional. Hasilnya: kotak *legend* melayang bebas di sudut kanan atas tanpa menutupi puncak batang data (*bars*).
3. **Penyempurnaan Panel 6 (Daya Beli / Tarif Tiket)**:
   - Boxplot sebelumnya membuat kotak data terjepit di dasar grafik akibat pencilan ekstrem (£512).
   - Kami menggantinya dengan **Bar Chart Rata-rata Tarif (£) + Median**, menyajikan perbandingan daya beli yang jauh lebih informatif, presisi, dan mudah dibaca audiens.

---

## 2. Bedah 6 Panel Visualisasi Presisi Tinggi

File visualisasi tersimpan di:  
📂 [dashboard_titanic.png](file:///d:/BY%20LEARNING/PYTHON-LEARNING/HARI-KE1/dashboard_titanic.png)

```
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│ [Panel 1]               │ [Panel 2]               │ [Panel 3]               │
│ Donut Chart Bersih:     │ Bar Horizontal:         │ Bar Vertikal:           │
│ Rasio Keselamatan Total │ Prioritas Wanita & Anak │ Tingkat Selamat/Kelas   │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ [Panel 4]               │ [Panel 5]               │ [Panel 6]               │
│ Histogram Sebaran Usia: │ Bar Interaksi Bersih:   │ Bar Rata-rata Tarif:    │
│ Headroom Bebas Tabrakan │ Gender x Kelas Tiket    │ Pengaruh Daya Beli      │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### 🔹 Panel 1: Donut Chart — Rasio Keselamatan Total
* **Data**: **37.8% Selamat** (122 orang) vs **62.2% Meninggal** (201 orang).
* **Desain**: Donut melayang bersih tanpa bingkai kotak kaku (*axis spines disabled*). Nilai selamat diletakkan di titik tengah lubang donut dengan warna toska neon.

### 🔹 Panel 2: Bar Horizontal — Prioritas 'Wanita & Anak'
* **Data**: Wanita mencapai **73.3%** keselamatan, sementara pria hanya **16.7%**.
* **Desain**: Nilai persentase tercantum tepat di sebelah ujung bar dengan label sumbu yang tebal dan jelas.

### 🔹 Panel 3: Bar Logam — Tingkat Selamat per Kelas Tiket
* **Data**: Kelas 1 (VVIP) **55.6%**, Kelas 2 (Bisnis) **41.8%**, Kelas 3 (Ekonomi) **29.3%**.
* **Desain**: Gradasi warna tema logam (Emas, Perak, Perunggu) memberikan isyarat visual hierarki sosial secara instan.

### 🔹 Panel 4: Histogram — Distribusi Usia Penumpang
* **Data**: Puncak keselamatan anak-anak usia balita (0–5 tahun) terlihat jelas, sementara puncak kematian terkonsentrasi di usia 20–35 tahun.
* **Desain**: Skala vertikal hingga 25 orang memberikan ruang lega bagi kotak legenda di pojok kanan atas.

### 🔹 Panel 5: Bar Terkelompok — Kombinasi Gender & Kasta
* **Data**:
  - Wanita Kelas 1: **94%**
  - Wanita Kelas 2: **88%**
  - Wanita Kelas 3: **57%**
  - Pria Kelas 1: **23%**
  - Pria Kelas 2: **16%**
  - Pria Kelas 3: **15%**
* **Desain**: Label persentase diletakkan rapi di atas setiap kolom batang dengan warna masing-masing kategori gender.

### 🔹 Panel 6: Pengaruh Daya Beli — Rata-rata Tarif Tiket
* **Data**: Korban meninggal rata-rata membayar **£23.5** (Median: £12.5), sedangkan penumpang selamat rata-rata membayar **£45.2** (Median: £21.0).
* **Makna Logika**: Penumpang yang selamat rata-rata membeli tiket seharga **hampir 2x lipat** lebih mahal dibanding korban meninggal.

---

## 3. Cara Menjalankan Sendiri di Terminal

Untuk mengeksekusi script ini kapan saja secara mandiri:
```powershell
cd "D:\BY LEARNING\PYTHON-LEARNING\HARI-KE1"
python visualisasi_titanic.py
```
Gambar resolusi tinggi 220 DPI akan langsung diperbarui ke [dashboard_titanic.png](file:///d:/BY%20LEARNING/PYTHON-LEARNING/HARI-KE1/dashboard_titanic.png).
