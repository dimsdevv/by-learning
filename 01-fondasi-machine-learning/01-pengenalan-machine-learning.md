# Modul 1: Pengenalan Machine Learning

Selamat datang di materi pertama kita. Di modul ini, kita akan berkenalan dengan Machine Learning dari dasarnya dulu. Tujuannya sederhana: agar Anda punya gambaran yang utuh dan intuisi yang tepat tentang apa itu Machine Learning, kapan kita membutuhkannya, dan bagaimana cara kerjanya secara umum.

---

## 1. Apa Sebenarnya Machine Learning Itu?

Secara sederhana, Machine Learning adalah cara membuat komputer bisa belajar dari pengalaman dan data, tanpa kita harus mendiktekan setiap langkahnya secara manual.

Coba bayangkan bagaimana seorang anak kecil belajar mengenali seekor kucing. Orang tua tidak pernah memberikan rumus matematika seperti:
* "Kucing adalah hewan dengan telinga segitiga sudut 45 derajat, berat 3,5 kilogram, dan panjang kumis 5 centimeter."

Yang dilakukan orang tua hanyalah menunjukkan berbagai contoh:
* "Lihat, itu kucing."
* "Yang di buku itu juga kucing."
* "Kalau yang itu anjing, bukan kucing."

Lama-kelamaan, otak si anak menyimpulkan sendiri pola-pola umum yang membedakan kucing dari hewan lain. 

Machine Learning bekerja dengan prinsip yang persis sama. Alih-alih kita menulis aturan kaku di dalam kode, kita memberikan banyak contoh data kepada komputer, lalu membiarkan komputer mengenali polanya sendiri.

---

## 2. Perbedaan Pemrograman Biasa vs Machine Learning

Untuk melihat bedanya, mari kita bandingkan cara kerja keduanya:

### Cara Pemrograman Biasa (Tradisional)
Pada pemrograman biasa, manusia yang berpikir keras menentukan seluruh aturan logikanya.
* **Input:** Anda memasukkan data dan aturan yang sudah Anda tulis sendiri.
* **Proses:** Komputer hanya menjalankan instruksi yang Anda berikan persis apa adanya.
* **Output:** Jawaban atau hasil perhitungan.

**Contoh:** Aplikasi kalkulator atau perhitungan pajak. Rumusnya sudah pasti, aturannya jelas, dan tidak akan berubah sendiri.

### Cara Machine Learning
Pada Machine Learning, peran tersebut dibalik karena masalah yang dihadapi terlalu rumit untuk dibuatkan aturannya satu per satu oleh manusia.
* **Input:** Anda memasukkan data dan contoh-contoh jawaban di masa lalu.
* **Proses:** Komputer mencari sendiri pola atau rumus yang menghubungkan data dengan jawaban tersebut.
* **Output:** Sebuah model atau aturan baru yang siap digunakan untuk menebak data baru.

**Contoh:** Filter email penipuan (spam). Penipu selalu mengubah kata-kata mereka setiap hari. Jika programmer harus menulis aturan baru setiap kali ada trik baru, programmer akan kewalahan. Dengan Machine Learning, sistem belajar sendiri dari ribuan email spam baru yang masuk setiap hari.

---

## 3. Tiga Elemen Utama Menurut Pakar (Tom Mitchell)

Seorang profesor ilmu komputer bernama Tom Mitchell merumuskan bahwa sebuah komputer bisa dikatakan "belajar" jika memenuhi tiga hal berikut:

1. **Tugas (Task):** Pekerjaan apa yang ingin kita selesaikan?  
   *Contoh:* Memprediksi apakah sebuah transaksi kartu kredit itu asli atau penipuan.

2. **Pengalaman (Experience):** Data masa lalu apa yang dipelajari oleh komputer?  
   *Contoh:* Catatan riwayat 100.000 transaksi nasabah terdahulu, lengkap dengan catatan mana yang sah dan mana yang terbukti dibobol.

3. **Tolok Ukur Keberhasilan (Performance):** Bagaimana kita tahu komputer kita sudah pintar?  
   *Contoh:* Berapa persen transaksi penipuan yang berhasil dicegat dengan benar tanpa salah memblokir transaksi nasabah yang sah.

Jika semakin banyak data transaksi yang dipelajari membuat sistem semakin jarang salah menebak, artinya komputer tersebut benar-benar sedang belajar.

---

## 4. Kapan Kita Butuh Machine Learning?

Sebagai aturan umum yang sangat penting: **Jangan gunakan Machine Learning jika masalah Anda bisa diselesaikan dengan logika sederhana.**

### Gunakan Pemrograman Biasa Jika:
* Aturan dan rumusnya sudah pasti serta tidak berubah-ubah. Misalnya perhitungan diskon belanja, rumus bunga pinjaman, atau konversi suhu dari Celsius ke Fahrenheit.
* Hasilnya harus 100% tepat dan tidak boleh ada toleransi salah sama sekali.

### Gunakan Machine Learning Jika:
* Masalahnya terlalu rumit untuk dituliskan aturannya satu per satu. Misalnya mengenali wajah seseorang di foto, memahami suara orang yang berbicara, atau menerjemahkan bahasa.
* Pola datanya selalu berkembang dan berubah dari waktu ke waktu, seperti tren rekomendasi video di media sosial.
* Kita menerima bahwa hasilnya berupa tebakan atau estimasi cerdas dengan tingkat akurasi tertentu (misalnya 95% tepat).

---

## 5. Bahan Diskusi Bersama

Agar pemahaman Anda semakin melekat, mari kita diskusikan dua skenario berikut dengan bahasa Anda sendiri:

### Skenario Pertama: Ongkos Kirim Belanja Online
Sebuah toko online ingin membuat fitur perhitungan ongkos kirim. Ongkosnya dihitung berdasarkan berat paket dalam kilogram, jarak kilometer dari toko ke alamat pembeli, dan pilihan kurir (ekspres atau reguler).
* Menurut Anda, apakah fitur ini perlu dibuat menggunakan Machine Learning, atau cukup menggunakan logika pemrograman biasa? Mengapa demikian?

### Skenario Kedua: Prediksi Risiko Penyakit
Sebuah klinik ingin membuat aplikasi untuk memperkirakan apakah seorang pasien berisiko terkena serangan jantung dalam satu tahun ke depan, berdasarkan riwayat tekanan darah, usia, kadar kolesterol, dan gaya hidup pasien.
* Coba tentukan tiga hal ini:
  1. Apa **Tugas** yang harus dikerjakan komputer?
  2. Apa **Pengalaman** (data) yang dibutuhkan komputer untuk belajar?
  3. Bagaimana kita mengukur **Keberhasilan** sistem tersebut?

Tuliskan pendapat Anda dengan santai, lalu kita bahas bersama!
