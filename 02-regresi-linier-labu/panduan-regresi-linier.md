# Modul 2: Pelajaran 1 — Praktik Koding Pertama: Regresi Linier Harga Labu 🎃

Selamat! Anda resmi memulai perjalanan teknis sebagai praktisi Machine Learning. 

Semua kebutuhan sudah kita siapkan langsung di komputer Anda:
* Library **`scikit-learn`** sudah berhasil dipasang.
* Dataset resmi **`data/US-pumpkins.csv`** (berisi 1.757 data penjualan labu di Amerika Utara) sudah diunduh ke folder kerja Anda.
* Skrip Python pertama Anda, **`latihan_regresi_labu.py`**, sudah dibuat dan sukses dijalankan!

Di dokumen ini, kita akan membedah logika kode tersebut baris demi baris, agar Anda paham betul apa yang sedang terjadi di balik layar.

---

## 1. Cerita di Balik Dataset Labu (Kenapa Labu?)

Di Amerika Utara, labu adalah komoditas musiman yang sangat unik. Menjelang perayaan Halloween dan Thanksgiving (bulan September hingga November), permintaan labu melonjak drastis.

Namun, data mentah dari pasar petani ini sangat "berantakan":
1. **Satuannya tidak seragam:** Ada petani yang menjual per keranjang standar (*bushel*), ada yang per kotak kayu besar (*bin*), dan ada yang per peti (*crate*).
2. **Harganya berupa rentang:** Data mencatat harga terendah (*Low Price*) dan harga tertinggi (*High Price*) pada hari itu.
3. **Format tanggal teks:** Komputer tidak bisa langsung menghitung tanggal jika masih berupa teks seperti `"9/24/16"`.

Sebagai data scientist, 70% waktu kita di dunia nyata dihabiskan untuk **membersihkan data (Data Wrangling)** sebelum komputer bisa melatih model.

---

## 2. Bedah Kode Baris Demi Baris

Mari kita pelajari alur kerja skrip `latihan_regresi_labu.py` yang ada di folder Anda:

### Tahap A: Membaca dan Menyaring Data (Cleaning)
```python
import pandas as pd

# Membaca file data tabel
df = pd.read_csv('data/US-pumpkins.csv')

# Menyaring hanya kemasan 'bushel' agar satuannya adil
df = df[df['Package'].str.contains('bushel', na=False, case=False)]

# Menghitung harga tengah rata-rata
df['Price'] = (df['Low Price'] + df['High Price']) / 2
```
**Mengapa langkah ini penting?**  
Jika kita mencampur harga 1 keranjang kecil (*bushel*) dengan 1 peti raksasa (*bin*), komputer akan bingung karena perbandingannya tidak seimbang. Dengan menyaringnya, data kita menjadi adil dan setara.

---

### Tahap B: Membagi Data untuk Latihan dan Ujian (Train - Test Split)
Ini adalah salah satu aturan emas dalam Machine Learning:
```python
from sklearn.model_selection import train_test_split

X = clean_df[['DayOfYear']]  # Masukan: Hari ke berapa dalam setahun (misal 268 = September)
y = clean_df['Price']        # Target yang ingin ditebak: Harga labu

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

**Konsep Dosen yang Perlu Anda Ingat:**
* **`X_train` & `y_train` (80% data):** Ini adalah buku bahan belajar model. Model membaca soal beserta jawabannya untuk mencari pola garis hubungan.
* **`X_test` & `y_test` (20% data):** Ini adalah lembar ujian akhir. Data ini disimpan rapat-rapat dan **tidak pernah dilihat oleh model saat latihan**. Tujuannya agar kita bisa menguji apakah model benar-benar pintar atau hanya menghafal data latihan (*overfitting*).

---

### Tahap C: Melatih Model Machine Learning
Hanya dengan 2 baris kode ini, algoritma Scikit-learn bekerja mencari rumus garis lurus terbaik:
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)  # Proses belajar berlangsung di sini!
```

Hasil perhitungan model Anda:
* **Kemiringan Garis (Koefisien):** `-0.0067`  
  *Artinya:* Setiap harinya, harga labu cenderung sedikit menurun sekitar 0,0067 dollar per bushel.
* **Titik Potong (Intercept):** `20.4912`  
  *Artinya:* Titik awal patokan harga di garis regresi adalah sekitar $20,49.

---

### Tahap D: Evaluasi Hasil & Misteri Skor R2
Saat kita menguji model pada data ujian (`X_test`), sistem menghasilkan:
* **Rata-rata kesalahan kuadrat (MSE):** `32.83`
* **Skor R-squared (R2 Score):** `0.0007`

**Apa arti skor ini?**  
Skor $R^2$ berkisar antara 0 sampai 1 (atau 0% hingga 100%). Angka `0.0007` menunjukkan bahwa **garis lurus biasa (linier) hampir tidak bisa menangkap pola fluktuasi harga labu secara akurat.**

**Mengapa demikian?**  
Karena harga labu di dunia nyata tidak bergerak lurus turun atau lurus naik! Harga labu biasanya melonjak naik tajam di pertengahan musim gugur saat perayaan Halloween, lalu anjlok kembali di akhir musim. Polanya berbentuk **kurva (lengkungan)**, bukan garis lurus.

Di sinilah kurikulum kita akan membawa Anda ke teknik berikutnya: **Regresi Polinomial (Polynomial Regression)** yang mampu menggambar garis melengkung mengikuti lekuk data!

---

## 3. Melihat Hasil Gambar Visualisasi Anda

Skrip yang baru saja kita jalankan telah menghasilkan sebuah file grafik di folder kerja Anda:
* File gambar: **`grafik_prediksi_labu.png`**

Silakan buka file gambar tersebut di panel penjelajah berkas (file explorer) Anda di sebelah kiri. Anda akan melihat titik-titik hitam (data asli penjualan labu) dan sebuah garis merah lurus (hasil tebakan model Machine Learning pertama Anda).

---

## 4. Cara Menjalankan Kode Sendiri di Terminal

Anda bisa mencoba menjalankan kode ini sendiri kapan pun melalui terminal:
1. Buka terminal di editor Anda.
2. Pastikan Anda berada di direktori `d:\BY LEARNING`.
3. Ketik perintah berikut lalu tekan Enter:
   ```bash
   python latihan_regresi_labu.py
   ```

---

## Tantangan Eksperimen Ringan untuk Anda

Coba buka file [latihan_regresi_labu.py](file:///d:/BY%20LEARNING/latihan_regresi_labu.py), lalu perhatikan bagian nomor 5:
```python
hari_contoh = [[260]]
```
* Angka `260` mewakili hari ke-260 dalam setahun (sekitar pertengahan September).
* Coba ganti angka tersebut menjadi `300` (sekitar akhir Oktober, tepat saat Halloween).
* Simpan file, lalu jalankan kembali skripnya di terminal. Berapa harga yang ditebak oleh model Anda?

Setelah Anda mencobanya, ceritakan apa yang Anda amati!
