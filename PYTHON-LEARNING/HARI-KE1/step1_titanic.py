import pandas as pd

print("="*60)
print("MEMBUKA DAN MENGECEK DATA PENUMPANG TITANIC")
print("="*60)

# MEMBACA FILE DATA CSV (Menggunakan jalur relatif yang aman)
import os
jalur_file = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'titanic.csv')
df = pd.read_csv(jalur_file)

# Melihat jumlah baris dan kolom
jumlah_baris, jumlah_kolom = df.shape
print(f"Total penumpang yang tercatat: {jumlah_baris} orang")
print(f"Total kolom informasi: {jumlah_kolom} kolom\n")

# Menampilkan 5 penumpang teratas
print("Berikut contoh data 5 penumpang pertama:")
print(df[['PassengerId', 'Name', 'Sex', 'Age', 'Pclass', 'Survived']].head())

# MENGHITUNG TOTAL YANG SELAMAT VS MENINGGAL
total_selamat = df['Survived'].sum()
persen_selamat = (total_selamat / jumlah_baris) * 100

print("\n" + "=" * 60)
print(f"Total penumpang yang selamat : {total_selamat} orang")
print(f"Total yang meninggal dunia   : {jumlah_baris - total_selamat} orang")
print(f"Tingkat keselamatan umum     : {persen_selamat:.1f}%")
print("=" * 60)