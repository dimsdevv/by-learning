# Modul 1: Pelajaran 3 — Etika, Bias, dan Keadilan dalam AI

> "Komputer tidak memiliki niat jahat. Komputer hanya menatap cermin masa lalu kita, lalu mengulangi apa yang pernah kita lakukan dengan kecepatan jutaan kali lebih cepat."

---

## 1. Tanggapan Dosen untuk Analisis Anda Sebelumnya

Analisis Anda mengenai potensi Musim Dingin AI (*AI Winter*) sangat tepat dan berbobot. 

Anda menyebutkan hal yang sangat krusial: **ekosistemnya sudah terbentuk nyata di industri**.
* Di era 1970-an, AI hanya wacana riset di laboratorium universitas. 
* Sekarang, AI digerakkan oleh industri bernilai triliunan dollar: pabrikan chip raksasa seperti NVIDIA yang merancang GPU khusus komputasi AI (seperti arsitektur Hopper dan Blackwell), integrasi NPU (*Neural Processing Unit*) di laptop dan smartphone kita, hingga produk konsumen nyata seperti ChatGPT, Claude, dan DeepSeek.

### Wawasan Tambahan untuk Memperkaya Sudut Pandang Anda:
Meskipun peluang terjadinya "Musim Dingin Beku" (di mana riset AI mati total) sangat kecil, di kalangan para ahli saat ini muncul istilah **"AI Autumn" (Musim Gugur AI)** atau **fase koreksi realitas**. 

Maksudnya apa? Pasar saat ini sedang menguji apakah pengeluaran ratusan triliun rupiah untuk membangun pusat data dan membeli chip benar-benar sebanding dengan pendapatan bisnis yang dihasilkan. Jika nanti ada perlambatan investasi, itu bukan karena teknologinya gagal, melainkan proses penyesuaian ekonomi yang wajar sebelum AI menjadi kebutuhan sehari-hari seperti halnya listrik dan internet.

Sekarang, mari kita masuk ke materi Pelajaran 3: **sebuah topik yang membedakan programmer biasa dengan praktisi data profesional sejati.**

---

## 2. Mengapa Belajar Etika Sebelum Menulis Kode?

Banyak pemula mengira bahwa belajar Machine Learning hanyalah soal rumus matematika, menulis kode Python, dan mencari akurasi setinggi-tingginya. 

Namun, ada satu fakta penting yang sering dilupakan: **Machine Learning belajar dari data masa lalu manusia.**
* Jika data masa lalu kita bersih, adil, dan objektif, maka model AI yang dihasilkan akan bijak.
* Namun, jika data masa lalu kita menyimpan prasangka, ketimpangan sosial, atau ketidakadilan sejarah, maka komputer akan menganggap ketidakadilan itu sebagai **"aturan baku yang benar"**.

Prinsip terkenalnya adalah: **"Bias In, Bias Out."**

Komputer tidak tahu moral. Komputer hanya mencari pola statistik. Jika tidak diawasi dengan hati-hati, algoritma kita bisa secara tidak sengaja merugikan ribuan bahkan jutaan orang.

---

## 3. Cerita Nyata di Industri yang Mengguncang Dunia

Agar Anda mendapat gambaran nyata, mari kita lihat tiga peristiwa nyata yang pernah terjadi di perusahaan teknologi dunia:

### Kasus 1: AI Rekrutmen Karyawan Amazon (2018)
Amazon pernah membangun sistem Machine Learning untuk menyortir ribuan surat lamaran kerja insinyur perangkat lunak secara otomatis. Tujuannya baik: mempermudah perekrutan talenta terbaik.

Apa yang terjadi? Sistem tersebut secara sistematis **mendiskriminasi pelamar perempuan**. Setiap kali menemukan kata "wanita" (misalnya: "ketua klub catur wanita" atau nama universitas khusus perempuan), sistem langsung memotong skor kandidat tersebut.

**Mengapa ini bisa terjadi?**  
Karena data yang dipakai untuk melatih AI adalah data pelamar 10 tahun ke belakang. Dalam 10 tahun tersebut, industri teknologi didominasi oleh laki-laki. Akibatnya, komputer "menyimpulkan sendiri" pola keliru: *"Oh, pelamar laki-laki lebih sukses di masa lalu, berarti laki-laki adalah kandidat yang lebih unggul."*

Menyadari hal ini berbahaya dan diskriminatif, Amazon akhirnya mematikan proyek tersebut secara total.

---

### Kasus 2: Dispenser Sabun Otomatis dan Deteksi Wajah
Pernah viral sebuah video di mana dispenser sabun otomatis di toilet umum langsung mengeluarkan sabun saat didekati oleh tangan berkulit cerah, tetapi sama sekali tidak merespons ketika didekati oleh tangan berkulit gelap.

Kasus serupa terjadi pada teknologi pengenalan wajah: seorang peneliti MIT berkulit gelap bernama Joy Buolamwini menemukan bahwa kamera AI di laboratoriumnya baru bisa mengenali dirinya setelah ia mengenakan topeng putih di wajahnya.

**Mengapa ini bisa terjadi?**  
Bukan karena pembuatnya rasis dengan sengaja, melainkan karena **kelalaian saat mengumpulkan data**. Para insinyur yang melatih sistem tersebut mayoritas hanya menggunakan foto wajah diri mereka sendiri dan rekan sekantor yang berkulit cerah. Data latihnya kekurangan variasi warna kulit manusia di dunia nyata.

---

### Kasus 3: Stereotip Gender pada Mesin Penerjemah Bahasa
Beberapa bahasa di dunia (seperti Bahasa Turki) tidak memiliki pembeda kata ganti gender pria/wanita (semuanya menggunakan kata "O").

Ketika kalimat diterjemahkan ke Bahasa Inggris:
* *"O bir doktor"* diterjemahkan menjadi: *"He is a doctor"* (Dia pria adalah dokter).
* *"O bir hemşire"* diterjemahkan menjadi: *"She is a nurse"* (Dia wanita adalah perawat).

Algoritma penerjemah otomatis mengadopsi stereotip pekerjaan berdasarkan frekuensi tulisan-tulisan lama yang ada di internet, di mana kata dokter lebih sering berdampingan dengan pria, dan perawat lebih sering berdampingan dengan wanita.

---

## 4. Lima Bentuk Kerugian Akibat AI yang Bias (Harms in AI)

Para peneliti di Microsoft mengelompokkan dampak buruk bias AI ke dalam lima kategori:

1. **Ketimpangan Alokasi Kesempatan (Allocation Harm)**  
   Ketika sistem menahan atau menolak hak seseorang secara tidak adil. Contoh: AI penilai kelayakan kredit bank yang mempersulit pinjaman untuk kelompok etnis tertentu, atau AI rekrutmen kerja seperti kasus Amazon.

2. **Kualitas Layanan yang Timpang (Quality of Service Harm)**  
   Teknologi bekerja sangat sempurna untuk sebagian orang, tetapi buruk bagi kelompok lain. Contoh: sistem pengenal suara di mobil yang sangat peka terhadap suara pria, tetapi sering gagal memahami instruksi suara wanita atau aksen daerah.

3. **Pelecehan dan Pelabelan Merendahkan (Denigration Harm)**  
   Sistem mengklasifikasikan manusia ke kategori yang ofensif. Contoh: algoritma penanda foto otomatis yang pernah keliru melabeli foto orang Afrika-Amerika dengan label hewan.

4. **Penguatan Stereotip (Stereotyping Harm)**  
   Menggeneralisasi sifat atau profesi seseorang berdasarkan kelompoknya, seperti contoh mesin penerjemah tadi.

5. **Keterwakilan yang Berat Sebelah (Under-representation Harm)**  
   Kelompok minoritas atau budaya tertentu sama sekali tidak hadir dalam hasil pencarian atau rekomendasi sistem karena datanya tidak pernah dimasukkan.

---

## 5. Enam Prinsip Responsible AI dari Microsoft

Untuk mencegah bahaya di atas, Microsoft merumuskan enam pilar utama yang wajib dipegang setiap pembuat AI:

```
                  ┌──────────────────────┐
                  │    RESPONSIBLE AI    │
                  └──────────┬───────────┘
         ┌─────────────┬─────┴─────┬─────────────┐
         ▼             ▼           ▼             ▼
   [ Keadilan ]  [ Keandalan ]  [ Privasi ]  [ Inklusif ]
     Fairness       Safety       Security    Inclusive
                       │           │
                       ▼           ▼
               [ Transparansi ] [ Tanggung Jawab ]
                 Transparency    Accountability
```

1. **Fairness (Keadilan):** Sistem harus memperlakukan semua orang yang memiliki kualifikasi serupa dengan perlakuan yang sama.
2. **Reliability & Safety (Keandalan & Keamanan):** Sistem harus aman dan bekerja konsisten dalam situasi tak terduga (contoh: mobil otonom yang harus tetap aman di cuaca badai).
3. **Privacy & Security (Privasi):** Data pribadi pengguna tidak boleh bocor atau disalahgunakan.
4. **Inclusiveness (Inklusivitas):** Sistem dirancang agar dapat diakses oleh semua lapisan masyarakat, termasuk penyandang disabilitas.
5. **Transparency (Transparansi):** Model tidak boleh seperti "kotak hitam misterius". Pengguna berhak tahu mengapa sebuah keputusan diambil (misalnya: jika pengajuan pinjaman ditolak, sistem harus bisa menjelaskan alasannya).
6. **Accountability (Tanggung Jawab):** Yang bertanggung jawab atas kesalahan sistem adalah **manusia yang membuatnya**, bukan menyalahkan "komputernya yang salah".

---

## 6. Sesi Brainstorming: Dilema Etika di Meja Anda

Bayangkan Anda sekarang adalah seorang Kepala Data Science di sebuah bank terkemuka. 

Tim Anda baru saja membuat model Machine Learning untuk menentukan siapa yang berhak mendapatkan pinjaman modal usaha. Hasil pengujian menunjukkan akurasi model sangat tinggi (97%).

Namun, saat Anda memeriksa perilakunya lebih dalam, Anda menemukan bahwa model tersebut **selalu memberikan skor rendah dan menolak pelamar yang berasal dari kode pos (wilayah) perkampungan miskin**, meskipun ada pengusaha di wilayah tersebut yang memiliki catatan keuangan sangat rapi dan usaha yang sukses.

Model beralasan: *"Berdasarkan data historis 20 tahun terakhir, 70% kredit macet terjadi di kode pos wilayah tersebut."*

### Pertanyaan Diskusi Kita:
1. Menurut pandangan Anda, apakah model ini adil (*fair*) bagi pengusaha jujur yang tinggal di wilayah tersebut?
2. Sebagai pemimpin tim, langkah apa yang akan Anda ambil untuk memperbaiki masalah ini? Apakah menghapus data "kode pos" dari daftar variabel sudah cukup menyelesaikan masalah?

Pikirkan sejenak, lalu ceritakan sudut pandang Anda!
