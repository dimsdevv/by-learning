"""
PRAKTIK MACHINE LEARNING PERTAMA: REGRESI LINIER HARGA LABU 🎃
Kurikulum: Microsoft ML for Beginners (Modul 2: Regression)

Tujuan:
Membangun model Machine Learning untuk memprediksi harga rata-rata labu
berdasarkan waktu panen (hari dalam setahun).
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

print("=" * 60)
print("1. MEMBACA DAN MEMERIKSA DATASET")
print("=" * 60)

# Membaca data mentah
df = pd.read_csv('data/US-pumpkins.csv')
print(f"Total baris data awal: {len(df)} baris")

# -------------------------------------------------------------
# 2. PEMBERSIHAN DATA (DATA CLEANING)
# -------------------------------------------------------------
# Kita hanya memilih baris yang satuannya 'bushel' agar perbandingannya adil.
# Di Amerika, labu sering dijual per bushel (keranjang standar).
df = df[df['Package'].str.contains('bushel', na=False, case=False)]
print(f"Baris setelah disaring hanya kemasan bushel: {len(df)} baris")

# Menghitung harga rata-rata dari kolom Low Price dan High Price
df['Price'] = (df['Low Price'] + df['High Price']) / 2

# Mengubah tanggal menjadi format datetime, lalu mengambil hari dalam setahun (Day of Year)
# Contoh: 1 Februari = hari ke-32 dalam setahun
df['Date'] = pd.to_datetime(df['Date'])
df['DayOfYear'] = df['Date'].dt.dayofyear
df['Month'] = df['Date'].dt.month

# Memilih hanya kolom penting yang bersih
clean_df = df[['DayOfYear', 'Month', 'Price']].dropna()

print("\nContoh 5 baris data yang sudah bersih:")
print(clean_df.head())

# -------------------------------------------------------------
# 3. MEMBAGI DATA UNTUK LATIHAN DAN UJIAN (TRAIN - TEST SPLIT)
# -------------------------------------------------------------
# X = Variabel masukan (Fitur): Hari dalam setahun (DayOfYear)
# y = Variabel target yang ingin ditebak: Harga (Price)
X = clean_df[['DayOfYear']]
y = clean_df['Price']

# 80% data untuk melatih model, 20% data disimpan untuk menguji kecerdasan model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\n" + "=" * 60)
print("2. MELATIH MODEL MACHINE LEARNING (TRAINING)")
print("=" * 60)

# Membuat objek model Regresi Linier
model = LinearRegression()

# Membiarkan model mempelajari hubungan antara X (hari) dan y (harga)
model.fit(X_train, y_train)

# Mendapatkan kemiringan garis (slope/koefisien) dan titik potong (intercept)
print("Model berhasil dilatih!")
print(f"Kemiringan garis (Koefisien): {model.coef_[0]:.4f}")
print(f"Titik potong garis (Intercept): {model.intercept_:.4f}")

# -------------------------------------------------------------
# 4. MENGUJI KECERDASAN MODEL (EVALUATION)
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("3. EVALUASI HASIL TEBAKAN MODEL")
print("=" * 60)

# Meminta model menebak harga dari data ujian (X_test)
y_pred = model.predict(X_test)

# Menghitung seberapa dekat tebakan model dengan kenyataan
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Rata-rata kesalahan kuadrat (MSE): {mse:.2f}")
print(f"Skor R-squared (R2 Score): {r2:.4f}")

# -------------------------------------------------------------
# 5. MENCOBA PREDIKSI NYATA
# -------------------------------------------------------------
print("\n" + "=" * 60)
print("4. SIMULASI TEBAKAN NYATA")
print("=" * 60)
# Misalnya hari ke-260 (sekitar pertengahan September)
hari_contoh = [[260]]
harga_tebakan = model.predict(hari_contoh)
print(f"Jika panen terjadi pada hari ke-260 (September), perkiraan harga labu: ${harga_tebakan[0]:.2f}")

# -------------------------------------------------------------
# 6. MEMBUAT GRAFIK VISUALISASI HASIL
# -------------------------------------------------------------
plt.figure(figsize=(9, 5))

# Titik-titik data asli
plt.scatter(X_test, y_test, color='black', alpha=0.5, label='Data Asli Penjualan')

# Garis lurus merah yang dibuat oleh Machine Learning kita
plt.plot(X_test, y_pred, color='red', linewidth=2.5, label='Garis Prediksi Machine Learning')

plt.title('Regresi Linier: Hubungan Hari Panen Terhadap Harga Labu 🎃', fontsize=12, fontweight='bold')
plt.xlabel('Hari dalam Setahun (Day of Year)', fontsize=10)
plt.ylabel('Harga Labu ($ per Bushel)', fontsize=10)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Simpan grafik ke dalam file gambar
grafik_path = 'grafik_prediksi_labu.png'
plt.savefig(grafik_path, dpi=150, bbox_inches='tight')
print(f"\nGrafik hasil visualisasi berhasil disimpan sebagai: '{grafik_path}'")
print("=" * 60)
