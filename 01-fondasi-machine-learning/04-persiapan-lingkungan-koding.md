# Modul 1: Pelajaran 4 — Taksonomi Teknik ML & Persiapan Praktik Koding

> "Memahami peta sebelum melangkah ke medan perang adalah kunci agar Anda tidak tersesat di antara ratusan algoritma yang ada."

---

## 1. Evaluasi Tanggapan Anda: Insting Seorang Pemimpin Data

Jawaban Anda pada kasus pinjaman bank sebelumnya sungguh luar biasa. Dua poin yang Anda sampaikan menyentuh konsep krusial di dunia industri:

### Poin A: Bahaya "Akurasi Semu" (Accuracy Paradox)
Anda sangat jeli melihat bahwa angka akurasi 97% di atas kertas bisa sangat menipu jika model mendiskriminasi kelompok tertentu. Di dunia nyata, banyak tim data dipecat karena hanya mengejar angka akurasi tinggi tanpa mengaudit keadilan model mereka terhadap kelompok rentan.

### Poin B: Konsep "Human-in-the-Loop"
Solusi yang Anda tawarkan—mengarahkan tim untuk melakukan verifikasi manusia terhadap pelamar yang jujur dan memiliki rekam jejak bagus—adalah praktik resmi di industri perbankan yang disebut **Human-in-the-Loop**. 
* Komputer bertindak sebagai penyaring awal untuk mempercepat proses.
* Keputusan kritis yang berdampak besar pada hajat hidup manusia tetap diawasi atau divalidasi oleh intuisi nurani manusia.

### Catatan Tambahan Dosen (Rahasia Industri):
Apakah cukup hanya dengan **menghapus kolom kode pos** dari data latih?
Ternyata di dunia data ada yang namanya **Proxy Variable (Variabel Pengganti)**. Meskipun kolom kode pos sudah kita hapus, komputer masih bisa menebak bahwa seseorang tinggal di wilayah miskin dari data lain, misalnya: nominal transaksi belanja bulanan, cabang bank tempat membuka rekening, atau jenis provider internet yang digunakan. 

Karena itu, solusi teknis yang benar adalah melatih model murni berdasarkan **indikator kelayakan bisnis** (seperti laba usaha, arus kas, dan disiplin pembayaran utang di masa lalu), bukan atribut wilayah maupun latar belakang keluarga.

---

## 2. Pelajaran 4: Tiga Keluarga Besar Machine Learning

Sebelum kita membuka editor kode dan mulai mengetik perintah Python, Anda perlu tahu bahwa semua algoritma Machine Learning di dunia ini terbagi ke dalam **tiga keluarga besar**:

```
                         ┌─────────────────────────┐
                         │    MACHINE LEARNING     │
                         └────────────┬────────────┘
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
[ SUPERVISED LEARNING ]     [ UNSUPERVISED LEARNING ]    [ REINFORCEMENT LEARNING ]
  (Ada Kunci Jawaban)          (Tanpa Kunci Jawaban)        (Hadiah & Hukuman)
         │                            │                            │
   ┌─────┴─────┐                      │                            │
   ▼           ▼                      ▼                            ▼
[Regresi] [Klasifikasi]          [Clustering]              [Agen Otomatis]
(Tebak      (Tebak              (Mengelompokkan              (Game, Mobil
 Angka)     Kategori)              Data Serupa)                 Otonom)
```

Mari kita pahami ketiganya dengan contoh sehari-hari yang sangat mudah:

### A. Supervised Learning (Pembelajaran Terbimbing / Ada Kunci Jawaban)
Ibarat seorang murid yang belajar mengerjakan soal ujian lengkap dengan buku kunci jawaban di sampingnya. Komputer diberikan data masukan beserta hasil akhirnya.

Keluarga ini terbagi menjadi dua jenis tugas utama:
1. **Regresi (Regression):** Jika hasil yang ingin ditebak berupa **angka kontinu**.
   * *Contoh:* Memprediksi harga rumah (misalnya Rp 850 juta), memprediksi suhu cuaca besok (31,5°C), atau memprediksi omzet penjualan bulan depan.
2. **Klasifikasi (Classification):** Jika hasil yang ingin ditebak berupa **kategori / label**.
   * *Contoh:* Menentukan apakah email ini spam atau bukan spam, menentukan foto ini kucing atau anjing, mendiagnosis apakah pasien positif atau negatif penyakit.

---

### B. Unsupervised Learning (Pembelajaran Tanpa Kunci Jawaban)
Ibarat Anda menumpahkan sekotak kelereng warna-warni yang bentuk dan ukurannya beragam ke atas meja, lalu meminta anak kecil merapikannya tanpa memberitahu aturan apa pun. Anak tersebut akan mengelompokkan sendiri kelereng-kelereng tersebut berdasarkan kesamaan warna atau ukuran.

* Tidak ada kunci jawaban yang benar atau salah.
* Komputer bertugas mencari **pola tersembunyi** atau **pengelompokan alami** dalam data.
* **Contoh Aplikasi Nyata:** 
  Aplikasi e-commerce mengelompokkan jutaan pelanggan menjadi beberapa segmen: *"Pelanggan tipe pemburu diskon"*, *"Pelanggan tipe borong barang mewah"*, atau Spotify mengelompokkan lagu-lagu berdasarkan kemiripan ritme dan nada (*Clustering*).

---

### C. Reinforcement Learning (Pembelajaran Berbasis Imbalan & Hukuman)
Ibarat melatih seekor anjing peliharaan. Anda tidak mengajari anjing cara duduk dengan rumus matematika. Ketika anjing berhasil duduk sesuai perintah, Anda memberinya camilan (*Reward*). Ketika dia menggigit sepatu, Anda menegurnya (*Penalty*).

* Komputer belajar lewat proses **coba-salah (trial and error)** di dalam sebuah lingkungan (*environment*).
* Komputer akan mencari strategi terbaik untuk mengumpulkan poin imbalan sebanyak mungkin.
* **Contoh Aplikasi Nyata:** AI yang belajar bermain game catur (AlphaZero), mobil tanpa sopir yang belajar bermanuver di jalan raya, atau lengan robot di pabrik.

---

## 3. Kapan Mulai Koding? Sekarang Juga! 🚀

Kabar baik untuk Anda: saya sudah memeriksa komputer lokal Anda secara langsung, dan **perangkat Anda sudah sangat siap untuk mulai koding!**

### Status Perangkat Anda Saat Ini:
* ✅ **Python:** Sudah terpasang versi modern (`Python 3.14.3`).
* ✅ **Package Manager:** `pip` sudah aktif dan siap memasang modul data science.
* ✅ **Pustaka Data Dasar:** `pandas` (untuk membaca tabel data) dan `matplotlib` (untuk menggambar grafik) sudah terpasang.

Kita hanya membutuhkan satu pustaka pamungkas yang menjadi standar industri dunia untuk Machine Learning klasik, yaitu: **`scikit-learn`**.

---

## 4. Rencana Praktik Koding Pertama Kita (Modul 2)

Sesuai urutan kurikulum resmi Microsoft, proyek koding pertama kita adalah **Modul 2: Regresi Linier**.

Kita akan menggunakan dataset unik dari dunia nyata: **Data Harga Labu di Pasar Amerika Utara (North American Pumpkin Market) 🎃**.

### Apa yang Akan Kita Lakukan di Kode Pertama Nanti?
1. Membaca file data tabel (.csv) menggunakan Python dan `pandas`.
2. Membersihkan data: membuang kolom yang tidak perlu dan merapikan format tanggal/harga.
3. Membuat visualisasi grafik sebaran data menggunakan `matplotlib`.
4. Melatih model Machine Learning pertama Anda menggunakan `scikit-learn` untuk memprediksi harga labu berdasarkan ukuran dan bulan panennya.

---

## Langkah Berikutnya

Jika Anda sudah siap untuk mulai menulis kode pertama, silakan beri tahu saya. 

Saya akan langsung memandu Anda memasang `scikit-learn` (jika belum aktif) dan membuatkan file notebook/skrip latihan pertama di folder kerja Anda lengkap dengan penjelasan setiap baris kodenya!
