# ==============================================
# Laporan Harian Kopi Senja v1.0
# Penulis: Raka (dan kamu!)
#
# Jalankan dari terminal:
#   python3 laporan.py      (Mac/Linux)
#   python laporan.py       (Windows)
# ==============================================

# --- 1. Konstanta: nilai yang nggak berubah ---           (Bab 4)
NAMA_TOKO = "Kopi Senja"
TARGET_HARIAN = 10_000_000
JAM_OPERASIONAL = (7, 22)                                 # (Bab 7: tuple)

# --- 2. Input dari orang yang menjalankan script ---      (Bab 8 + Bab 6)
nama_analis = input("Nama analis: ").strip().title()
tanggal = input("Tanggal laporan (DD-MM-YYYY): ").strip()

# --- 3. Data hari ini (ceritanya hasil download kasir) --- (Bab 7: list)
cabang = ["Jakarta", "Bandung", "Surabaya"]
omzet = [4_250_000, 2_875_000, 3_520_000]
transaksi = [170, 125, 160]
menu_terlaris_mentah = "   es KOPI susu gula AREN  "
kode_trx_terakhir = "TRX-20261005-JKT-0170"

# --- 4. Olah data ---                                      (Bab 5)
total_omzet = sum(omzet)
total_transaksi = sum(transaksi)
rata_rata = round(total_omzet / total_transaksi)
selisih = max(omzet) - min(omzet)
persen_target = total_omzet / TARGET_HARIAN * 100
target_tercapai = total_omzet >= TARGET_HARIAN

menu_terlaris = menu_terlaris_mentah.strip().title()      # (Bab 6)
kode_cabang = kode_trx_terakhir[13:16]
nomor_trx = int(kode_trx_terakhir[-4:])

# --- 5. Cetak laporan ---                                  (Bab 8)
garis = "=" * 44
garis_tipis = "-" * 44

print(garis)
print(f"LAPORAN HARIAN {NAMA_TOKO.upper()}".center(44))
print(garis)
print(f"Tanggal          : {tanggal}")
print(f"Analis           : {nama_analis}")
print(f"Jam operasional  : {JAM_OPERASIONAL[0]}.00 - {JAM_OPERASIONAL[1]}.00")
print(garis_tipis)
print("Omzet per cabang")
print(f"  {cabang[0]}\t: Rp{omzet[0]:,} ({transaksi[0]} trx)".replace(",", "."))
print(f"  {cabang[1]}\t: Rp{omzet[1]:,} ({transaksi[1]} trx)".replace(",", "."))
print(f"  {cabang[2]}\t: Rp{omzet[2]:,} ({transaksi[2]} trx)".replace(",", "."))
print(garis_tipis)
print(f"Total omzet      : Rp{total_omzet:,}".replace(",", "."))
print(f"Total transaksi  : {total_transaksi}")
print(f"Rata-rata/trx    : Rp{rata_rata:,}".replace(",", "."))
print(f"Selisih max-min  : Rp{selisih:,}".replace(",", "."))
print(f"Menu terlaris    : {menu_terlaris}")
print(f"Trx terakhir     : #{nomor_trx} di cabang {kode_cabang}")
print(garis_tipis)
print(f"Target harian    : Rp{TARGET_HARIAN:,}".replace(",", "."))
print(f"Capaian          : {persen_target:.2f}%")
print(f"Target tercapai? : {target_tercapai}")
print(garis)
print("Laporan ini dibuat otomatis oleh Python ☕")
