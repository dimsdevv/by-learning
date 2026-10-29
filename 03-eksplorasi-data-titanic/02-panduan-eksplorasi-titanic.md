# Panduan Belajar Mandiri: Mengungkap Misteri Tragedi Kapal Titanic 🚢

> **Pesan Dosen:**  
> "Saya sangat bangga dengan prinsip Anda: *'Jangan Anda yang mengeksekusi, biar saya sendiri yang belajar'*. Inilah mentalitas sejati seorang calon Data Scientist. Tangan yang mengetik sendiri dan mata yang melihat sendiri error di terminal adalah cara tercepat untuk mahir. Saya hanya bertindak sebagai pemandu di samping Anda."

File data Titanic sudah tersedia di komputer Anda pada lokasi:  
📁 `data/titanic.csv` (berada di folder utama `d:\BY LEARNING\data\titanic.csv`)

> 💡 **Tips Jalur File Aman di Python:**  
> Karena Anda meletakkan script di dalam sub-folder `PYTHON-LEARNING/HARI-KE1`, gunakan kode pembaca file berikut di semua file script Anda agar tidak pernah terkena `FileNotFoundError`:
> ```python
> import os
> import pandas as pd
> 
> jalur_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'titanic.csv')
> df = pd.read_csv(jalur_file)
> ```

---

## 1. Cerita di Balik Data (The Story of Titanic)

Pada malam 14 April 1912, kapal penumpang termewah dan terbesar di dunia saat itu, **RMS Titanic**, menabrak gunung es di Samudra Atlantik Utara dalam pelayaran perdananya menuju New York.

Hanya dalam waktu kurang dari 3 jam, kapal tersebut karam. Dari sekitar 2.224 penumpang dan awak kapal, lebih dari 1.500 orang tewas.

Tragedi ini menjadi salah satu studi kasus paling terkenal di dunia sains data karena sebuah fakta kelam: **kapal tersebut hanya membawa 20 sekoci penyelamat**, yang kapasitasnya hanya cukup untuk sekitar separuh dari total manusia di atas kapal.

Ketika kepanikan melanda di tengah malam yang gelap gulita dan suhu air minus 2 derajat Celsius, muncullah protokol penyelamatan legendaris dari Kapten Edward Smith:
> *"Women and children first!" (Wanita dan anak-anak didahulukan!)*

### Pertanyaan Penyelidikan Data Kita:
Sebagai seorang analis data, tugas Anda adalah menguji apakah protokol kemanusiaan itu benar-benar terjadi di lapangan melalui bukti angka:
1. **Apakah jenis kelamin benar-benar menjadi faktor penentu utama keselamatan?**
2. **Apakah status sosial dan kekayaan (penumpang Kelas 1 vs Kelas 3) memengaruhi kesempatan seseorang mendapatkan sekoci?**
3. **Berapa usia penumpang termuda yang selamat dan tertua yang menjadi korban?**

---

## 2. Kamus Data (Memahami Arti Setiap Kolom)

Buka mata Anda seperti seorang detektif. Tabel `titanic.csv` memiliki 12 kolom penting:

| Nama Kolom | Arti dalam Bahasa Indonesia | Keterangan Nilai |
| :--- | :--- | :--- |
| **`PassengerId`** | Nomor Urut Penumpang | 1, 2, 3, ... |
| **`Survived`** | Status Keselamatan | **`0` = Meninggal**, **`1` = Selamat** |
| **`Pclass`** | Kelas Tiket Kapal | **`1`** (Kelas Atas/Kaya), **`2`** (Menengah), **`3`** (Ekonomi) |
| **`Name`** | Nama Lengkap Penumpang | Teks nama lengkap |
| **`Sex`** | Jenis Kelamin | `male` (Pria), `female` (Wanita) |
| **`Age`** | Usia Penumpang | Angka usia dalam tahun |
| **`SibSp`** | Saudara / Pasangan | Jumlah saudara kandung atau suami/istri yang ikut |
| **`Parch`** | Orang Tua / Anak | Jumlah orang tua atau anak yang ikut di kapal |
| **`Ticket`** | Nomor Tiket | Kode tiket |
| **`Fare`** | Tarif Tiket | Harga tiket dalam poundsterling zaman itu |
| **`Cabin`** | Nomor Kamar / Kabin | Huruf dan nomor kamar (misal: C85) |
| **`Embarked`** | Pelabuhan Naik Kapal | `C` (Cherbourg), `Q` (Queenstown), `S` (Southampton) |

---

## 3. Langkah 1: Berkenalan dengan Data (`step1_titanic.py`)
Membuka tabel, melihat jumlah baris, dan menghitung persentase selamat secara umum.

---

## 4. Langkah 2: Menguji Hipotesis Gender (`step2_titanic.py`)
Membuktikan aturan *"Women First"* menggunakan `groupby('Sex')`.

---

## 5. Langkah 3: Menguji Pengaruh Kelas Sosial (`step3_titanic.py`)
Membuktikan apakah uang dan kelas tiket memengaruhi peluang bertahan hidup.

```python
import pandas as pd
import os

jalur_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'titanic.csv')
df = pd.read_csv(jalur_file)

print("=" * 60)
print("ANALISIS KESELAMATAN BERDASARKAN KELAS TIKET (PCLASS)")
print("=" * 60)

# Mengelompokkan berdasarkan kelas tiket (1, 2, 3)
tabel_kelas = df.groupby('Pclass')['Survived'].agg(
    Total_Penumpang='count',
    Jumlah_Selamat='sum',
    Persentase_Selamat=lambda x: f"{(x.mean() * 100):.1f}%"
)

# Mengganti angka 1, 2, 3 menjadi teks agar lebih mudah dibaca
tabel_kelas.index = ['Kelas 1 (Kaya/VVIP)', 'Kelas 2 (Menengah)', 'Kelas 3 (Ekonomi)']

print(tabel_kelas)
print("=" * 60)
```

---

## 6. Langkah 4: Membuat Grafik Visualisasi Data (`step4_titanic.py`)

Mengubah tabel angka menjadi gambar grafik visual berwarna yang siap dipresentasikan.

### Kode Program Lengkap:
```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Membaca data dengan jalur aman
jalur_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'titanic.csv')
df = pd.read_csv(jalur_file)

# Menghitung persentase selamat
persen_gender = df.groupby('Sex')['Survived'].mean() * 100
persen_kelas = df.groupby('Pclass')['Survived'].mean() * 100

# Membuat kanvas gambar berisi 2 grafik berdampingan
plt.figure(figsize=(12, 5))

# Grafik 1: Berdasarkan Gender
plt.subplot(1, 2, 1)
warna_gender = ['#e75480', '#2b580c'] # Pink untuk wanita, Hijau untuk pria
bars1 = plt.bar(['Wanita (Female)', 'Pria (Male)'], persen_gender, color=warna_gender, width=0.5)
plt.title('Tingkat Keselamatan Berdasarkan Gender', fontsize=12, fontweight='bold')
plt.ylabel('Persentase Selamat (%)')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Menuliskan angka persentase di atas batang
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.15, yval + 2, f"{yval:.1f}%", fontweight='bold')

# Grafik 2: Berdasarkan Kelas Tiket
plt.subplot(1, 2, 2)
warna_kelas = ['#ffd700', '#c0c0c0', '#cd7f32'] # Emas, Perak, Perunggu
bars2 = plt.bar(['Kelas 1', 'Kelas 2', 'Kelas 3'], persen_kelas, color=warna_kelas, width=0.5)
plt.title('Tingkat Keselamatan Berdasarkan Kelas Tiket', fontsize=12, fontweight='bold')
plt.ylabel('Persentase Selamat (%)')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + 0.15, yval + 2, f"{yval:.1f}%", fontweight='bold')

plt.tight_layout()

# Menyimpan grafik sebagai file gambar di folder yang sama
nama_gambar = os.path.join(os.path.dirname(__file__), 'grafik_analisis_titanic.png')
plt.savefig(nama_gambar, dpi=150)
print(f"Grafik berhasil digambar dan disimpan sebagai: {nama_gambar}")
```

### Jalankan di Terminal Anda:
```bash
python step4_titanic.py
```
