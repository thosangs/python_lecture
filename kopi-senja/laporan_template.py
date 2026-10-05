# ==============================================
# Laporan Harian Kopi Senja v1.0 (TEMPLATE LATIHAN)
# Penulis: ___ (ganti dengan namamu)
#
# Ganti semua ___ sampai laporan tampil.
# Kalau masih ada ___ yang tersisa, Python akan protes:
#   NameError: name '___' is not defined
# Kunci jawaban: laporan.py
# ==============================================

# --- 1. Konstanta ---
NAMA_TOKO = "Kopi Senja"
TARGET_HARIAN = 10_000_000
JAM_OPERASIONAL = (7, 22)

# --- 2. Input ---
# TODO: minta nama analis, lalu rapikan (buang spasi + Huruf Depan Kapital)   [Bab 6 & 8]
nama_analis = ___
tanggal = input("Tanggal laporan (DD-MM-YYYY): ").strip()

# --- 3. Data hari ini ---
cabang = ["Jakarta", "Bandung", "Surabaya"]
omzet = [4_250_000, 2_875_000, 3_520_000]
transaksi = [170, 125, 160]
menu_terlaris_mentah = "   es KOPI susu gula AREN  "
kode_trx_terakhir = "TRX-20261005-JKT-0170"

# --- 4. Olah data ---
total_omzet = ___                 # TODO: jumlahkan semua omzet               [Bab 7]
total_transaksi = ___             # TODO: jumlahkan semua transaksi           [Bab 7]
rata_rata = ___                   # TODO: total omzet / total trx, dibulatkan [Bab 5]
selisih = ___                     # TODO: omzet tertinggi - terendah          [Bab 5]
persen_target = ___               # TODO: total omzet / target * 100          [Bab 5]
target_tercapai = ___             # TODO: apakah total omzet >= target?       [Bab 5]

menu_terlaris = ___               # TODO: rapikan menu_terlaris_mentah        [Bab 6]
kode_cabang = ___                 # TODO: ambil "JKT" dari kode trx           [Bab 6]
nomor_trx = ___                   # TODO: ambil "0170", ubah jadi angka       [Bab 6]

# --- 5. Cetak laporan ---
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
# TODO: tulis baris untuk Bandung dan Surabaya (contek baris di atas)
___
___
print(garis_tipis)
print(f"Total omzet      : Rp{total_omzet:,}".replace(",", "."))
# TODO: cetak total transaksi, rata-rata (format Rupiah), selisih (format Rupiah)
___
___
___
print(f"Menu terlaris    : {menu_terlaris}")
print(f"Trx terakhir     : #{nomor_trx} di cabang {kode_cabang}")
print(garis_tipis)
print(f"Target harian    : Rp{TARGET_HARIAN:,}".replace(",", "."))
# TODO: cetak capaian (2 desimal + tanda %) dan status target tercapai
___
___
print(garis)
print("Laporan ini dibuat otomatis oleh Python ☕")
