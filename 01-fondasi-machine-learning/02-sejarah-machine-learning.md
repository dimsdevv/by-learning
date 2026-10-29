# Modul 1: Evaluasi Diskusi & Pelajaran 2

---

## Bagian 1: Evaluasi dan Pembahasan Jawaban Anda

Pertama-tama, kerja yang sangat bagus! Jawaban Anda menunjukkan bahwa Anda sudah mulai menangkap pola pikir seorang praktisi data. Mari kita bedah satu per satu:

### Jawaban Nomor 1 (Ongkos Kirim): 100% Tepat!
Analisis Anda sangat akurat. 
* Perhitungan ongkos kirim punya rumus pasti: berat dikali jarak dikali tarif per kilometer.
* Aturannya jelas, tidak berubah-ubah secara tiba-tiba, dan manusia sangat mudah menuliskannya ke dalam beberapa baris kode pemrograman biasa.
* Menggunakan Machine Learning untuk kasus ini justru salah kaprah karena akan membuang waktu, biaya server, dan hasilnya malah bisa meleset (karena Machine Learning sifatnya estimasi, sedangkan pelanggan ingin kepastian tarif).

### Jawaban Nomor 2 (Risiko Serangan Jantung): Arahnya Sudah Bagus, Mari Kita Pertajam
Jawaban Anda sudah menangkap intinya: komputer membantu proses analisis data kesehatan. Namun, ada perbedaan penting antara **validasi kondisi sekarang** dengan **prediksi masa depan**:

1. **Tugas (Task):**
   Bukan memvalidasi apakah pasien *sedang* sakit jantung saat ini (karena itu tugas dokter dengan alat medis langsung), melainkan **memprediksi kemungkinan**: apakah pasien yang saat ini tampak sehat berisiko mengalami serangan jantung dalam satu tahun ke depan?
   
2. **Pengalaman (Experience / Data yang dipelajari):**
   Komputer mempelajari puluhan ribu data rekam medis pasien di masa lalu. Komputer melihat catatan:
   * "Pasien A, usia 52 tahun, tensi 140, kolesterol 240, merokok -> Ternyata 8 bulan kemudian kena serangan jantung."
   * "Pasien B, usia 45 tahun, tensi 115, kolesterol 180, rajin olahraga -> Ternyata aman."
   Dari ribuan riwayat inilah komputer belajar mengenali kombinasi tanda-tanda bahaya yang tersembunyi.

3. **Tolok Ukur Keberhasilan (Performance):**
   Seberapa jitu tebakan komputer tersebut. Khusus untuk kasus medis, tolok ukur yang paling penting adalah: **sistem tidak boleh sampai melewatkan orang yang sebenarnya berisiko tinggi** (jangan sampai ada pasien bahaya yang dibilang sehat).

---

## Bagian 2: Pelajaran 2 — Kisah di Balik Machine Learning

Sebelum kita mulai utak-atik data di modul berikutnya, sangat menarik untuk mengetahui: bagaimana teknologi ini bisa sampai di titik sekarang? Kenapa baru beberapa tahun belakangan ini Machine Learning begitu meledak di seluruh dunia?

Ternyata, perjalanan Machine Learning penuh dengan pasang surut yang dramatis.

---

### 1. Awal Mula: Apakah Mesin Bisa Berpikir? (Tahun 1950-an)

Semua berawal dari seorang matematikawan asal Inggris bernama **Alan Turing**. Pada tahun 1950, ia mengajukan pertanyaan yang mengguncang dunia: *"Bisakah mesin berpikir?"*

Ia membuat sebuah tes sederhana yang terkenal dengan nama **Turing Test**:
* Seseorang mengobrol lewat ketikan teks dengan dua lawan bicara di balik dinding: satu manusia dan satu program komputer.
* Jika orang tersebut tidak bisa membedakan mana jawaban manusia dan mana jawaban komputer, maka komputer itu dianggap berhasil menunjukkan kecerdasan.

Beberapa tahun setelahnya, tepatnya tahun 1956, para ilmuwan berkumpul di Dartmouth College, Amerika Serikat. Di sanalah istilah **Artificial Intelligence (Kecerdasan Buatan)** resmi lahir. Para ilmuwan saat itu sangat optimis bahwa dalam 10 sampai 20 tahun, komputer akan bisa meniru seluruh kecerdasan manusia.

Namun, kenyataan berkata lain.

---

### 2. "Musim Dingin AI" (AI Winter)

Optimisme yang berlebihan di awal justru membawa kekecewaan besar. Pada era 1970-an hingga 1980-an, proyek-proyek kecerdasan buatan mengalami masa mati suri yang dikenal sebagai **AI Winter (Musim Dingin AI)**.

Mengapa hal itu bisa terjadi? Ada dua alasan utama:
1. **Komputer zaman itu masih sangat lambat:** Kemampuan memori dan prosesornya belum sanggup melakukan miliaran hitungan rumit.
2. **Data sangat langka:** Zaman dulu belum ada internet, belum ada kamera digital, dan belum ada smartphone. Semua data masih dicatat manual di atas kertas.

Karena hasilnya tidak sesuai dengan janji manis para peneliti, dana riset dari pemerintah dan perusahaan dipangkas habis-habisan. Bidang ini sempat dianggap jalan buntu.

---

### 3. Titik Balik dan Era Kebangkitan Modern

Lalu, apa yang membuat Machine Learning tiba-tiba bangkit kembali dan menjadi begitu hebat seperti sekarang? 

Ada tiga faktor pemicu utama yang datang secara bersamaan:

#### A. Ledakan Data (Big Data)
Munculnya internet, media sosial, sensor, dan ponsel pintar membuat dunia dibanjiri data setiap detiknya. Machine Learning yang tadinya kelaparan data, kini punya bahan bakar yang melimpah ruah untuk belajar.

#### B. Lompatan Kekuatan Komputer
Prosesor komputer menjadi jutaan kali lebih cepat. Menariknya, kartu grafis (GPU) yang awalnya hanya dibuat untuk merender grafis video game, ternyata sangat jago melakukan operasi hitungan matematika Machine Learning dalam waktu singkat.

#### C. Algoritma Terbuka dan Gratis
Dulu, algoritma canggih hanya tersimpan rapat di laboratorium universitas ternama. Sekarang, siapa saja bisa menggunakan pustaka Machine Learning kelas dunia seperti **Python** dan **Scikit-learn** secara gratis hanya dengan beberapa baris kode.

---

## 4. Bahan Refleksi untuk Pelajaran 2

Setelah melihat sejarah panjang pasang surut Machine Learning di atas, coba renungkan satu pertanyaan ini:

> Menurut Anda, di masa sekarang ini, apakah ada risiko kita akan mengalami "Musim Dingin AI" jilid berikutnya? Atau apakah teknologi ini sudah terlalu kuat untuk bisa redup kembali? Mengapa Anda berpandangan demikian?

Silakan renungkan sebentar dan tuliskan pandangan Anda. Setelah ini, kita akan melangkah ke topik yang sangat krusial: **Etika, Bias, dan Keadilan dalam Machine Learning (Pelajaran 3)**.
