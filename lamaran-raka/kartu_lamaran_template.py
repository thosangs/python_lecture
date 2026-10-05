# ==============================================
# Kartu Lamaran Raka v1.0 (TEMPLATE LATIHAN)
# Penulis: ___ (ganti dengan namamu)
#
# Ganti semua ___ sampai kartu tampil.
# Kalau masih ada ___ yang tersisa, Python akan protes:
#   NameError: name '___' is not defined
# Kunci jawaban: kartu_lamaran.py
# ==============================================

# --- 1. Konstanta ---
NAMA_KAMPUS = "Universitas Kenanga Raya"
GAJI_HARAPAN = 6_500_000
TANGGAL_LAHIR = (12, 3, 2004)

# --- 2. Input data lowongan ---
perusahaan = input("Nama perusahaan: ").strip().upper()
# TODO: minta posisi, rapikan (buang spasi + Huruf Depan Kapital)    [Bab 6 & 8]
posisi = ___
# TODO: minta IPK minimal, ubah jadi angka desimal                    [Bab 6 & 8]
ipk_minimal = ___

# --- 3. Data Raka (dari ijazah & transkrip) ---
nama_mentah = "  raka PRATAMA putra "
jurusan = "Statistika"
nomor_ijazah = "IJZ-20260915-STA-0457"
total_sks = 144
total_mutu = 497
ips = [3.20, 3.35, 3.50, 3.41, 3.60, 3.52, 3.38, 3.65]
skill = ["Python", "Excel", "SQL"]

# --- 4. Olah data ---
ipk = ___                 # TODO: total mutu / total SKS, bulatkan 2 desimal  [Bab 5]
ips_terbaik = ___         # TODO: IPS paling tinggi                          [Bab 7]
usia = ___                # TODO: 2026 - tahun lahir (ambil dari tuple)       [Bab 7]
memenuhi_syarat = ___     # TODO: apakah ipk >= ipk_minimal?                  [Bab 5]

nama = ___                # TODO: rapikan nama_mentah                         [Bab 6]
tanggal_lulus = nomor_ijazah[10:12] + "-" + nomor_ijazah[8:10] + "-" + nomor_ijazah[4:8]
lulusan_ke = ___          # TODO: ambil "0457", ubah jadi angka               [Bab 6]

# --- 5. Cetak kartu lamaran ---
garis = "=" * 46
garis_tipis = "-" * 46

print(garis)
print(f"KARTU LAMARAN {nama.upper()}".center(46))
print(garis)
print(f"Perusahaan       : {perusahaan}")
print(f"Posisi           : {posisi}")
print(garis_tipis)
print(f"Nama             : {nama} ({usia} th)")
print(f"Kampus           : {NAMA_KAMPUS}")
# TODO: cetak jurusan, nomor ijazah, dan tanggal lulus (+ lulusan ke-berapa)
___
___
___
print(garis_tipis)
print(f"Total SKS        : {total_sks}")
print(f"IPK              : {ipk:.2f}")
# TODO: cetak IPS terbaik (2 desimal) dan ketiga skill
___
___
print(f"Ekspektasi gaji  : Rp{GAJI_HARAPAN:,}".replace(",", "."))
print(garis_tipis)
# TODO: cetak IPK minimal (2 desimal) dan status memenuhi syarat
___
___
print(garis)
print(f"Yth. HRD {perusahaan},")
print(f"saya {nama}, lulusan {jurusan}")
print(f"{NAMA_KAMPUS} dengan IPK {ipk:.2f},")
print(f"ingin melamar posisi {posisi}.")
