import pandas as pd
import os

# Membaca data menggunakan jalur file yang aman
jalur_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'titanic.csv')
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