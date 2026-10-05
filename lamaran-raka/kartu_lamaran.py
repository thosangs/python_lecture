# ==============================================
# Kartu Lamaran Raka v1.0
# Penulis: Raka (dan kamu!)
#
# Jalankan dari terminal:
#   python3 kartu_lamaran.py      (Mac/Linux)
#   python kartu_lamaran.py       (Windows)
# ==============================================

# --- 1. Konstanta: nilai yang nggak berubah ---           (Bab 4)
NAMA_KAMPUS = "Universitas Kenanga Raya"
GAJI_HARAPAN = 6_500_000
TANGGAL_LAHIR = (12, 3, 2004)                             # (Bab 7: tuple)

# --- 2. Input data lowongan ---                           (Bab 8 + Bab 6)
perusahaan = input("Nama perusahaan: ").strip().upper()
posisi = input("Posisi yang dilamar: ").strip().title()
ipk_minimal = float(input("IPK minimal: "))

# --- 3. Data Raka (dari ijazah & transkrip) ---           (Bab 7: list)
nama_mentah = "  raka PRATAMA putra "
jurusan = "Statistika"
nomor_ijazah = "IJZ-20260915-STA-0457"
total_sks = 144
total_mutu = 497
ips = [3.20, 3.35, 3.50, 3.41, 3.60, 3.52, 3.38, 3.65]
skill = ["Python", "Excel", "SQL"]

# --- 4. Olah data ---                                      (Bab 5)
ipk = round(total_mutu / total_sks, 2)
ips_terbaik = max(ips)
usia = 2026 - TANGGAL_LAHIR[2]
memenuhi_syarat = ipk >= ipk_minimal

nama = nama_mentah.strip().title()                        # (Bab 6)
tanggal_lulus = nomor_ijazah[10:12] + "-" + nomor_ijazah[8:10] + "-" + nomor_ijazah[4:8]
lulusan_ke = int(nomor_ijazah[-4:])

# --- 5. Cetak kartu lamaran ---                            (Bab 8)
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
print(f"Jurusan          : {jurusan}")
print(f"Nomor ijazah     : {nomor_ijazah}")
print(f"Tanggal lulus    : {tanggal_lulus} (lulusan ke-{lulusan_ke})")
print(garis_tipis)
print(f"Total SKS        : {total_sks}")
print(f"IPK              : {ipk:.2f}")
print(f"IPS terbaik      : {ips_terbaik:.2f}")
print(f"Skill            : {skill[0]}, {skill[1]}, {skill[2]}")
print(f"Ekspektasi gaji  : Rp{GAJI_HARAPAN:,}".replace(",", "."))
print(garis_tipis)
print(f"IPK minimal      : {ipk_minimal:.2f}")
print(f"Memenuhi syarat? : {memenuhi_syarat}")
print(garis)
print(f"Yth. HRD {perusahaan},")
print(f"saya {nama}, lulusan {jurusan}")
print(f"{NAMA_KAMPUS} dengan IPK {ipk:.2f},")
print(f"ingin melamar posisi {posisi}.")
