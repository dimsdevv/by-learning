"""
VISUALISASI AESTHETIC DATA TITANIC - HIGH PRECISION DASHBOARD (VERSI FINAL)
Dirancang dengan presisi tata letak mutlak, margin lapang, tanpa tabrakan komponen.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ── 1. MEMBACA DATASET ─────────────────────────────────────────────
jalur_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'titanic.csv')
df = pd.read_csv(jalur_file)

# ── 2. PALET WARNA PROFESIONAL & ELEGAN ─────────────────────────────
BG_COLOR      = '#0b0e14'   # Sangat gelap & elegan
CARD_BG       = '#151922'   # Latar belakang panel grafik
BORDER_COLOR  = '#262c38'   # Garis batas halus
TEXT_TITLE    = '#f0f4f8'   # Putih bersih
TEXT_BODY     = '#d0d7de'   # Teks isi kontras
TEXT_MUTED    = '#8b949e'   # Abu-abu redup

CYAN_ACCENT   = '#20c997'   # Selamat / Positif
RED_ACCENT    = '#ff6b6b'   # Meninggal / Bahaya
GOLD_ACCENT   = '#fcc419'   # Kelas 1 (VVIP)
SILVER_ACCENT = '#adb5bd'   # Kelas 2 (Menengah)
BRONZE_ACCENT = '#e67700'   # Kelas 3 (Ekonomi)
PINK_ACCENT   = '#f06595'   # Wanita
BLUE_ACCENT   = '#339af0'   # Pria

# ── 3. KONFIGURASI GLOBAL MATPLOTLIB ───────────────────────────────
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'DejaVu Sans', 'Arial'],
    'figure.facecolor': BG_COLOR,
    'axes.facecolor': CARD_BG,
    'axes.edgecolor': BORDER_COLOR,
    'axes.linewidth': 1.0,
    'axes.labelcolor': TEXT_BODY,
    'text.color': TEXT_BODY,
    'xtick.color': TEXT_MUTED,
    'ytick.color': TEXT_MUTED,
    'grid.color': BORDER_COLOR,
    'grid.alpha': 0.4,
    'grid.linestyle': ':',
    'font.size': 10,
})

# ── 4. MEMBUAT CANVAS DENGAN GRIDSPEC PRESISI ──────────────────────
fig = plt.figure(figsize=(18, 11), dpi=220)

# Header Utama (dengan posisi vertikal aman yang tidak menyentuh panel)
fig.text(0.5, 0.955, 'RMS TITANIC : EXECUTIVE SUMMARY',
         ha='center', va='center', fontsize=22, fontweight='bold',
         color=TEXT_TITLE)
fig.text(0.5, 0.925, 'Investigasi Data dan Pola Keselamatan Penumpang Tragedi 14 April 1912',
         ha='center', va='center', fontsize=11, color=TEXT_MUTED)

# Tata Letak Grid: Jarak atas top=0.84 memberikan ruang bernapas lega di bawah header
gs = gridspec.GridSpec(
    2, 3,
    figure=fig,
    left=0.07, right=0.94,
    bottom=0.07, top=0.84,
    wspace=0.30, hspace=0.36
)

# ═════════════════════════════════════════════════════════════════════
# PANEL 1: DONUT CHART - RASIO KESELAMATAN TOTAL
# ═════════════════════════════════════════════════════════════════════
ax1 = fig.add_subplot(gs[0, 0])
ax1.axis('off')  # Hilangkan garis tepi kotak agar donut bersih melayang

selamat = int(df['Survived'].sum())
meninggal = int(len(df) - selamat)
sizes = [selamat, meninggal]
colors_pie = [CYAN_ACCENT, RED_ACCENT]

wedges, texts, autotexts = ax1.pie(
    sizes,
    explode=(0.04, 0.04),
    colors=colors_pie,
    autopct='%1.1f%%',
    pctdistance=0.74,
    startangle=140,
    wedgeprops=dict(width=0.42, edgecolor=BG_COLOR, linewidth=2.5)
)

for t in autotexts:
    t.set_fontsize(11)
    t.set_fontweight('bold')
    t.set_color(BG_COLOR)

# Teks di tengah Donut
ax1.text(0, 0.09, f"{selamat}", ha='center', va='center',
         fontsize=18, fontweight='bold', color=CYAN_ACCENT)
ax1.text(0, -0.11, "Selamat", ha='center', va='center',
         fontsize=10, color=TEXT_MUTED)

ax1.set_title("1. Rasio Keselamatan Penumpang", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

legend_labels = [f"Selamat ({selamat})", f"Meninggal ({meninggal})"]
ax1.legend(wedges, legend_labels, loc='lower center', bbox_to_anchor=(0.5, -0.10),
           frameon=False, ncol=2, fontsize=9, labelcolor=TEXT_BODY)

# ═════════════════════════════════════════════════════════════════════
# PANEL 2: BAR HORIZONTAL - TINGKAT SELAMAT PER GENDER
# ═════════════════════════════════════════════════════════════════════
ax2 = fig.add_subplot(gs[0, 1])

gender_pct = df.groupby('Sex')['Survived'].mean() * 100
categories = ['Wanita', 'Pria']
values = [gender_pct['female'], gender_pct['male']]
bar_colors = [PINK_ACCENT, BLUE_ACCENT]

y_positions = np.array([1, 0])
bars2 = ax2.barh(y_positions, values, height=0.42, color=bar_colors, edgecolor='none')

for bar, val in zip(bars2, values):
    ax2.text(val + 2, bar.get_y() + bar.get_height()/2,
             f"{val:.1f}%", va='center', fontsize=11, fontweight='bold', color=TEXT_TITLE)

ax2.set_yticks(y_positions)
ax2.set_yticklabels(categories, fontsize=11, fontweight='bold')
ax2.set_xlim(0, 95)
ax2.set_xlabel("% Tingkat Selamat", fontsize=9, color=TEXT_MUTED)
ax2.set_title("2. Prioritas 'Wanita & Anak'", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

ax2.xaxis.grid(True)
ax2.yaxis.grid(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# ═════════════════════════════════════════════════════════════════════
# PANEL 3: BAR VERTIKAL - KESELAMATAN PER KELAS TIKET
# ═════════════════════════════════════════════════════════════════════
ax3 = fig.add_subplot(gs[0, 2])

class_pct = df.groupby('Pclass')['Survived'].mean() * 100
class_labels = ['Kelas 1\n(VVIP)', 'Kelas 2\n(Bisnis)', 'Kelas 3\n(Ekonomi)']
class_vals = [class_pct[1], class_pct[2], class_pct[3]]
class_colors = [GOLD_ACCENT, SILVER_ACCENT, BRONZE_ACCENT]

bars3 = ax3.bar(class_labels, class_vals, width=0.48, color=class_colors, edgecolor='none')

for bar, val in zip(bars3, class_vals):
    ax3.text(bar.get_x() + bar.get_width()/2, val + 2.5,
             f"{val:.1f}%", ha='center', va='bottom', fontsize=11,
             fontweight='bold', color=TEXT_TITLE)

ax3.set_ylim(0, 75)
ax3.set_ylabel("% Tingkat Selamat", fontsize=9, color=TEXT_MUTED)
ax3.set_title("3. Tingkat Selamat per Kelas Tiket", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

ax3.yaxis.grid(True)
ax3.xaxis.grid(False)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# ═════════════════════════════════════════════════════════════════════
# PANEL 4: HISTOGRAM - DISTRIBUSI USIA
# ═════════════════════════════════════════════════════════════════════
ax4 = fig.add_subplot(gs[1, 0])

usia_meninggal = df[df['Survived'] == 0]['Age'].dropna()
usia_selamat = df[df['Survived'] == 1]['Age'].dropna()

bins = np.arange(0, 75, 4)
ax4.hist(usia_meninggal, bins=bins, color=RED_ACCENT, alpha=0.65,
         label='Meninggal', edgecolor=BG_COLOR, linewidth=0.8)
ax4.hist(usia_selamat, bins=bins, color=CYAN_ACCENT, alpha=0.75,
         label='Selamat', edgecolor=BG_COLOR, linewidth=0.8)

ax4.set_ylim(0, 26)  # Ruang vertikal lega agar legend tidak menabrak bar
ax4.set_xlabel("Rentang Usia (Tahun)", fontsize=9, color=TEXT_MUTED)
ax4.set_ylabel("Jumlah Penumpang", fontsize=9, color=TEXT_MUTED)
ax4.set_title("4. Distribusi Usia Penumpang", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

ax4.legend(loc='upper right', frameon=False, fontsize=9, labelcolor=TEXT_BODY)
ax4.yaxis.grid(True)
ax4.xaxis.grid(False)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

# ═════════════════════════════════════════════════════════════════════
# PANEL 5: BAR TERKELOMPOK - GENDER X KELAS TIKET
# ═════════════════════════════════════════════════════════════════════
ax5 = fig.add_subplot(gs[1, 1])

grouped = df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100
x = np.arange(3)
width = 0.30

fem_vals = [grouped.get((1, 'female'), 0), grouped.get((2, 'female'), 0), grouped.get((3, 'female'), 0)]
male_vals = [grouped.get((1, 'male'), 0), grouped.get((2, 'male'), 0), grouped.get((3, 'male'), 0)]

bars_fem = ax5.bar(x - width/2, fem_vals, width, label='Wanita', color=PINK_ACCENT, edgecolor='none')
bars_male = ax5.bar(x + width/2, male_vals, width, label='Pria', color=BLUE_ACCENT, edgecolor='none')

for bar in bars_fem:
    h = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2, h + 2.5,
             f"{h:.0f}%", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=PINK_ACCENT)

for bar in bars_male:
    h = bar.get_height()
    ax5.text(bar.get_x() + bar.get_width()/2, h + 2.5,
             f"{h:.0f}%", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color=BLUE_ACCENT)

ax5.set_xticks(x)
ax5.set_xticklabels(['Kelas 1', 'Kelas 2', 'Kelas 3'], fontsize=10)
ax5.set_ylim(0, 115)  # Headroom lapang untuk teks 94%
ax5.set_ylabel("% Tingkat Selamat", fontsize=9, color=TEXT_MUTED)
ax5.set_title("5. Kombinasi Gender & Kasta", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

ax5.legend(loc='upper right', frameon=False, fontsize=9, labelcolor=TEXT_BODY)
ax5.yaxis.grid(True)
ax5.xaxis.grid(False)
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)

# ═════════════════════════════════════════════════════════════════════
# PANEL 6: RATA-RATA HARGA TIKET (BERSIH & INFORMATIF)
# ═════════════════════════════════════════════════════════════════════
ax6 = fig.add_subplot(gs[1, 2])

fare_mean = df.groupby('Survived')['Fare'].mean()
fare_median = df.groupby('Survived')['Fare'].median()

labels_fare = ['Meninggal', 'Selamat']
vals_mean = [fare_mean[0], fare_mean[1]]
vals_median = [fare_median[0], fare_median[1]]
colors_fare = [RED_ACCENT, CYAN_ACCENT]

x_f = np.arange(2)
w_f = 0.40

bars_f = ax6.bar(x_f, vals_mean, width=w_f, color=colors_fare, edgecolor='none')

for bar, val in zip(bars_f, vals_mean):
    ax6.text(bar.get_x() + bar.get_width()/2, val + 1.8,
             f"£{val:.1f}", ha='center', va='bottom', fontsize=11, fontweight='bold', color=TEXT_TITLE)

ax6.text(0, vals_mean[0]/2, f"Median: £{vals_median[0]:.1f}", ha='center', va='center',
         fontsize=9, fontweight='bold', color=BG_COLOR)
ax6.text(1, vals_mean[1]/2, f"Median: £{vals_median[1]:.1f}", ha='center', va='center',
         fontsize=9, fontweight='bold', color=BG_COLOR)

ax6.set_xticks(x_f)
ax6.set_xticklabels(labels_fare, fontsize=10, fontweight='bold')
ax6.set_ylim(0, 62)
ax6.set_ylabel("Rata-rata Tarif (Pound)", fontsize=9, color=TEXT_MUTED)
ax6.set_title("6. Pengaruh Daya Beli / Tarif Tiket", fontsize=12, fontweight='bold',
              color=TEXT_TITLE, pad=15)

ax6.yaxis.grid(True)
ax6.xaxis.grid(False)
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)

# ── 5. FOOTER ──────────────────────────────────────────────────────
fig.text(0.5, 0.025,
         'Sumber Data: Titanic Dataset  |  Desain Sistem: Bento Grid Dark Theme  |  Dibuat dengan Python & Matplotlib',
         ha='center', va='center', fontsize=8.5, color=TEXT_MUTED)

# ── 6. MENYIMPAN HASIL GAMBAR ──────────────────────────────────────
output_path = os.path.join(os.path.dirname(__file__), 'dashboard_titanic.png')
plt.savefig(output_path, dpi=220, facecolor=BG_COLOR, edgecolor='none')
plt.close(fig)

print(f"Berhasil merender dashboard presisi: {output_path}")
