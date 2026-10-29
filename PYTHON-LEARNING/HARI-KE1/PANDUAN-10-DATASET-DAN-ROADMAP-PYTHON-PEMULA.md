# Panduan Dosen: 10 Rekomendasi Dataset Ramah Pemula & Peta Belajar Python dari Nol

> "Menyadari bahwa Anda belum memiliki dasar Python bukanlah kelemahan, melainkan titik awal yang sangat jujur dan bijak. Kunci belajar data science bagi pemula bukanlah menghafal seluruh sintaks pemrograman, melainkan belajar lewat data yang ceritanya menarik dan mudah dibayangkan."

---

## 1. Selamat Atas Keberhasilan Eksekusi Pertama Anda!

Sebelum kita membahas rekomendasi data, mari kita beri apresiasi: Anda baru saja berhasil menjalankan skrip Machine Learning pertama Anda di terminal komputer sendiri! 

Output yang Anda dapatkan:
* **Hari ke-260 (Pertengahan September) -> Perkiraan harga labu adalah $18.75.**

Komputer Anda sudah terbukti mampu memproses data dan mengeksekusi model. Sekarang, saatnya kita memperkuat fondasi Anda di bahasa **Python** dengan memilih data latihan yang tepat.

---

## 2. Kriteria Data yang Cocok untuk yang Belum Punya Dasar Python

Bagi orang yang baru pertama kali menyentuh kode, **jangan langsung menyentuh data rumit** seperti rekaman video, audio, atau data triliunan baris. 

Data yang paling cocok untuk pemula harus memenuhi 3 syarat:
1. **Berbentuk Tabel Sederhana (CSV / Excel):** Ada baris dan kolom yang jelas, seperti tabel keuangan atau absensi.
2. **Topiknya Dekat dengan Kehidupan Sehari-hari:** Anda tidak perlu pusing memikirkan rumus ilmiah; logikanya sudah Anda pahami di kepala.
3. **Jumlah Baris Sedang (100 sampai 5.000 baris):** Cukup ringan dibuka di laptop, tidak membuat komputer lemot, tapi cukup kaya untuk dianalisis.

---

## 3. 10 Rekomendasi Dataset Terbaik untuk Belajar Data Science dari Nol

Berikut adalah 10 dataset pilihan yang menjadi standar emas di universitas dan komunitas data global, diurutkan dari yang paling mudah:

### 1. Data Penumpang Kapal Titanic (Titanic Survival Dataset) 🚢
* **Cerita Datanya:** Catatan daftar penumpang kapal legendaris Titanic, mencakup usia, jenis kelamin, kelas tiket (kelas 1, 2, atau 3), tarif tiket, dan apakah mereka selamat dari tragedi tersebut.
* **Kenapa Sangat Bagus untuk Pemula:** Sangat intuitif. Anda bisa langsung menjawab pertanyaan logis tanpa rumus rumit: *"Apakah penumpang wanita dan anak-anak benar-benar lebih banyak yang selamat?"* atau *"Apakah penumpang kelas 1 memiliki tingkat keselamatan lebih tinggi daripada kelas 3?"*
* **Skill Python yang Dilatih:** Memfilter data (`df[df['Sex'] == 'female']`) dan menghitung persentase.

---

### 2. Data Menu & Nutrisi Restoran Cepat Saji (Fast Food / Starbucks Menu) 🍔☕
* **Cerita Datanya:** Daftar menu makanan dan minuman (seperti menu McDonald's atau Starbucks) lengkap dengan jumlah kalori, kadar gula, lemak, dan protein.
* **Kenapa Sangat Bagus untuk Pemula:** Siapa pun paham konsep kalori dan gula. Anda tidak perlu latar belakang matematika untuk membedakan makanan sehat dan tidak sehat.
* **Tantangan Menarik:** Mencari menu dengan kalori tertinggi, atau membuat grafik perbandingan kadar gula antara minuman kopi vs teh.
* **Skill Python yang Dilatih:** Mengurutkan data dari yang terbesar ke terkecil (*sorting*), serta membuat diagram batang sederhana.

---

### 3. Data Penjualan Toko Ritel / Supermarket (Supermarket Sales) 🛒
* **Cerita Datanya:** Catatan transaksi kasir: tanggal pembelian, kategori barang (makanan, elektronik, fesyen), metode pembayaran (tunai / kartu kredit), dan total belanjaan.
* **Kenapa Sangat Bagus untuk Pemula:** Ini adalah kasus nomor satu yang paling sering dicari di dunia kerja nyata. 
* **Tantangan Menarik:** *"Bulan apa penjualan paling ramai?"*, *"Metode pembayaran apa yang paling disukai pembeli?"*, atau *"Kategori barang mana yang menyumbang keuntungan paling besar?"*
* **Skill Python yang Dilatih:** Mengelompokkan data berdasarkan kategori (*grouping*) dan menjumlahkan total uang (*aggregation*).

---

### 4. Data Lagu Populer di Spotify (Spotify Top Songs) 🎧
* **Cerita Datanya:** Daftar lagu-lagu hits dunia lengkap dengan nama artis, genre, tahun rilis, durasi lagu, hingga skor keceriaan musik (*danceability* dan *energy*).
* **Kenapa Sangat Bagus untuk Pemula:** Belajar sambil mendengarkan musik favorit membuat proses belajar terasa seperti bermain, bukan belajar berat.
* **Tantangan Menarik:** Melihat tren durasi lagu dari tahun ke tahun (apakah lagu zaman sekarang makin pendek karena TikTok?), atau melihat artis dengan lagu hits terbanyak.
* **Skill Python yang Dilatih:** Menghitung frekuensi kemunculan teks dan membuat grafik tren waktu.

---

### 5. Data Rating dan Ulasan Film IMDb / Netflix 🎬
* **Cerita Datanya:** Ribuan judul film lengkap dengan tahun rilis, genre (aksi, horor, komedi), durasi, sutradara, dan skor rating dari penonton (skala 1 sampai 10).
* **Kenapa Sangat Bagus untuk Pemula:** Sangat seru untuk eksplorasi.
* **Tantangan Menarik:** *"Sutradara mana yang film-filmnya konsisten mendapat rating di atas 8?"* atau *"Apakah film berdurasi panjang selalu mendapat rating lebih bagus?"*
* **Skill Python yang Dilatih:** Menghapus data yang kosong (*missing values*) dan membedah korelasi angka.

---

### 6. Data Bunga Iris (The Famous Iris Dataset) 🌸
* **Cerita Datanya:** Hanya berisi 150 data bunga dari 3 spesies berbeda. Setiap bunga hanya diukur 4 hal: panjang kelopak, lebar kelopak, panjang daun mahkota, dan lebar daun mahkota.
* **Kenapa Sangat Bagus untuk Pemula:** Ini adalah dataset "Hello World"-nya seluruh ilmuwan data di dunia. Datanya sangat bersih dan tidak ada kesalahan ketik sama sekali.
* **Tantangan Menarik:** Membuat grafik titik-titik warna-warni (*scatter plot*) untuk melihat bagaimana ukuran kelopak memisahkan ketiga jenis bunga tersebut dengan sangat rapi.
* **Skill Python yang Dilatih:** Visualisasi warna-warni dua dimensi menggunakan pustaka `matplotlib`.

---

### 7. Data Cuaca Harian Kota (Daily Weather Data) ⛅
* **Cerita Datanya:** Catatan suhu harian, kelembaban udara, kecepatan angin, dan apakah hari itu turun hujan atau tidak di suatu kota selama 1 tahun.
* **Kenapa Sangat Bagus untuk Pemula:** Mengenalkan Anda pada jenis data waktu (*time series*).
* **Tantangan Menarik:** Menghitung suhu rata-rata bulanan dan melihat perubahan musim.
* **Skill Python yang Dilatih:** Mengolah format tanggal dan jam (*datetime*).

---

### 8. Data Penjualan dan Harga Rumah (Housing Prices) 🏡
* **Cerita Datanya:** Daftar rumah yang terjual lengkap dengan luas tanah (meter persegi), jumlah kamar tidur, jumlah kamar mandi, jarak ke pusat kota, dan harga jual akhirnya.
* **Kenapa Sangat Bagus untuk Pemula:** Sangat cocok sebagai jembatan untuk memahami konsep Machine Learning regresi (seperti materi labu yang baru saja kita pelajari).
* **Tantangan Menarik:** Menguji intuisi: apakah menambah 1 kamar tidur selalu menaikkan harga rumah, atau luas tanah yang jauh lebih berpengaruh?
* **Skill Python yang Dilatih:** Menghitung rumus korelasi antar variabel angka.

---

### 9. Data Gaji Karyawan di Industri Teknologi (Tech Salaries Dataset) 💼
* **Cerita Datanya:** Survei gaji anonim para pekerja teknologi: posisi pekerjaan (Data Scientist, Software Engineer), tahun pengalaman, negara, dan nominal gaji tahunan.
* **Kenapa Sangat Bagus untuk Pemula:** Memberi wawasan nyata tentang karier masa depan yang sedang Anda tuju.
* **Tantangan Menarik:** Melihat perbandingan gaji rata-rata antara Data Analyst, Data Engineer, dan Machine Learning Engineer berdasarkan lama pengalaman kerja.
* **Skill Python yang Dilatih:** Menghitung nilai median, rata-rata (*mean*), dan menyaring data berdasarkan rentang angka.

---

### 10. Data Pasar Labu Amerika (US-Pumpkins Dataset) 🎃
* **Cerita Datanya:** Dataset yang sudah ada di komputer Anda saat ini (`d:\BY LEARNING\data\US-pumpkins.csv`).
* **Kenapa Tetap Masuk Daftar:** Karena Anda sudah punya filenya! Daripada mencari file baru, data ini sebenarnya menyimpan banyak cerita lain yang belum kita gali: variasi jenis labu (pie pumpkin, big mac), kota pasar penjualan (Boston, New York), dan perbedaan harga berdasarkan warna labu (oranye vs putih).
* **Tantangan Menarik:** Membandingkan harga labu oranye biasa dengan labu hias warna putih.

---

## 4. Jembatan Belajar: 4 Fondasi Python yang Perlu Anda Kuasai

Banyak orang gagal belajar Data Science karena mereka belajar Python seperti seorang pembuat website atau pembuat game. Itu keliru! 

Untuk Data Science, Anda **TIDAK PERLU** menguasai seluruh bahasa Python. Anda hanya butuh 4 hal dasar ini:

```
[1. Variabel & Tipe Data]   ➔ Menyimpan angka dan teks sederhana
          │
[2. List & Dictionary]      ➔ Menyimpan kumpulan daftar nama atau tabel mini
          │
[3. Pandas DataFrame]       ➔ Membuka, memfilter, dan mengotak-atik tabel seperti Excel
          │
[4. Matplotlib Chart]       ➔ Mengubah tabel angka menjadi gambar grafik warna-warni
```

---

## 5. Rekomendasi Langkah Kita Selanjutnya

Sebagai dosen Anda, saya menyarankan pendekatan: **"Belajar Python Sambil Mengulik Data Nyata (Learning by Doing)"**. 

Kita tidak akan belajar teori sintaks yang membosankan. Sebaliknya, kita bisa memilih salah satu dari 10 dataset di atas (misalnya: **Data Menu Cepat Saji** yang super santai, atau **Data Penumpang Titanic** yang penuh cerita), lalu kita pelajari Python dasar melalui studi kasus tersebut.

Dari 10 data di atas, mana topik yang paling membuat Anda penasaran untuk kita bedah bersama?
