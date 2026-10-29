import pandas as pd
import os

# Membaca data menggunakan jalur file yang aman
jalur_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'titanic.csv')
df = pd.read_csv(jalur_file)

print("=" * 60)
print("ANALISIS KESELAMATAN BERDASARKAN JENIS KELAMIN")
print("=" * 60)

# Menghitung persentase selamat per jenis kelamin
tabel_gender = df.groupby('Sex')['Survived'].agg(
    Total_Penumpang='count',
    Jumlah_Selamat='sum',
    Persentase_Selamat=lambda x: f"{(x.mean() * 100):.1f}%"
)

print(tabel_gender)
print("=" * 60)