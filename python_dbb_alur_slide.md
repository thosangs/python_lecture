# Alur Slide — Python Fundamentals & Logic
### Pertemuan 1 · 2,5 jam · "Laporan Pagi Raka"

> Dokumen ini pendamping [python_dbb.md](python_dbb.md). Isinya alur per slide, contoh kode (sudah dites di Python 3.12), kapan pindah ke Colab/VSCode, latihan, dan catatan trainer.

---

## Daftar Isi

0. [Cara pakai dokumen ini](#0-cara-pakai-dokumen-ini)
1. [Ceritanya: Senin Pagi di Kopi Senja](#1-ceritanya-senin-pagi-di-kopi-senja)
2. [Tujuan pembelajaran](#2-tujuan-pembelajaran)
3. [Prinsip pedagogis yang dipakai](#3-prinsip-pedagogis-yang-dipakai)
4. [Rundown & peta navigasi](#4-rundown--peta-navigasi)
5. [Persiapan sebelum kelas](#5-persiapan-sebelum-kelas)
6. [Alur per slide](#6-alur-per-slide)
7. [Kode final + template peserta](#7-kode-final--template-peserta)
8. [Kamus Error](#8-kamus-error)
9. [FAQ trainer](#9-faq-trainer)
10. [Rencana cadangan](#10-rencana-cadangan)
11. [Catatan perubahan dari outline asli](#11-catatan-perubahan-dari-outline-asli)
12. [Lampiran: Cheat sheet peserta](#12-lampiran-cheat-sheet-peserta)

---

## 0. Cara pakai dokumen ini

**Deck slide:** https://thosangs.github.io/python_lecture/ (sumber: [slides/slides.md](slides/slides.md)). Nomor slide di dokumen ini **sama persis** dengan nomor di deck. Footer tiap slide sudah menampilkan bab aktif, progres kartu stempel, dan penanda lokasi (🧪/🎯/💻) beserta section notebook yang harus dibuka. Poin "Ngomongnya" & "Catatan trainer" juga ada di **mode presenter** (`/presenter`).

**Notebook** (folder [notebooks/](notebooks/)):
- `01_materi_kopi_senja.ipynb`: notebook **trainer** untuk live coding (= "Materi" di footer slide), sudah dijalankan
- `02_latihan_peserta.ipynb`: notebook **peserta** (= "Latihan" di footer slide), bersih tanpa output
- `03_kunci_jawaban.ipynb`: kunci jawaban, sudah dijalankan

**Legend lokasi** (lihat di judul tiap slide, ini penanda "aku harus ke mana"):

| Ikon | Artinya |
|---|---|
| 🖥️ **SLIDE** | Tetap di slide, kamu menjelaskan |
| 🧪 **COLAB-DEMO** | Pindah ke Colab, **kamu** live coding, peserta nonton (boleh ikut ngetik) |
| 🎯 **HANDS-ON** | Peserta **wajib** ngetik di Colab mereka sendiri |
| 💻 **VSCODE** | Pindah ke VSCode (demo trainer) |
| ⏸️ **ISTIRAHAT** | Break |
| 🎟️ **STEMPEL** | Akhir bab, "cap" kartu stempel (lihat bagian 1) |

**Legend level materi** (biar jelas mana yang harus dikuasai, mana yang cukup dikenalkan):

| Tag | Artinya | Implikasi di kelas |
|---|---|---|
| 🟢 **Wajib** | Harus bisa dipraktikkan di akhir kelas | Ada latihan, muncul di final project |
| 🟡 **Paham** | Ngerti konsepnya, belum harus lancar | Demo + 1 contoh |
| ⚪ **Kenalan** | Cukup tahu "ada" | 1 kalimat + 1 contoh, jangan didalami |

**Format tiap slide:**
- **Di layar**: apa yang tampil di slide (usahakan max ±20 kata + visual)
- **Ngomongnya**: poin bicara / skrip (dalam tanda kutip = kalimat yang bisa langsung kamu pakai)
- **Kode**: yang diketik live (bukan di-paste, kecuali data)
- **Interaksi**: pertanyaan / tebak output / polling
- **Catatan trainer**: jebakan, nuansa, antisipasi pertanyaan
- **➡️ Lanjut**: transisi ke slide/lokasi berikutnya

---

## 1. Ceritanya: Senin Pagi di Kopi Senja

### Tokoh
- **Raka**: data analyst baru (3 bulan) di **Kopi Senja**, kedai kopi dengan 3 cabang: **Jakarta (JKT), Bandung (BDG), Surabaya (SBY)**.
- **Bu Sari**: owner Kopi Senja, tiap pagi jam 08.00 nunggu laporan penjualan kemarin di WhatsApp.

### Masalahnya
Tiap pagi Raka menghabiskan **±65 menit** untuk:
1. Download 3 file penjualan dari aplikasi kasir tiap cabang
2. Gabungin di Excel
3. Benerin nama menu yang ditulis beda-beda tiap kasir (`"  es kopi SUSU gula aren "`, `"ES KOPI SUSU GULA AREN"`, ...)
4. Hitung total, rata-rata, cabang terbaik, cek target
5. Ngetik ulang laporan di WhatsApp ke Bu Sari

Suatu hari Raka salah ketik `Rp1.250.000` jadi `Rp12.500.000`. Bu Sari sempat girang, lalu panik. 😅

### Misinya
Di akhir kelas, peserta membantu Raka membuat **script Python yang menghasilkan laporan harian rapi dalam 1 detik**.

### Kenapa satu cerita?
Konteks yang konsisten bikin setiap konsep punya **alasan untuk ada**. Peserta nggak belajar "string slicing" sebagai teori abstrak, tapi sebagai "cara Raka ngambil kode cabang dari kode transaksi". Setiap bab selalu dibuka dengan **masalah Raka** → lalu **konsep** yang menyelesaikannya.

### Peta cerita (story arc)

| Bab | Masalah Raka | Konsep | Hasil yang dibawa ke final project |
|---|---|---|---|
| Prolog | Laporan manual 65 menit/hari | – | Melihat target akhir (demo) |
| 1. Kenapa Raka Harus Ngoding? | Repetitif, membosankan, rawan salah | Otomasi & konsistensi | Motivasi |
| 2. Kenalan sama Python | "Pakai bahasa apa?" | Python: high-level, interpreted, general purpose | – |
| 3. Nyiapin Meja Kerja | "Ngodingnya di mana?" | Dev environment, Colab, VSCode | Notebook & file `laporan.py` |
| 4. Toples Berlabel | Angka-angka berserakan | Komentar, `print`, variabel, aturan nama | Konstanta & variabel data |
| 5. Ngitung Omzet | Hitung total, rata-rata, cek target | int, float, operator, built-in angka, boolean | Semua angka laporan |
| 6. Beresin Nama Menu | Nama menu berantakan, kode transaksi panjang | String, indexing, slicing, method, casting | Menu terlaris rapi, nomor transaksi |
| 7. Wadah Banyak Barang | "Kalau cabangnya 30?" | list, tuple, set, dict | Data per cabang dalam list |
| 8. Laporan buat Bu Sari | Laporan harus rapi & bisa diisi | `print`, escape char, f-string, `input` | Tampilan laporan |
| Final: Satu Klik, Laporan Jadi | Gabungkan semuanya | Semua di atas | **Laporan Harian v1.0** |
| Epilog: Bersambung... | Masih ada yang manual | Teaser: if, loop, function, pandas | Hook pertemuan berikutnya |

### Gamifikasi: Kartu Stempel Kopi Senja ☕
Tampilkan kartu stempel dengan **8 kotak** di slide peta perjalanan. Tiap selesai bab, satu kotak dicap (cukup animasi di slide). 8 stempel = **"1 kopi gratis"** = final project. Murah, tapi bikin progres terasa dan memberi ritme.

### Data Kit (dipakai sepanjang kelas, angka konsisten)

```python
# ===== DATA KIT KOPI SENJA (penjualan Senin, 5 Oktober 2026) =====
omzet_jakarta  = 4_250_000     # Rupiah
omzet_bandung  = 2_875_000
omzet_surabaya = 3_520_000

trx_jakarta  = 170             # jumlah transaksi
trx_bandung  = 125
trx_surabaya = 160

TARGET_HARIAN = 10_000_000     # target omzet gabungan 3 cabang

# nama menu terlaris versi tiap kasir (berantakan!)
menu_kasir_jkt = "  es kopi SUSU gula aren "
menu_kasir_bdg = "ES KOPI SUSU GULA AREN"
menu_kasir_sby = "Es Kopi susu Gula Aren   "

kode_trx = "TRX-20261005-JKT-0170"   # transaksi terakhir hari itu
```

**Angka kunci (buat cek jawaban cepat):** total omzet `10645000` · total transaksi `455` · rata-rata/transaksi `23396` (dibulatkan) · selisih tertinggi-terendah `1375000` · capaian target `106.45%` · target tercapai `True`.

---

## 2. Tujuan pembelajaran

Setelah pertemuan ini, peserta mampu:

1. **Menjelaskan** dengan bahasa sendiri apa itu Python dan kenapa dipakai di dunia data.
2. **Menjalankan** kode Python di Google Colab dan (melihat demo) di VSCode.
3. **Membuat** variabel dengan nama yang valid dan sesuai konvensi.
4. **Membedakan** tipe data dasar (int, float, str, bool) dan mengenali koleksi (list, tuple, set, dict).
5. **Mengolah** angka dengan operator dan fungsi bawaan, serta teks dengan indexing, slicing, dan method.
6. **Menampilkan** output terformat dengan f-string dan menerima input dari pengguna.
7. **Membaca** pesan error dasar dan memperbaikinya sendiri.
8. **Menyusun** script sederhana yang menggabungkan semua konsep di atas (Laporan Harian v1.0).

> Versi ramah peserta (untuk Slide 7): *"Hari ini kalian akan (1) kenalan sama Python, (2) nulis & jalanin kode sendiri, (3) bikin laporan otomatis buat Kopi Senja."*

---

## 3. Prinsip pedagogis yang dipakai

| Prinsip | Kenapa penting untuk pemula | Cara diterapkan di kelas ini |
|---|---|---|
| **Narrative / contextual learning** | Otak lebih gampang mengingat cerita daripada daftar fakta | Satu cerita Raka dari awal sampai akhir; tiap konsep menjawab "masalah Raka yang mana?" |
| **Tunjukkan tujuan di awal** (Gagné) | Peserta tahu "ujungnya ke mana", jadi tiap materi terasa relevan | Slide 6: demo laporan jadi dalam 1 detik |
| **Advance organizer** | Kasih "peta" sebelum detail biar informasi baru punya tempat | Peta perjalanan (Slide 7), peta tipe data (Slide 34) |
| **Masalah → Konsep → Contoh → Coba** | Konsep muncul sebagai solusi, bukan hafalan | Pola tetap di tiap bab |
| **PRIMM** (Predict-Run-Investigate-Modify-Make) | Menebak dulu bikin otak aktif dan miskonsepsi langsung kelihatan | "Tebak dulu sebelum di-run" di setiap demo; latihan bergerak dari modifikasi ke membuat sendiri |
| **Worked example → faded → mandiri** | Pemula kewalahan kalau langsung disuruh nulis dari nol | Demo lengkap → latihan isi titik-titik → final project dengan template |
| **Cognitive load** | Memori kerja pemula kecil (±4 hal baru sekaligus) | Satu konsep per slide; label 🟢🟡⚪; data di-paste (bukan diketik) supaya fokus ke logika |
| **Aturan 10 menit** | Atensi turun setelah ±10 menit mendengarkan | Tidak pernah lebih dari ±10 menit tanpa peserta ngetik / menjawab |
| **Error itu teman** (productive failure) | Pemula sering takut error dan berhenti | Sengaja bikin error di depan; "Kamus Error" yang bertambah tiap bab; skill membaca error diajarkan eksplisit |
| **Retrieval practice** | Mengingat kembali lebih efektif daripada membaca ulang | Tebak output tiap bab, latihan, final project, exit ticket |
| **Spiral** | Konsep diulang di konteks baru jadi makin kuat | Indexing string dipakai ulang di list; semua konsep muncul lagi di final project |
| **Analogi konsisten dari satu dunia** | Analogi yang konsisten mengurangi beban "pindah konteks" | Semua analogi dari dunia kedai kopi (toples, mesin kopi, papan menu, dll) |
| **Formative assessment** | Trainer tahu kapan harus melambat | Sinyal 🟢/🔴, tebak output, exit ticket 3-2-1 |
| **Psychological safety** | Pemula malu bertanya | Aturan main di awal; normalisasi error; trainer juga "kena error" |

### Aturan live coding
1. Font editor **besar** (Colab: Settings → Editor → font size 16–18; zoom browser 125–150%).
2. **Ketik, jangan paste** (kecuali data kit). Ketik pelan sambil **narasikan** apa yang kamu ketik.
3. **Tanya "tebak hasilnya?"** sebelum menekan Shift+Enter.
4. **Sengaja salah** minimal sekali per bab, lalu baca error bareng.
5. Kalau ada peserta tertinggal, **jangan tunggu satu-satu di depan kelas**. Minta asisten / teman sebelah bantu, lanjutkan.

### Aturan main peserta (ditampilkan di Slide 7)
- Error itu **wajar dan normal**. Programmer senior pun kena error tiap hari.
- Tanya kapan saja, nggak ada pertanyaan bodoh.
- Sinyal: 🟢 = "aman, berhasil" · 🔴 = "stuck, tolong" (offline: kertas/sticky note hijau-merah; online: reaction Zoom/Meet).
- **Ketik sendiri**, jangan cuma copy-paste. Jari yang ngetik bikin otak lebih ingat.

---

## 4. Rundown & peta navigasi

| Waktu | Durasi | Slide | Bagian | Lokasi | Aktivitas utama |
|---|---|---|---|---|---|
| 00:00 | 7' | 1–7 | **Prolog**: Senin Pagi di Kopi Senja | 🖥️ → 🧪 (S6) → 🖥️ | Hook cerita, demo hasil akhir |
| 00:07 | 6' | 8–10 | **Bab 1**: Kenapa Raka Harus Ngoding? | 🖥️ | Diskusi, hitung jam terbuang |
| 00:13 | 10' | 11–17 | **Bab 2**: Kenalan sama Python | 🖥️ → 🧪 (S15) → 🖥️ | Tebak arti kode, demo interpreted |
| 00:23 | 7' | 18–21 | **Bab 3**: Nyiapin Meja Kerja | 🖥️ | Konsep dev environment |
| 00:30 | 12' | 22–25 | **Hands-on 1**: Halo, Kopi Senja! | 🎯 Colab → 💻 VSCode → 🖥️ | Setup Colab, error pertama, demo VSCode |
| 00:42 | 15' | 26–33 | **Bab 4**: Toples Berlabel | 🖥️ ⇄ 🧪, 🎯 di S33 | Komentar, print, variabel |
| 00:57 | 15' | 34–40 | **Bab 5**: Ngitung Omzet | 🖥️ ⇄ 🧪, 🎯 di S40 | Angka, operator, boolean |
| 01:12 | 10' | 41 | ⏸️ **Istirahat** | – | Teaser puzzle di layar |
| 01:22 | 20' | 42–50 | **Bab 6**: Beresin Nama Menu | 🖥️ ⇄ 🧪, 🎯 di S50 | String, slicing, method |
| 01:42 | 10' | 51–55 | **Bab 7**: Wadah Banyak Barang | 🖥️ ⇄ 🧪 | list, tuple, set, dict |
| 01:52 | 15' | 56–61 | **Bab 8**: Laporan buat Bu Sari | 🖥️ ⇄ 🧪, 🎯 di S61 | f-string, input |
| 02:07 | 15' | 62–64 | **Final**: Satu Klik, Laporan Jadi | 🎯 Colab → 💻 VSCode | Mini project |
| 02:22 | 8' | 65–69 | **Epilog**: Bersambung... | 🖥️ | Recap, teaser, PR, exit ticket |

**Rasio kegiatan:** ±45% peserta aktif (ngetik/menjawab), ±55% penjelasan + demo. Bagian teori murni (Prolog–Bab 3) dibatasi 30 menit supaya peserta cepat pegang kode.

**Buffer tersembunyi** (kalau telat, ini yang dipadatkan duluan): ⚪ complex & frozenset, `%` & `.format()`, step slicing, tuple & set (lihat [Rencana cadangan](#10-rencana-cadangan)).

### Struktur notebook Colab
Ketiga notebook punya section yang sama persis:

| Section | `01_materi` (trainer, live coding) | `02_latihan_peserta` | `03_kunci_jawaban` |
|---|---|---|---|
| `00 · Demo Final` | Script final siap run | – | – |
| `Bab 3 · Halo Kopi Senja` | Contoh print, demo interpreted | Cell kosong + demo tebak output | Jawaban |
| `Bab 4 · Toples Berlabel` | Semua demo Bab 4 | Latihan + Pojok Error (1 cell per baris) | Jawaban + tabel Pojok Error |
| `Bab 5 · Ngitung Omzet` | Semua demo Bab 5 | Data kit angka + 1 cell per soal | Jawaban |
| `Bab 6 · Beresin Nama Menu` | Semua demo Bab 6 | Data kit teks + 1 cell per soal | Jawaban |
| `Bab 7 · Wadah Banyak Barang` | Semua demo Bab 7 | Cell coba-coba + kuis | Jawaban kuis |
| `Bab 8 · Laporan buat Bu Sari` | Semua demo Bab 8 | Latihan | Jawaban |
| `Final · Laporan Harian v1.0` | Penutup + teaser | Template isi titik-titik | Kunci final + bonus |

Di slide yang ada 🧪/🎯, sebut **nama section-nya** supaya peserta tahu harus scroll ke mana. Link Colab peserta: https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb

---

## 5. Persiapan sebelum kelas

### Peserta (kirim H-3, ingatkan H-1)
- [ ] Punya akun Google, bisa buka [colab.research.google.com](https://colab.research.google.com)
- [ ] *(Opsional, untuk ikut demo VSCode)* Install Python 3.12+ dan VSCode + extension "Python" (Microsoft). Tes di terminal: `python3 --version` (Mac/Linux) atau `python --version` (Windows)
- [ ] Laptop dicas, internet stabil

### Trainer
- [ ] Buka `01_materi_kopi_senja.ipynb` di Colab (link dari README repo), *Save a copy in Drive* supaya bisa diedit saat live coding
- [ ] Link Colab `02_latihan_peserta.ipynb` siap di-paste ke chat (peserta nanti *Save a copy in Drive*)
- [ ] Section `00 · Demo Final` sudah dites, termasuk `input()`
- [ ] Clone repo, buka folder `kopi-senja/` di VSCode: `laporan.py` (isi final) siap, terminal sudah terbuka, interpreter Python terpilih
- [ ] Font size Colab & VSCode diperbesar
- [ ] Deck terbuka (https://thosangs.github.io/python_lecture/), mode presenter di layar kedua kalau ada
- [ ] Link notebook + link form exit ticket siap di-paste ke chat
- [ ] Papan/area **"Kamus Error"** (whiteboard, atau 1 slide yang diisi bertahap)
- [ ] **Backup**: kalau Colab bermasalah, pakai Jupyter lokal / VSCode dengan file `.ipynb` yang sama

---

## 6. Alur per slide

---

## PROLOG: Senin Pagi di Kopi Senja
**00:00 – 00:07 (7 menit)**

### Slide 1 · Judul · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** "Python Fundamentals & Logic: Dari Excel Manual ke Laporan Otomatis". Subjudul: Pertemuan 1. Visual: secangkir kopi + laptop.

**Ngomongnya:** Perkenalan singkat diri (maks 30 detik). Langsung masuk ke kalibrasi.

---

### Slide 2 · Angkat tangan dulu! · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** 3 pertanyaan:
1. Siapa yang **pakai Excel/Spreadsheet** hampir tiap hari?
2. Siapa yang pernah **ngerjain hal yang sama berulang-ulang** tiap hari/minggu di laptop?
3. Siapa yang **pernah ngoding** (bahasa apa pun)?

**Interaksi:** Angkat tangan / reaction. Catat dalam hati proporsi yang pernah ngoding.

**Catatan trainer:** Ini **kalibrasi**. Kalau banyak yang sudah pernah ngoding, siapkan "jalur ngebut" (tantangan 🔴). Kalau hampir semua belum, lambatkan Bab 4–6. Pertanyaan 2 juga jadi jembatan emosional ke cerita Raka: *"Nah, kalian nggak sendirian. Kenalin, Raka."*

---

### Slide 3 · 📖 Kenalan sama Raka · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** Ilustrasi Raka. "Raka, data analyst baru (3 bulan) di **Kopi Senja**: 3 cabang (Jakarta, Bandung, Surabaya)." Logo kedai fiktif.

**Ngomongnya:** "Raka ini sebenernya mirip banyak dari kita: jago Excel, rajin, tapi kerjaannya makin hari makin banyak."

---

### Slide 4 · 📖 Senin pagi Raka · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** Timeline:
```
07.00  Download 3 file penjualan dari kasir tiap cabang
07.15  Gabungin di Excel
07.25  Benerin nama menu yang ditulis beda-beda
07.40  Hitung total, rata-rata, cek target
07.55  Ketik ulang laporan di WhatsApp ke Bu Sari
08.05  Selesai... tiap hari. 😮‍💨
```
Plus screenshot/potongan data berantakan:
```
"  es kopi SUSU gula aren "   | 4250000
"ES KOPI SUSU GULA AREN"      | 2875000
"Es Kopi susu Gula Aren   "   | 3520000
```

**Ngomongnya:** "Ini terjadi **setiap hari kerja**."

---

### Slide 5 · 📖 Sampai suatu hari... · 🖥️ SLIDE · ⏱️ 0,5'
**Di layar:** Bubble chat WhatsApp:
> Raka: "Omzet Jakarta kemarin Rp12.500.000 Bu 🙏"
> Bu Sari: "WAH 😍 ... eh bentar, kok 10x lipat? 😨"

**Ngomongnya:** "Harusnya Rp1.250.000. Satu nol nyelip. Capek, ngantuk, manusiawi. Tapi Bu Sari jadi nggak percaya lagi sama laporan."

---

### Slide 6 · Hari ini kita bantu Raka · 🧪 COLAB-DEMO · ⏱️ 1,5'
**Di layar (sebelum pindah):** "Bagaimana kalau semua itu selesai dalam **1 detik**?"

**➡️ Pindah ke Colab, notebook `01_materi_kopi_senja`, section `00 · Demo Final`.** Jalankan cell (isi nama & tanggal saat diminta input). Biarkan output laporan tampil penuh.

**Ngomongnya:** "Ini yang **kalian sendiri** bakal bikin di akhir kelas. Bukan saya, kalian. Semua yang kita pelajari hari ini adalah potongan puzzle buat bikin ini."

**Catatan trainer:** Jangan jelaskan kodenya sekarang. Scroll cepat untuk menunjukkan kodenya "cuma" ±50 baris. Tujuannya membuat penasaran.

**➡️ Lanjut:** balik ke 🖥️ Slide 7.

---

### Slide 7 · Peta perjalanan & aturan main · 🖥️ SLIDE · ⏱️ 1'
**Di layar:**
- Kiri: **Kartu Stempel Kopi Senja** (8 kotak) dengan nama bab. "8 stempel = 1 kopi gratis (laporan otomatis!)"
- Kanan: Aturan main (lihat bagian 3): error itu wajar · tanya kapan saja · 🟢/🔴 · ketik sendiri

**Ngomongnya:** Bacakan tujuan versi ramah peserta. "Setiap selesai satu bab, kita cap satu stempel."

---

## BAB 1: Kenapa Raka Harus Ngoding?
**00:07 – 00:13 (6 menit)**

### Slide 8 · Masalahnya bukan di Excel-nya · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** Diagram: banyak sumber data mengalir ke Raka: 🧾 Kasir 3 cabang · 🛵 Aplikasi ojol (GoFood/GrabFood) · 📦 Stok gudang · 📱 Instagram · 💳 Mutasi bank. Tulisan besar: **"Di dunia data, datanya bukan cuma 1 file Excel."**

**Ngomongnya:** "Excel itu alat yang bagus. Masalahnya, data di dunia nyata datang dari banyak tempat, tiap hari, dengan format beda-beda. Excel nggak didesain buat kerja ulang yang sama tiap pagi."

**Interaksi:** "Di kerjaan/kampus kalian, data datang dari mana aja?" (1–2 jawaban saja)

---

### Slide 9 · 3 musuh kerja manual · 🖥️ SLIDE · ⏱️ 2,5'
**Di layar:** 3 kartu:
1. 🔁 **Repetitif**: kerjaan sama, tiap hari
2. 😴 **Membosankan**: bikin kita lengah
3. ⚠️ **Rawan salah & susah diaudit**: typo, rumus ketimpa, angka bisa diubah tanpa jejak

**Interaksi: hitung bareng.** "Raka butuh 65 menit sehari. Kerja 22 hari sebulan. Berapa jam sebulan?"
> 65 × 22 = 1.430 menit ≈ **24 jam ≈ 3 hari kerja penuh tiap bulan**, cuma buat copy-paste.

**Ngomongnya:** "Dan yang paling bahaya bukan capeknya, tapi **salahnya**. Proses manual juga susah diaudit: kalau ada angka yang berubah, siapa yang ngubah? Kapan? Nggak ada jejaknya."

**Catatan trainer:** Di outline tertulis "Fradulent". Di sini dibingkai sebagai *rawan salah & rawan manipulasi* karena proses manual tidak meninggalkan jejak.

---

### Slide 10 · Kodenya = resep · 🖥️ SLIDE · ⏱️ 1,5' · 🎟️ STEMPEL 1
**Di layar:** Kiri: "Manual: 65 menit, hasil bisa beda-beda". Kanan: "Script: 1 detik, hasil selalu sama". Tulisan besar: **Otomasi · Repetitif → Konsisten**.

**Ngomongnya:** "Kode itu kayak **resep**. Ditulis sekali, bisa dimasak berkali-kali, rasanya selalu sama. Kalau Raka nulis resep laporannya dalam bentuk kode, besok pagi tinggal 'masak' ulang."

**➡️ Transisi:** "Oke, Raka mau ngoding. Tapi pakai **bahasa** apa?" → 🎟️ cap stempel 1.

---

## BAB 2: Kenalan sama Python
**00:13 – 00:23 (10 menit)**

### Slide 11 · Bahasa buat ngobrol sama komputer · 🖥️ SLIDE · ⏱️ 1,5' · ⚪
**Di layar:** Spektrum dari kiri ke kanan:
`Bahasa mesin (0101) → Assembly → C → Java, PHP → Python`
dengan label **Low level** (dekat ke mesin) ↔ **High level** (dekat ke manusia).

**Ngomongnya (analogi barista):**
> "Bayangin kalian pesan kopi.
> **Low level**: 'Ambil 18 gram biji, giling ukuran 3, tekan tamper 15 kg, seduh 9 bar selama 25 detik, tuang susu 150 ml suhu 65 derajat...'
> **High level**: 'Mas, es kopi susu satu, gulanya dikit ya.'
> Hasilnya sama-sama kopi. Bedanya: siapa yang mikirin detailnya. Di bahasa high level, detail ribetnya diurus oleh bahasanya."

---

### Slide 12 · Sama-sama bilang "Halo" · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:** 4 kotak berdampingan, semuanya menampilkan tulisan "Halo, Kopi Senja!":

**Bahasa mesin (ilustrasi):**
```
10110000 01100001 11001101 00100001 ...
```
**Assembly:**
```
mov edx, len
mov ecx, msg
mov ebx, 1
mov eax, 4
int 0x80
```
**Java:**
```java
public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, Kopi Senja!");
    }
}
```
**Python:**
```python
print("Halo, Kopi Senja!")
```

**Ngomongnya:** "Java juga high level, tapi lihat bedanya. Python satu baris. Itu yang dimaksud **simple syntax**."

---

### Slide 13 · Dirancang untuk mudah dibaca · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:**
```python
menu_tersedia = ["kopi susu", "americano", "latte"]
pesanan = "latte"

if pesanan in menu_tersedia:
    print("Siap, pesanan dibuat!")
else:
    print("Maaf, menu habis.")
```

**Interaksi:** "Kalian **belum belajar** Python sama sekali. Tapi coba tebak: program ini ngapain?" Tunggu 2–3 jawaban.

**Ngomongnya:** "Kalian bisa nebak, kan? Itu karena Python didesain dengan prinsip **readability**: kode harus gampang dibaca manusia. Salah satu prinsip resmi Python bunyinya *'Readability counts'*."

**Catatan trainer:** `if` sengaja dipakai di sini sebagai *teaser* (baru dipelajari pertemuan berikutnya). Jangan dijelaskan sintaksnya. Bonus: di Hands-on 1, peserta bisa jalankan `import this` untuk melihat "Zen of Python".

---

### Slide 14 · Interpreted vs Compiled · 🖥️ SLIDE · ⏱️ 2' · 🟡
**Di layar:**

| | **Interpreted** (Python) | **Compiled** (C, C++, Java, C#) |
|---|---|---|
| Cara kerja | Dibaca & dijalankan **baris per baris** | Seluruh kode **dibungkus** jadi bahasa mesin dulu, baru dijalankan |
| Analogi | Barista yang meracik sambil baca resep | Pabrik kopi kaleng: produksi dulu, baru bisa diminum |
| Error ketahuan | Saat baris itu dijalankan. Baris sebelumnya **sudah jalan** | Saat proses compile, **sebelum** program jalan sama sekali |
| Kelebihan | Cepat dicoba, cocok buat eksplorasi data | Eksekusi lebih cepat |
| Kekurangan | Eksekusi relatif lebih lambat | Tiap ubah kode harus compile ulang |

**Ngomongnya:** "Barista baca resep langkah demi langkah. Kalau di langkah ke-3 ternyata susunya habis, langkah 1 dan 2 udah terjadi, kopi udah digiling. Pabrik kopi kaleng beda: resep dicek dan diproses semua dulu. Kalau ada yang salah, ketahuan sebelum produksi, tapi tiap ganti resep harus produksi ulang."

**Catatan trainer (kalau ada yang kritis bertanya):**
- Secara teknis, Python (CPython) juga mengompilasi kode ke *bytecode* dulu, lalu bytecode itu dijalankan oleh interpreter. Tetap dikategorikan "interpreted".
- Java & C# dikompilasi ke bytecode lalu dijalankan virtual machine (JVM / .NET), jadi "compiled" di sini versi sederhana.
- **Penting untuk demo:** `SyntaxError` (salah tata bahasa) dicek di awal, jadi **seluruh cell tidak jalan**. Yang berhenti di tengah adalah error saat runtime seperti `NameError`. Karena itu demo Slide 15 pakai `NameError`.

**➡️ Lanjut:** "Biar kebayang, saya tunjukin langsung." → 🧪 Colab.

---

### Slide 15 · Demo: barista baca resep · 🧪 COLAB-DEMO · ⏱️ 1,5'
**➡️ Pindah ke Colab materi (`01_materi_kopi_senja`), section `Bab 3 · Halo Kopi Senja`** (peserta nonton saja).

**Kode:**
```python
print("1. Download data Jakarta... beres")
print("2. Download data Bandung... beres")
prnt("3. Download data Surabaya...")
print("4. Kirim laporan ke Bu Sari")
```

**Interaksi:** "Ada typo di baris 3. Tebak: berapa baris yang akan tercetak?" (A) 0 · (B) 2 · (C) 4

**Hasil:** 2 baris tercetak, lalu `NameError: name 'prnt' is not defined`. Baris 4 tidak dijalankan.

**Ngomongnya:** "Baris 1–2 jalan, baris 3 error, baris 4 nggak pernah dijalankan. Persis barista tadi."

**Catatan trainer:** Jangan bahas cara baca error dulu, itu nanti di Slide 23 saat peserta mengalaminya sendiri.

**➡️ Lanjut:** balik ke 🖥️ Slide 16.

---

### Slide 16 · General purpose: satu bahasa, banyak dapur · 🖥️ SLIDE · ⏱️ 1' · ⚪
**Di layar:** Grid ikon "library":
- 📊 **Data**: pandas, numpy, matplotlib
- 🤖 **AI/ML**: scikit-learn, PyTorch
- 🌐 **Web**: Django, Flask, FastAPI
- 🎮 **Game**: pygame
- ⚙️ **Otomasi**: openpyxl (Excel!), requests

**Ngomongnya:** "**Library** itu kayak bahan setengah jadi. Kopi Senja nggak perlu bikin sirup gula aren dari tebu, tinggal beli yang udah jadi. Di Python, mau baca Excel nggak perlu bikin dari nol, tinggal pakai library. Raka nanti pakai **pandas** buat baca file kasir, itu materi pertemuan selanjutnya."

---

### Slide 17 · Gratis, komunitasnya besar, jagoan di data · 🖥️ SLIDE · ⏱️ 1' · 🎟️ STEMPEL 2
**Di layar:**
- 🆓 **Free & open source**: gratis, kodenya terbuka
- 👥 **Komunitas besar**: di Indonesia ada **PythonID** (grup Telegram/Facebook) dan **PyCon ID** tiap tahun
- 🏆 Konsisten di peringkat atas bahasa terpopuler dunia, dan **bahasa nomor satu di dunia data**

**Ringkasan bab (tulisan besar di bawah):**
> **Python = bahasa high-level, mudah dibaca, interpreted, serbaguna, gratis, dan jagoan di dunia data.**

**Ngomongnya:** "Komunitas besar artinya kalau kalian error, 99% kemungkinan sudah ada orang lain yang pernah kena dan nanya duluan di internet."

**Catatan trainer:** Kalau mau menyebut peringkat/angka spesifik, cek data terbaru (TIOBE, IEEE Spectrum, Stack Overflow Developer Survey) sebelum kelas. Boleh tambah contoh perusahaan yang kamu tahu pasti pakai Python.

**➡️ Transisi:** "Bahasanya udah kepilih. Sekarang, Raka ngodingnya **di mana**?" → 🎟️ cap stempel 2.

---

## BAB 3: Nyiapin Meja Kerja
**00:23 – 00:30 (7 menit)**

### Slide 18 · Development environment = dapur · 🖥️ SLIDE · ⏱️ 1,5' · 🟡
**Di layar:** "**Development Environment**: tempat kita menulis, menjalankan, dan mengembangkan aplikasi." Ilustrasi dapur kedai.

**Ngomongnya:** "Barista butuh dapur. Programmer butuh **dev environment**. Dan dapurnya tergantung mau masak apa:
- Bikin web? Biasanya VSCode, Cursor, PhpStorm.
- Ngolah data? Biasanya VSCode, Cursor, atau **notebook**."

---

### Slide 19 · Isi dapur Python · 🖥️ SLIDE · ⏱️ 2' · ⚪ (kecuali interpreter & editor: 🟡)

**Di layar:**

| Komponen | Fungsinya | Analogi dapur |
|---|---|---|
| **Python interpreter** | Yang benar-benar menjalankan kode | Barista / mesin kopi |
| **Code editor** | Tempat menulis kode | Meja racik + buku resep |
| **Package manager** (pip, uv) | Download & install library | Supplier bahan |
| **Virtual environment** | Ruang terpisah per proyek, biar versi library nggak bentrok | Dapur terpisah per menu, biar bumbu nggak campur |

**Ngomongnya:** "Hari ini cukup ingat dua yang pertama: **interpreter** (yang menjalankan) dan **editor** (tempat nulis). Package manager dan virtual env akan kepakai nanti waktu kita mulai pakai library. Kabar baiknya: di Google Colab, semuanya udah disiapin."

---

### Slide 20 · 3 gaya meja kerja · 🖥️ SLIDE · ⏱️ 2'
**Di layar:**

| Gaya | Contoh | Analogi | Cocok untuk |
|---|---|---|---|
| **Text editor + terminal** | Notepad++ + terminal | Dapur minimalis | Script kecil, server |
| **IDE** (Integrated Dev Environment) | VSCode, PyCharm | Dapur produksi lengkap | Aplikasi / script yang dipakai rutin |
| **Notebook** | Jupyter (lokal), **Google Colab**, Marimo | *Test kitchen*: coba satu-satu, langsung cicip | Belajar, eksplorasi & analisis data |

**Ngomongnya:** "Notebook itu kayak dapur uji coba: kodenya dipotong-potong per **cell**, tiap cell bisa dijalankan dan langsung kelihatan hasilnya. Cocok banget buat belajar dan eksplorasi data."

---

### Slide 21 · Hari ini pakai yang mana? · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:**
- 🧪 **Google Colab** → tempat kita **belajar & coba-coba** (nggak perlu install apa pun)
- 💻 **VSCode** → tempat script **"beneran"** yang dijalankan rutin tiap pagi (tujuan akhir Raka)

**Ngomongnya:** "Sepanjang kelas kita pakai Colab. Di akhir kelas, kita pindahin hasilnya ke VSCode, karena itulah yang nanti dijalankan Raka tiap pagi."

**Catatan trainer:** Alasan semua peserta pakai Colab: **nol instalasi** = nol waktu terbuang buat troubleshooting setup, dan beban kognitif pemula fokus ke Python, bukan ke tools. VSCode cukup didemokan.

**➡️ Lanjut:** "Saatnya pegang kode!" → 🎯 Hands-on 1.

---

## HANDS-ON 1: Halo, Kopi Senja!
**00:30 – 00:42 (12 menit)**

### Slide 22 · Meja kerja pertamamu · 🎯 HANDS-ON · ⏱️ 6'
**Di layar (biarkan tampil, atau paste langkahnya di chat):**
1. Buka link notebook `02_latihan_peserta` (tombol di slide / di chat) → **File → Save a copy in Drive**
2. Ganti nama: `KopiSenja_NamaKamu.ipynb`
3. Scroll ke section **`Bab 3 · Halo Kopi Senja`**
4. Klik **+ Code**, ketik:
   ```python
   print("Halo, Kopi Senja!")
   ```
5. Tekan **Shift + Enter**
6. Ganti tulisannya jadi namamu, jalankan lagi
7. Klik **+ Text**, tulis: "Catatan kelas Python pertamaku ☕"
8. Kasih sinyal 🟢 kalau berhasil, 🔴 kalau stuck

**➡️ Pindah ke Colab (share screen)**, kerjakan bareng langkah demi langkah.

**Ngomongnya / tunjukkan:**
- "Kotak abu-abu ini namanya **cell**. Ada **code cell** (buat kode) dan **text cell** (buat catatan)."
- "Angka `[1]` di kiri cell = urutan cell itu dijalankan."
- "Run pertama kali agak lama karena Colab lagi nyiapin 'dapur' (runtime) di server Google."

**Catatan trainer:**
- Kalau peserta lupa tanda kutip → `NameError`; kurung tidak ditutup → `SyntaxError`. Bagus! Pakai sebagai bahan Slide 23.
- Bonus buat yang cepat: jalankan `import this`.

---

### Slide 23 · Error pertamamu (dan cara bacanya) · 🎯 HANDS-ON · ⏱️ 2,5'
**Kegiatan:** Di notebook latihan, cell demo Slide 15 sudah disiapkan. Peserta **tebak dulu** berapa baris yang tercetak, lalu jalankan.

**Di layar: Cara baca error dalam 3 langkah**
1. 👇 **Baca baris paling bawah dulu**: jenis error + pesannya (`NameError: name 'prnt' is not defined`)
2. 🔍 **Cari nomor baris / tanda panah**: di baris mana error terjadi
3. 🤔 **Bandingkan dengan maksudmu**: typo? lupa kutip? kurung belum ditutup?

**Ngomongnya:** "Pesan error itu bukan marah-marah, tapi **petunjuk**. Python sering bahkan kasih saran, misalnya *'Did you mean: print?'*."

**Mulai "Kamus Error"** (whiteboard/slide): tulis entri pertama:
> **NameError** = "Aku nggak kenal nama ini." Biasanya: typo, lupa tanda kutip, atau cell yang membuat variabelnya belum dijalankan.

---

### Slide 24 · Dapur produksi: VSCode · 💻 VSCODE · ⏱️ 2,5'
**➡️ Pindah ke VSCode** (demo trainer; peserta yang sudah install boleh ikut).

**Langkah demo:**
1. **File → Open Folder** → `kopi-senja` (folder di repo)
2. File baru: `laporan.py`
3. Ketik `print("Halo, Kopi Senja!")` → **simpan** (Cmd+S / Ctrl+S)
4. Jalankan lewat tombol ▶ **Run Python File**, atau di terminal:
   ```bash
   python3 laporan.py
   ```
   *(Windows: `python laporan.py`)*

**Ngomongnya:** "Bedanya sama Colab: ini **file** `.py`, resep yang tersimpan rapi. Bisa dijalankan kapan saja tanpa buka browser, bahkan bisa dijadwalkan jalan otomatis tiap jam 7 pagi. **Kita balik ke sini di akhir kelas.**"

**Catatan trainer:** Kalau tombol ▶ tidak muncul, cek extension Python terpasang dan interpreter terpilih (pojok kanan bawah VSCode). Peserta yang belum install: kirim panduan setup untuk dikerjakan di rumah.

---

### Slide 25 · Colab vs VSCode · 🖥️ SLIDE · ⏱️ 1' · 🎟️ STEMPEL 3
**Di layar:**

| | Colab (notebook) | VSCode (file `.py`) |
|---|---|---|
| Analogi | Test kitchen | Dapur produksi |
| Cara jalan | Per cell, Shift+Enter | Seluruh file sekaligus |
| Dipakai untuk | Belajar, eksplorasi, analisis | Script rutin, aplikasi |

**Tips penting notebook:** "Kalau Colab bilang variabel nggak dikenal padahal sudah kamu tulis, biasanya **cell-nya belum di-run**. Solusi pamungkas: **Runtime → Run all**."

**➡️ Transisi:** "Meja kerja siap. Sekarang Raka mulai nulis resep laporannya. Mulai sekarang kita di **Colab** terus." → 🎟️ cap stempel 3.

---

## BAB 4: Toples Berlabel
**00:42 – 00:57 (15 menit)**
*Komentar, print, variabel*

### Slide 26 · 📖 Langkah pertama Raka: catatan · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Di layar:** "Komentar: catatan untuk **manusia**, dilewati oleh Python." Simbol `#`.

**➡️ 🧪 Colab materi, section `Bab 4 · Toples Berlabel`.**

**Kode:**
```python
# Laporan harian Kopi Senja
# Dibuat oleh: Raka
print("Laporan dimulai")   # komentar juga bisa di ujung baris
# print("baris ini nggak dijalankan")
```

**Ngomongnya:** "Komentar dipakai untuk (1) menjelaskan **kenapa** kode ditulis begitu, dan (2) 'mematikan' kode sementara tanpa menghapusnya."

**Tips:** Shortcut **Cmd + /** (Mac) atau **Ctrl + /** (Windows) untuk menjadikan baris komentar / sebaliknya.

---

### Slide 27 · `print()` dan konsep function · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Di layar:** Ilustrasi **mesin kopi**: bahan masuk (argumen) dalam kurung `( )` → mesin bekerja → hasil keluar.
> **Function** = mesin yang mengerjakan tugas tertentu.
> **Built-in function** = mesin bawaan Python, tinggal pakai.

**Kode:**
```python
print("Laporan Kopi Senja")
print(3)
print("Jumlah cabang:", 3)    # beberapa nilai, dipisah koma
print()                       # baris kosong
print(Kopi)                   # ❌ sengaja: lupa tanda kutip
```

**Interaksi:** Sebelum menjalankan baris terakhir: "Ini bakal jalan nggak?"

**Ngomongnya:** "Teks pakai tanda kutip, angka tidak. Tanpa kutip, Python mengira `Kopi` itu nama sesuatu, dan dia nggak kenal → `NameError`, teman lama kita dari tadi."

**Catatan trainer:** Sebut sekilas bahwa built-in function lain akan menyusul: `type`, `len`, `abs`, `max`, `min`, `round`, `input`.

---

### Slide 28 · Variabel = toples berlabel · 🖥️→🧪 · ⏱️ 2' · 🟢
**Di layar:** Ilustrasi rak toples di dapur Kopi Senja. Tiap toples punya **label** (nama variabel) dan **isi** (nilai).
```
nama_variabel = nilai
```
**"`=` artinya MASUKKAN KE, bukan SAMA DENGAN."**

**Ngomongnya:** "Di Excel, Raka nyimpen omzet di sel `B2`, terus rumusnya `=B2+B3`. Masalahnya, `B2` itu apa? Nggak ada yang tahu tanpa buka filenya. Di Python, kita kasih **nama yang bermakna**."

**Kode:**
```python
nama_toko = "Kopi Senja"
jumlah_cabang = 3
omzet_jakarta = 4250000

print(nama_toko)
print(omzet_jakarta)
```

**Interaksi: tebak output** (tulis di layar sebelum run):
```python
stok_cup = 10
stok_cup = stok_cup - 3
stok_cup = stok_cup + 5
print(stok_cup)
```
(A) 10 · (B) 12 · (C) Error

Jawaban: **B (12)**.

**Ngomongnya:** "Di matematika, `x = x + 1` itu mustahil. Di Python itu normal banget: *ambil isi toples, tambah 1, masukin lagi ke toples yang sama*. Baca `=` dari **kanan ke kiri**."

**Catatan trainer:** Miskonsepsi `=` sebagai "sama dengan" adalah salah satu miskonsepsi paling umum pada pemula. Tekankan sekarang, karena di Bab 5 akan muncul `==`.

---

### Slide 29 · Isi toples bisa diganti · 🖥️→🧪 · ⏱️ 1,5' · 🟡
**Di layar:** Perbandingan:
```java
// Java: tipe ditulis & dikunci
int omzetJakarta = 4250000;
omzetJakarta = "empat juta";   // ❌ error saat compile
```
```python
# Python: tipe "ditebak" dari isinya (dynamic typing)
omzet_jakarta = 4250000
omzet_jakarta = "empat juta"   # ✅ boleh... tapi bikin bingung
```

**Kode:**
```python
omzet_jakarta = 4250000
print(type(omzet_jakarta))    # <class 'int'>

omzet_jakarta = "empat juta"
print(type(omzet_jakarta))    # <class 'str'>
```

**Ngomongnya:**
- "Kalau kita isi ulang toples dengan nama yang sama, **isi lama hilang**. Boleh, tapi hati-hati."
- "Python menebak tipe data dari isinya. Fleksibel, tapi sebaiknya **jangan ganti-ganti tipe** di satu variabel."
- "`type()` = built-in function buat ngecek isi toples itu jenisnya apa."

---

### Slide 30 · Aturan wajib kasih label · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Di layar:**

| Aturan | ❌ Salah | ✅ Benar | Error-nya |
|---|---|---|---|
| Tidak boleh diawali angka | `2cabang = 3` | `cabang2 = 3` | `SyntaxError: invalid decimal literal` |
| Tidak boleh pakai spasi | `omzet bandung = 875000` | `omzet_bandung = 875000` | `SyntaxError: invalid syntax` |
| Hanya huruf, angka, `_` | `omzet-surabaya = 3520000` | `omzet_surabaya = 3520000` | `SyntaxError: cannot assign to expression here` |
| Bukan *keyword* Python | `class = "A"` | `kelas = "A"` | `SyntaxError: invalid syntax` |
| *Case sensitive* | `Total` ≠ `total` | konsisten | `NameError` kalau salah huruf |

**Kode (lihat daftar keyword):**
```python
import keyword
print(keyword.kwlist)
```

**Ngomongnya:** "Kenapa `omzet-surabaya` salah? Karena tanda `-` dibaca Python sebagai **pengurangan**: 'omzet dikurangi surabaya'. Keyword itu kata-kata yang udah 'dipesan' Python: `if`, `for`, `class`, `True`, dan lain-lain."

**Kamus Error:** tambah **SyntaxError** = "Tata bahasanya salah." Python menolak menjalankan cell sama sekali.

---

### Slide 31 · Jebakan: boleh, tapi bikin celaka · 🖥️→🧪 · ⏱️ 1,5' · 🟡
**Di layar:** 📖 "Raka pernah bikin variabel `max` buat nyimpen omzet tertinggi. 10 menit kemudian..."

**Kode:**
```python
max = 4250000          # Raka nyimpen omzet tertinggi
print(max)             # jalan normal: 4250000

print(max(3, 7, 5))    # ❌ TypeError: 'int' object is not callable
```

**Ngomongnya:** "Nama function bawaan **bukan** keyword, jadi Python **mengizinkan** dipakai sebagai nama variabel. Tapi akibatnya mesin `max` aslinya ketimpa sama angka. Toples dikasih label 'mesin kopi', mesinnya jadi hilang."

**Perbaikan, sekalian kenalan `del`:**
```python
del max               # hapus variabel buatan kita
print(max(3, 7, 5))   # ✅ 7 (mesin aslinya kembali)
```

**Ngomongnya:** "`del` dipakai untuk menghapus variabel. Setelah dihapus, kalau dipanggil lagi → `NameError`."

**Tips:** Hindari nama `max`, `min`, `sum`, `list`, `str`, `print`, `type`, `input`. Di Colab/VSCode, nama bawaan biasanya **berwarna beda**. Kalau nama variabelmu berubah warna, ganti namanya.

---

### Slide 32 · Konvensi: biar rapi & dimengerti orang lain · 🖥️ SLIDE · ⏱️ 1' · 🟢
**Di layar:** Konvensi resmi komunitas Python (**PEP 8**):

| Jenis | Gaya | Contoh |
|---|---|---|
| Variabel | `snake_case` | `omzet_jakarta`, `jumlah_cabang` |
| Konstanta (nilai tetap) | `UPPER_CASE` | `TARGET_HARIAN = 10_000_000` |
| Class (nanti) | `PascalCase` | `LaporanHarian` |

Nama jelek vs nama bagus: `x`, `a1`, `data2` ❌ → `omzet_jakarta`, `trx_bandung` ✅

**Ngomongnya:** "Aturan di slide sebelumnya itu **wajib** (kalau dilanggar, error). Konvensi ini **kesepakatan**: nggak error, tapi bikin kode gampang dibaca orang lain, termasuk diri kalian sendiri 3 bulan lagi. Kode itu lebih sering dibaca daripada ditulis."

---

### Slide 33 · 🎯 Latihan Bab 4 · 🎯 HANDS-ON · ⏱️ 4,5' · 🎟️ STEMPEL 4
**➡️ Peserta ke Colab mereka, section `Bab 4 · Toples Berlabel`.**

**Di layar / di cell latihan:**
```python
# 🎯 LATIHAN BAB 4
# 1. Buat variabel: nama toko, namamu (sebagai analis), jumlah cabang
# 2. Buat variabel omzet & transaksi tiap cabang (lihat data kit di bawah)
#    Jakarta : omzet 4250000, transaksi 170
#    Bandung : omzet 2875000, transaksi 125
#    Surabaya: omzet 3520000, transaksi 160
# 3. Buat konstanta target harian: 10000000
# 4. Print semuanya, cek tipenya pakai type()
```

**Pojok Error: tebak dulu, mana yang error dan kenapa? Lalu buktikan.**
```python
cabang_1 = "Jakarta"
1_cabang = "Bandung"
cabang surabaya = "Surabaya"
_catatan = "rahasia"
Omzet = 100
print(omzet)
```

**Jawaban:** baris 2 (diawali angka) & 3 (spasi) → `SyntaxError`; baris 6 → `NameError` (case sensitive). Baris 1, 4, 5 valid.

**Catatan trainer:**
- Karena satu `SyntaxError` membuat seluruh cell tidak jalan, di notebook latihan Pojok Error sudah dipisah **satu cell per baris**: tebak dulu, lalu jalankan satu per satu.
- Variabel dari latihan ini **dipakai lagi di Bab 5**. Peserta yang belum selesai boleh salin dari data kit di section Bab 5.

**➡️ Transisi:** 🎟️ cap stempel 4. "Angka-angka udah masuk toples. Sekarang saatnya **ngitung**."

---

## BAB 5: Ngitung Omzet
**00:57 – 01:12 (15 menit)**
*Angka, operator, built-in function angka, boolean*

### Slide 34 · Peta tipe data · 🖥️ SLIDE · ⏱️ 1'
**Di layar (advance organizer):**

| Kategori | Tipe | Contoh di Kopi Senja | Dibahas di |
|---|---|---|---|
| Numeric | `int` | `170` transaksi | Bab 5 🟢 |
| | `float` | `23395.6` rata-rata | Bab 5 🟢 |
| | `complex` | `3+4j` | Bab 5 ⚪ |
| Boolean | `bool` | `True` (target tercapai) | Bab 5 🟢 |
| Text sequence | `str` | `"Es Kopi Susu"` | Bab 6 🟢 |
| Sequence | `list`, `tuple` | daftar omzet, jam buka | Bab 7 🟢/🟡 |
| Set | `set`, `frozenset` | menu unik | Bab 7 🟡/⚪ |
| Mapping | `dict` | papan menu harga | Bab 7 🟢 |

**Ngomongnya:** "Ini peta semua jenis 'bahan' di Python. Kayak bahan di dapur: biji kopi dihitung per butir (`int`), susu ditakar (`float`), label menu berupa tulisan (`str`), lampu BUKA/TUTUP di pintu (`bool`). Kita kunjungi satu-satu."

---

### Slide 35 · Angka: int, float, complex · 🖥️→🧪 · ⏱️ 1,5' · 🟢 (complex ⚪)
**➡️ 🧪 Colab materi, section `Bab 5 · Ngitung Omzet`.**

**Kode:**
```python
trx_jakarta = 170              # int   : bilangan bulat
rata_rata = 23395.6            # float : bilangan desimal (pakai TITIK, bukan koma)
omzet_jakarta = 4_250_000      # underscore boleh, biar gampang dibaca

print(type(trx_jakarta), type(rata_rata), type(omzet_jakarta))

z = 3 + 4j                     # complex: kenalan aja, jarang dipakai di analisis data
print(type(z))
```

**Ngomongnya:**
- "Desimal di Python pakai **titik**. `23,5` bukan angka desimal."
- "`4_250_000` sama persis dengan `4250000`. Underscore cuma buat mata manusia."
- "`complex` itu bilangan kompleks dari matematika/teknik. Cukup tahu ada."

**Catatan trainer:** Untuk uang Rupiah, pakai `int`. Kalau ditanya kenapa: `0.1 + 0.2` hasilnya `0.30000000000000004` karena cara komputer menyimpan desimal (lihat FAQ).

---

### Slide 36 · Operator: kalkulator Raka · 🖥️→🧪 · ⏱️ 3' · 🟢 (`//` `%` `**`: 🟡)
**Di layar:**

| Operator | Arti | Contoh Kopi Senja | Hasil |
|---|---|---|---|
| `+` | tambah | `omzet_jakarta + omzet_bandung` | `7125000` |
| `-` | kurang | `omzet_jakarta - omzet_bandung` | `1375000` |
| `*` | kali | `25000 * 170` (harga × cup) | `4250000` |
| `/` | bagi (**selalu float**) | `4250000 / 170` | `25000.0` |
| `//` | bagi, dibulatkan ke bawah | `455 // 50` (kardus penuh) | `9` |
| `%` | sisa bagi (modulo) | `455 % 50` (sisa cup) | `5` |
| `**` | pangkat | `1.1 ** 3` | `1.3310000000000004` |

**Kode (ketik sebagian, tanya hasilnya sebelum run):**
```python
total_omzet = omzet_jakarta + omzet_bandung + omzet_surabaya
print(total_omzet)               # 10645000

print(10 / 2)                    # 5.0  ← kok ada .0?

# Cup dikirim per kardus isi 50. Total 455 cup:
print(455 // 50)                 # 9 kardus penuh
print(455 % 50)                  # sisa 5 cup

# Kalau omzet Jakarta naik 10% tiap bulan, 3 bulan lagi berapa?
print(omzet_jakarta * 1.1 ** 3)  # 5656750.000000002
```

**Interaksi:** Sebelum `print(10 / 2)`: "Hasilnya 5 atau 5.0?" Kebanyakan akan jawab 5.

**Ngomongnya:**
- "`/` **selalu** menghasilkan float, walaupun hasil baginya bulat."
- "`//` dan `%` itu pasangan: `//` 'dapat berapa kardus penuh', `%` 'sisanya berapa'."
- "Urutan operasi kayak matematika SD: `**` dulu, lalu `* / // %`, lalu `+ -`. Kalau ragu, pakai **kurung**."

**Catatan trainer:** `%` tidak ada di outline asli, tapi sangat sering dipakai dan berpasangan alami dengan `//`.

---

### Slide 37 · Built-in function untuk angka · 🖥️→🧪 · ⏱️ 2' · 🟢
**Kode:**
```python
print(abs(omzet_bandung - omzet_jakarta))   # 1375000 (selisih tanpa minus)
print(round(23395.6043))                    # 23396
print(round(23395.6043, 1))                 # 23395.6
print(max(omzet_jakarta, omzet_bandung, omzet_surabaya))   # 4250000
print(min(omzet_jakarta, omzet_bandung, omzet_surabaya))   # 2875000
print(int(3.99))                            # 3  ← dipotong, BUKAN dibulatkan!
print(float(170))                           # 170.0
```

**Interaksi:** Sebelum `int(3.99)`: "3 atau 4?"

**Cara mancing sendiri (penting!):**
```python
round?          # di Colab/Jupyter: muncul dokumentasi
help(round)     # bisa di mana saja
```

**Ngomongnya:** "Kalian **nggak perlu hafal** semua function. Yang penting tahu cara nyari: `?` di notebook, `help()`, Google, atau tanya AI. Programmer profesional pun buka dokumentasi tiap hari."

---

### Slide 38 · Boolean: lampu BUKA/TUTUP · 🖥️→🧪 · ⏱️ 2,5' · 🟢
**Di layar:** Ilustrasi papan "BUKA / TUTUP" di pintu kedai. **Boolean cuma punya 2 nilai: `True` dan `False`** (huruf depan **kapital**!).

| Perbandingan | Arti |
|---|---|
| `==` | sama dengan |
| `!=` | tidak sama dengan |
| `>` `<` | lebih besar / lebih kecil |
| `>=` `<=` | lebih besar/kecil atau sama dengan |

**Kode:**
```python
print(omzet_jakarta > omzet_surabaya)   # True
print(total_omzet >= TARGET_HARIAN)     # True  ← target tercapai!
print(trx_bandung != 125)               # False
print(type(True))                       # <class 'bool'>

print(true)                             # ❌ sengaja: huruf kecil
```

**Ngomongnya:**
- "**`=` itu memasukkan ke toples. `==` itu bertanya 'apakah sama?'.** Ini sumber error nomor satu pemula."
- "`true` huruf kecil → `NameError`. Python cuma kenal `True` dan `False`."

---

### Slide 39 · Gabungin kondisi: and, or, not · 🖥️→🧪 · ⏱️ 1' · 🟡
**Di layar:**

| Operator | Benar kalau... |
|---|---|
| `and` | **dua-duanya** True |
| `or` | **salah satu** True |
| `not` | membalik True ↔ False |

**Kode:**
```python
# Target tercapai DAN Bandung di atas 3 juta?
print(total_omzet >= TARGET_HARIAN and omzet_bandung > 3_000_000)   # False

# Target tercapai ATAU Bandung di atas 3 juta?
print(total_omzet >= TARGET_HARIAN or omzet_bandung > 3_000_000)    # True

print(not True)                                                      # False
```

**Ngomongnya (teaser):** "Sekarang boolean cuma bisa jawab benar/salah. Di pertemuan berikutnya, boolean ini jadi **otak** program: *'kalau target nggak tercapai, kirim peringatan ke Bu Sari'*. Itu pakai `if`, kode yang tadi kalian tebak di awal."

---

### Slide 40 · 🎯 Latihan Bab 5 · 🎯 HANDS-ON · ⏱️ 4' · 🎟️ STEMPEL 5
**➡️ Peserta ke section `Bab 5 · Ngitung Omzet`** (data kit angka sudah ada di cell pertama, tinggal run).

```python
# 🎯 LATIHAN BAB 5
# 1. Hitung total omzet 3 cabang
# 2. Hitung total transaksi 3 cabang
# 3. Hitung rata-rata omzet per transaksi, bulatkan tanpa desimal
# 4. Hitung selisih omzet tertinggi & terendah (pakai max dan min)
# 5. Apakah target harian tercapai? (hasilnya True/False)
# 🟡 Bonus: berapa persen capaian target?
# 🔴 Tantangan: cup dikirim per kardus isi 50. Untuk total transaksi
#    semua cabang, butuh berapa kardus penuh dan sisa berapa cup?
```

**Kunci:** `10645000` · `455` · `23396` · `1375000` · `True` · `106.45` · `9` kardus sisa `5`

**Tebak output cepat** (setelah latihan, angkat 1/2/3 jari):
```python
print(7 // 2, 7 % 2)
```
(1) `3.5 0` · (2) `3 1` · (3) `3 0.5` → Jawaban: **(2)**

**➡️ Transisi:** 🎟️ cap stempel 5. "Angka beres! Tapi Raka masih punya masalah besar: nama menu yang berantakan. Kita istirahat dulu."

---

### Slide 41 · ⏸️ Istirahat 10 menit · ⏸️ ISTIRAHAT · 01:12 – 01:22
**Di layar:** Timer 10 menit + **teaser puzzle**:
```python
print("10" + "5")
print(10 + 5)
```
"Kenapa hasilnya beda? Jawabannya setelah istirahat."

**Catatan trainer:** Pakai waktu ini untuk menghampiri peserta yang tadi 🔴. Cek apakah semua sudah sampai latihan Bab 5.

---

## BAB 6: Beresin Nama Menu
**01:22 – 01:42 (20 menit)**
*String, indexing, slicing, method, casting*

### Slide 42 · 📖 Tiga kasir, tiga gaya nulis · 🖥️→🧪 · ⏱️ 1,5'
**Di layar:**
```
Kasir Jakarta  : "  es kopi SUSU gula aren "
Kasir Bandung  : "ES KOPI SUSU GULA AREN"
Kasir Surabaya : "Es Kopi susu Gula Aren   "
```
"Buat manusia: menu yang sama. Buat komputer: **tiga menu berbeda**."

**➡️ 🧪 Colab materi, section `Bab 6 · Beresin Nama Menu`.**
```python
menu_kasir_jkt = "  es kopi SUSU gula aren "
menu_kasir_bdg = "ES KOPI SUSU GULA AREN"
print(menu_kasir_jkt == menu_kasir_bdg)    # False 😱
```

**Ngomongnya:** "Jawaban teaser tadi: `"10" + "5"` itu **teks digabung**, makanya `"105"`. Hari ini kita kenalan sama teks (`str`), dan di akhir bab ini, `False` tadi akan berubah jadi `True`."

---

### Slide 43 · String: untaian karakter · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Kode:**
```python
nama_toko = "Kopi Senja"        # kutip dua
slogan = 'Seduh rasa, pulang bahagia'   # kutip satu, sama saja
alamat = """Jl. Senja No. 7
Jakarta Selatan"""              # kutip tiga: bisa banyak baris

print("Kopi" + " " + "Senja")   # gabung (concatenation)
print("=" * 30)                 # ulang 30 kali → garis pemisah laporan!
print(len(nama_toko))           # 10 → jumlah karakter (spasi dihitung)
```

**Ngomongnya:** "Kutip satu atau dua sama saja, yang penting konsisten. `"=" * 30` ini nanti kita pakai buat garis di laporan Bu Sari."

---

### Slide 44 · Indexing: setiap karakter punya nomor · 🖥️→🧪 · ⏱️ 2' · 🟢
**Di layar (visual utama bab ini):**
```
kode_trx = "TRX-20261005-JKT-0170"

 karakter:  T   R   X   -   2   0   2   6   1   0   0   5   -   J   K   T   -   0   1   7   0
 index +:   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
 index -: -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```
Struktur kode: `TRX` - `tanggal` - `kode cabang` - `nomor urut transaksi`

**Kode:**
```python
kode_trx = "TRX-20261005-JKT-0170"
print(kode_trx[0])      # T   ← index mulai dari 0!
print(kode_trx[-1])     # 0   ← minus = hitung dari belakang
print(len(kode_trx))    # 21
print(kode_trx[21])     # ❌ IndexError: string index out of range
```

**Interaksi:** Sebelum baris terakhir: "Panjangnya 21, berarti index terakhir berapa?" (20, bukan 21)

**Ngomongnya:** "Kenapa mulai dari 0? Anggap index itu **jarak dari awal**. Huruf pertama jaraknya 0 langkah dari awal."

**Kamus Error:** tambah **IndexError** = "Nomor urutnya kelewatan."

---

### Slide 45 · Slicing: motong teks · 🖥️→🧪 · ⏱️ 2,5' · 🟢
**Di layar:**
```
teks[start:stop]   → ambil dari start, sampai SEBELUM stop
```
Mental model: **"Bayangkan pisau memotong DI ANTARA karakter."** Angka di slicing = posisi pisau.
```
   | T | R | X | - | 2 | 0 | ...
   0   1   2   3   4   5   6
   ↑           ↑
 [0:3] → "TRX"
```

**Kode:**
```python
print(kode_trx[0:3])     # TRX
print(kode_trx[:3])      # TRX   ← start kosong = dari awal
print(kode_trx[4:12])    # 20261005 (tanggal)
print(kode_trx[13:16])   # JKT (kode cabang)
print(kode_trx[-4:])     # 0170  ← stop kosong = sampai akhir
```

**Interaksi:** "Ambilkan tahunnya saja (`2026`), index berapa sampai berapa?" → `kode_trx[4:8]`

**Ngomongnya:** "Kenapa stop-nya nggak ikut? Biar gampang ngitung: `[4:12]` panjangnya pasti `12 - 4 = 8` karakter, pas buat tanggal `20261005`."

---

### Slide 46 · Slicing dengan langkah · 🖥️→🧪 · ⏱️ 1' · 🟡
**Di layar:** `teks[start:stop:step]`, step = loncat berapa langkah.

**Kode:**
```python
angka = "0123456789"
print(angka[::2])      # 02468 → loncat 2 (genap)
print(angka[1::2])     # 13579 → mulai index 1, loncat 2 (ganjil)
print(kode_trx[::-1])  # 0710-TKJ-50016202-XRT → dibalik!
```

**Ngomongnya:** "`[::-1]` itu trik terkenal buat membalik teks. Step jarang dipakai sehari-hari, cukup tahu cara bacanya."

---

### Slide 47 · String itu immutable · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Di layar:** "**Immutable** = tidak bisa diubah sebagian. Kayak tulisan yang dicetak di gelas: mau ganti, cetak gelas baru."

**Kode:**
```python
kode_trx[0] = "X"     # ❌ TypeError: 'str' object does not support item assignment

kode_baru = kode_trx.replace("JKT", "BDG")   # ✅ bikin string BARU
print(kode_baru)      # TRX-20261005-BDG-0170
print(kode_trx)       # TRX-20261005-JKT-0170 ← yang lama tetap
```

**Kamus Error:** tambah **TypeError** = "Tipe datanya nggak cocok untuk operasi ini."

---

### Slide 48 · String method: alat beres-beres teks · 🖥️→🧪 · ⏱️ 3' · 🟢
**Di layar:**

| Method | Fungsi | Contoh → Hasil |
|---|---|---|
| `.strip()` | buang spasi di kiri-kanan | `"  latte  ".strip()` → `"latte"` |
| `.lower()` / `.upper()` | huruf kecil / besar semua | `"Latte".upper()` → `"LATTE"` |
| `.title()` | Huruf Depan Kapital | `"es kopi".title()` → `"Es Kopi"` |
| `.replace(a, b)` | ganti a dengan b | `"JKT".replace("J", "B")` → `"BKT"` |
| `.split(pemisah)` | pecah jadi list | `kode_trx.split("-")` → `['TRX', '20261005', 'JKT', '0170']` |
| `.count(x)` | hitung kemunculan | `"latte".count("t")` → `2` |
| `.startswith(x)` | diawali x? | `kode_trx.startswith("TRX")` → `True` |
| `.center(n)` | taruh di tengah selebar n | dipakai buat judul laporan |

**Kode: momen "aha" bab ini**
```python
menu_kasir_sby = "Es Kopi susu Gula Aren   "

bersih_jkt = menu_kasir_jkt.strip().title()   # method bisa DIRANTAI
bersih_bdg = menu_kasir_bdg.strip().title()
bersih_sby = menu_kasir_sby.strip().title()

print(bersih_jkt)                    # Es Kopi Susu Gula Aren
print(bersih_jkt == bersih_bdg)      # True 🎉
```

**Jebakan (tebak output):**
```python
menu = "  latte  "
menu.upper()
print("[" + menu + "]")   # kurung siku biar spasinya kelihatan
```
(A) `[LATTE]` · (B) `[  LATTE  ]` · (C) `[  latte  ]` → Jawaban: **(C)**!

**Ngomongnya:** "Ingat: string immutable. Method **nggak mengubah** aslinya, tapi **mengembalikan string baru**. Kalau mau disimpan: `menu = menu.upper()`."

**Cara cari method lain:** ketik `menu.` lalu tekan **Tab** di Colab, atau `dir(str)`, atau `str.replace?`.

**Catatan trainer:** `.split()` menghasilkan **list**, jembatan ke Bab 7: "Kurung siku ini namanya list, kita bahas sebentar lagi."

---

### Slide 49 · Casting: ganti jenis bahan · 🖥️→🧪 · ⏱️ 1,5' · 🟢
**Di layar:** "Data dari file atau input sering datang sebagai **teks**, walaupun isinya angka."

**Kode:**
```python
nomor = kode_trx[-4:]
print(nomor, type(nomor))       # 0170 <class 'str'>

nomor_int = int(nomor)
print(nomor_int, type(nomor_int))   # 170 <class 'int'> ← nol di depan hilang

print(str(170) + " transaksi")  # angka → teks
print(float("23.5"))            # 23.5
print(int("17O"))               # ❌ ValueError (itu huruf O, bukan nol!)
```

**Ngomongnya:** "Kasir kadang ngetik huruf O, bukan angka 0. Python langsung protes: tipenya benar (teks), tapi **isinya** nggak bisa jadi angka."

**Kamus Error:** tambah **ValueError** = "Tipenya benar, nilainya nggak masuk akal."

---

### Slide 50 · 🎯 Latihan Bab 6 · 🎯 HANDS-ON · ⏱️ 5,5' · 🎟️ STEMPEL 6
**➡️ Peserta ke section `Bab 6 · Beresin Nama Menu`** (data kit string sudah ada, tinggal run; jangan diketik ulang supaya spasinya tidak berubah).

```python
# 🎯 LATIHAN BAB 6
# 1. Bersihkan ketiga nama menu jadi "Es Kopi Susu Gula Aren"
# 2. Buktikan ketiganya sama setelah dibersihkan (pakai == dan and)
# 3. Dari kode_trx, ambil: tanggal "20261005", kode cabang "JKT", nomor "0170"
# 4. Ubah nomor transaksi jadi angka 170
# 🟡 Bonus: tampilkan tanggal dengan format "05-10-2026"
#    (hint: slicing + gabung string dengan +)
# 🔴 Tantangan: ada berapa huruf "a" di nama menu yang sudah bersih?
#    (hint: .lower() lalu .count())
```

**Kunci:**
```python
bersih_jkt = menu_kasir_jkt.strip().title()
bersih_bdg = menu_kasir_bdg.strip().title()
bersih_sby = menu_kasir_sby.strip().title()
print(bersih_jkt == bersih_bdg and bersih_bdg == bersih_sby)   # True

print(kode_trx[4:12], kode_trx[13:16], kode_trx[-4:])
print(int(kode_trx[-4:]))                                      # 170

print(kode_trx[10:12] + "-" + kode_trx[8:10] + "-" + kode_trx[4:8])   # 05-10-2026
print(bersih_jkt.lower().count("a"))                           # 2
```

**➡️ Transisi:** 🎟️ cap stempel 6. "Teks udah rapi. Tapi Raka mulai sadar ada masalah lain..."

---

## BAB 7: Wadah Banyak Barang
**01:42 – 01:52 (10 menit)**
*list, tuple, set, dict*

### Slide 51 · 📖 "Kalau cabangnya 30?" → list · 🖥️→🧪 · ⏱️ 3,5' · 🟢
**Di layar:** "Kopi Senja buka 30 cabang. Berarti `omzet_jakarta`, `omzet_bandung`, ... 30 variabel? Plus 30 variabel transaksi?" 😵
→ **List** = **antrean pesanan**: urut, bisa ditambah, bisa diubah.

**➡️ 🧪 Colab materi, section `Bab 7 · Wadah Banyak Barang`.**
```python
cabang = ["Jakarta", "Bandung", "Surabaya"]
omzet  = [4_250_000, 2_875_000, 3_520_000]

print(omzet[0])        # 4250000  ← indexing SAMA PERSIS kayak string!
print(omzet[-1])       # 3520000
print(cabang[0:2])     # ['Jakarta', 'Bandung'] ← slicing juga sama

print(len(omzet))      # 3
print(sum(omzet))      # 10645000
print(max(omzet), min(omzet))
print(sorted(omzet, reverse=True))   # urut dari terbesar

omzet[1] = 2_900_000         # koreksi data Bandung → list BISA diubah
cabang.append("Yogyakarta")  # buka cabang baru
print(cabang)
```

**Interaksi:** Sebelum `omzet[0]`: "Kalian udah tahu caranya dari Bab 6. Tebak hasilnya?"

**Ngomongnya:**
- "Semua yang kalian pelajari soal indexing string **berlaku juga di list**. Ilmunya nggak hilang, dipakai lagi."
- "Bedanya: string **immutable**, list **mutable**, bisa diubah isinya."
- "`sum()` di list ini andalan Raka: 30 cabang pun tetap satu baris."

**Catatan trainer:** Kembalikan `omzet[1]` ke `2_875_000` kalau notebook trainer mau dipakai ulang untuk final.

---

### Slide 52 · Tuple: data yang dikunci · 🖥️→🧪 · ⏱️ 1' · 🟡
**Kode:**
```python
JAM_OPERASIONAL = (7, 22)        # buka jam 7, tutup jam 22
LOKASI_JKT = (-6.2, 106.8)       # koordinat: nggak boleh berubah

print(JAM_OPERASIONAL[0])        # 7
JAM_OPERASIONAL[0] = 8           # ❌ TypeError: 'tuple' object does not support item assignment
```

**Ngomongnya:** "Tuple itu kayak list yang **dikunci**. Pakai kurung biasa. Cocok buat data yang memang **nggak boleh berubah**."

---

### Slide 53 · Set: hanya yang unik · 🖥️→🧪 · ⏱️ 1,5' · 🟡 (frozenset ⚪)
**Kode:**
```python
menu_terjual = ["kopi susu", "latte", "kopi susu", "americano", "latte"]
menu_unik = set(menu_terjual)
print(menu_unik)          # {'latte', 'kopi susu', 'americano'} (urutan bisa beda!)
print(len(menu_unik))     # 3 → ada 3 jenis menu yang terjual

menu_tetap = frozenset(["kopi susu", "latte"])   # set yang dikunci (kenalan aja)
```

**Ngomongnya:** "Set otomatis **membuang duplikat** dan **tidak punya urutan**, jadi nggak bisa diakses pakai index. Frozenset = set yang nggak bisa diubah, cukup tahu."

---

### Slide 54 · Dict: papan menu · 🖥️→🧪 · ⏱️ 2' · 🟢
**Di layar:** Ilustrasi papan menu di dinding: **nama menu → harga**. `{kunci: nilai}`

**Kode:**
```python
harga = {
    "kopi susu": 25000,
    "latte": 28000,
    "americano": 22000,
}
print(harga["latte"])           # 28000 → akses pakai KUNCI, bukan nomor
harga["matcha latte"] = 30000   # tambah menu baru
print(harga)

print(harga["teh tarik"])       # ❌ KeyError: 'teh tarik'

omzet_cabang = {"Jakarta": 4_250_000, "Bandung": 2_875_000, "Surabaya": 3_520_000}
print(omzet_cabang["Bandung"])          # 2875000
print(sum(omzet_cabang.values()))       # 10645000
```

**Ngomongnya:** "Di list, kita nyari pakai nomor urut. Di dict, kita nyari pakai **nama**. Kayak papan menu: kita nggak bilang 'menu nomor 2', tapi 'latte berapa?'."

**Kamus Error:** tambah **KeyError** = "Kunci ini nggak ada di dict."

---

### Slide 55 · Pilih wadah yang tepat · 🖥️ SLIDE · ⏱️ 2' · 🎟️ STEMPEL 7
**Di layar:**

| Wadah | Tanda | Urut? | Bisa diubah? | Boleh duplikat? | Analogi |
|---|---|---|---|---|---|
| `list` | `[ ]` | ✅ | ✅ | ✅ | Antrean pesanan |
| `tuple` | `( )` | ✅ | ❌ | ✅ | Jam buka di pintu |
| `set` | `{ }` | ❌ | ✅ | ❌ | Daftar jenis menu terjual |
| `dict` | `{k: v}` | ✅* | ✅ | kunci ❌ | Papan menu |

*\*dict menyimpan urutan dimasukkan (Python 3.7+)*

**Interaksi: kuis cepat** (jawab serentak / di chat):
1. Daftar semua transaksi hari ini, urut waktu → **list**
2. Koordinat lokasi cabang → **tuple**
3. Daftar pelanggan unik (tanpa dobel) → **set**
4. Stok bahan berdasarkan nama bahan (`"susu": 12`) → **dict**

**➡️ Transisi:** 🎟️ cap stempel 7. "Semua data udah rapi di wadahnya. Tinggal satu: **menyajikan** laporannya ke Bu Sari."

---

## BAB 8: Laporan buat Bu Sari
**01:52 – 02:07 (15 menit)**
*print lanjutan, escape character, string formatting, input*

### Slide 56 · print() lebih jauh & escape character · 🖥️→🧪 · ⏱️ 2' · 🟡
**➡️ 🧪 Colab materi, section `Bab 8 · Laporan buat Bu Sari`.**

**Di layar:**

| Escape | Arti |
|---|---|
| `\n` | baris baru |
| `\t` | tab (rata kolom) |
| `\"` `\'` | tanda kutip di dalam teks |
| `\\` | garis miring terbalik |

**Kode:**
```python
print("Jakarta", "Bandung", "Surabaya", sep=" | ")   # Jakarta | Bandung | Surabaya
print("Laporan \"Kopi Senja\"\nTanggal:\t05-10-2026")
```
Output:
```
Jakarta | Bandung | Surabaya
Laporan "Kopi Senja"
Tanggal:	05-10-2026
```

**Catatan trainer (jebakan klasik, ceritakan saja):** `print("C:\data\new")` mencetak `C:\data` lalu baris baru dan `ew`, karena `\n` dianggap baris baru. Solusi: `"C:\\data\\new"` atau raw string `r"C:\data\new"`.

---

### Slide 57 · 📖 Raka mencoba bikin laporan... · 🖥️→🧪 · ⏱️ 1'
**Kode:**
```python
total_omzet = 10645000
print("Total omzet: " + total_omzet)
# ❌ TypeError: can only concatenate str (not "int") to str
```

**Ngomongnya:** "Teks + angka = nggak bisa. Kayak nyampur gula sama tulisan 'gula'. Gimana solusinya? Ternyata Python punya beberapa cara dari zaman ke zaman."

---

### Slide 58 · Evolusi string formatting · 🖥️ SLIDE · ⏱️ 2' · 🟢 f-string · ⚪ `%` & `.format`
**Di layar (semua menghasilkan `Total omzet: 10645000`):**
```python
print("Total omzet: " + str(total_omzet))        # 1. casting manual    → ribet
print("Total omzet: %d" % total_omzet)           # 2. gaya %  (jadul)   → masih ketemu di kode lama
print("Total omzet: {}".format(total_omzet))     # 3. .format()         → masih ketemu di kode lama
print(f"Total omzet: {total_omzet}")             # 4. f-string ⭐        → pakai ini!
```

**Ngomongnya:** "Kalian perlu **kenal** cara 2 dan 3 karena masih sering muncul di kode orang lain atau di internet. Tapi kalau nulis sendiri, pakai **f-string**: huruf `f` di depan kutip, variabel di dalam kurung kurawal `{ }`."

---

### Slide 59 · Kekuatan super f-string · 🖥️→🧪 · ⏱️ 3' · 🟢
**Di layar:**

| Format | Contoh | Hasil |
|---|---|---|
| Variabel | `f"{nama_toko}"` | `Kopi Senja` |
| Ekspresi/hitungan | `f"{total_omzet / 455}"` | `23395.604395604394` |
| Pemisah ribuan | `f"{total_omzet:,}"` | `10,645,000` |
| 2 angka desimal | `f"{106.4512:.2f}"` | `106.45` |
| Method di dalamnya | `f"{nama_toko.upper()}"` | `KOPI SENJA` |

**Kode:**
```python
persen_target = total_omzet / TARGET_HARIAN * 100

print(f"Total omzet : Rp{total_omzet:,}")                    # Rp10,645,000 (gaya Inggris)
print(f"Total omzet : Rp{total_omzet:,}".replace(",", "."))  # Rp10.645.000 (gaya Indonesia!)
print(f"Capaian     : {persen_target:.2f}%")                 # 106.45%
print(f"Tercapai?   : {total_omzet >= TARGET_HARIAN}")       # True
```

**Ngomongnya:** "Perhatikan trik `.replace(",", ".")`: itu **string method dari Bab 6**. Semua yang kita pelajari mulai nyambung."

---

### Slide 60 · input(): biar laporannya bisa diisi · 🖥️→🧪 · ⏱️ 2,5' · 🟢
**Kode:**
```python
nama_analis = input("Nama analis: ")
print(f"Laporan disusun oleh {nama_analis}")
```

**Tebak output (momen paling berkesan, jangan dilewati!):**
```python
trx = input("Jumlah transaksi: ")   # ketik: 10
print(trx * 2)
```
(A) `20` · (B) `1010` · (C) Error → Jawaban: **(B) `1010`**

**Ngomongnya:** "**`input()` selalu menghasilkan string**, apa pun yang diketik. `"10" * 2` = teks diulang 2 kali. Sama kayak teaser sebelum istirahat."

**Perbaikan (casting dari Bab 6):**
```python
trx = int(input("Jumlah transaksi: "))
print(trx * 2)    # 20
```

**Catatan trainer:** Di Colab, `input()` memunculkan kotak isian di bawah cell dan cell terlihat "berputar" sampai kita tekan **Enter**. Pemula sering mengira Colab hang. Kalau benar-benar macet: tombol ■ (interrupt).

---

### Slide 61 · 🎯 Latihan Bab 8 · 🎯 HANDS-ON · ⏱️ 4,5' · 🎟️ STEMPEL 8
**➡️ Peserta ke section `Bab 8 · Laporan buat Bu Sari`.**

```python
# 🎯 LATIHAN BAB 8
# 1. Minta nama analis lewat input(), rapikan pakai .strip().title()
# 2. Cetak header seperti ini:
#    ========================================
#    LAPORAN HARIAN KOPI SENJA
#    Analis : Raka Pratama
#    ========================================
# 3. Cetak total omzet dalam format Rupiah: Rp10.645.000
# 🟡 Bonus: minta target lewat input() lalu hitung persen capaian
```

**Kunci:**
```python
nama_analis = input("Nama analis: ").strip().title()
garis = "=" * 40
print(garis)
print("LAPORAN HARIAN KOPI SENJA")
print(f"Analis : {nama_analis}")
print(garis)
print(f"Total omzet : Rp{total_omzet:,}".replace(",", "."))

target = int(input("Target hari ini: "))
print(f"Capaian : {total_omzet / target * 100:.2f}%")
```

**➡️ Transisi:** 🎟️ cap stempel 8! "8 stempel penuh. Saatnya tukar dengan kopi gratis: **laporan otomatis Raka**."

---

## FINAL: Satu Klik, Laporan Jadi
**02:07 – 02:22 (15 menit)**

### Slide 62 · Misi: Laporan Harian Kopi Senja v1.0 · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** Target output (sama dengan demo di Slide 6):
```
============================================
         LAPORAN HARIAN KOPI SENJA
============================================
Tanggal          : 05-10-2026
Analis           : Raka Pratama
Jam operasional  : 7.00 - 22.00
--------------------------------------------
Omzet per cabang
  Jakarta    : Rp4.250.000 (170 trx)
  Bandung    : Rp2.875.000 (125 trx)
  Surabaya   : Rp3.520.000 (160 trx)
--------------------------------------------
Total omzet      : Rp10.645.000
Total transaksi  : 455
Rata-rata/trx    : Rp23.396
Selisih max-min  : Rp1.375.000
Menu terlaris    : Es Kopi Susu Gula Aren
Trx terakhir     : #170 di cabang JKT
--------------------------------------------
Target harian    : Rp10.000.000
Capaian          : 106.45%
Target tercapai? : True
============================================
Laporan ini dibuat otomatis oleh Python ☕
```

**Level:**
- 🟢 **Wajib**: isi semua `___` di template sampai laporan tampil
- 🟡 **Bonus**: tambah baris "Cabang terbaik: Jakarta" (hint: `cabang[omzet.index(max(omzet))]`)
- 🔴 **Tantangan**: omzet tiap cabang juga diminta lewat `input()`

**Ngomongnya:** "Perhatikan: tiap baris laporan ini pakai sesuatu yang kalian pelajari hari ini. Coba tebak, baris 'Menu terlaris' pakai ilmu dari bab berapa?" (Bab 6)

---

### Slide 63 · 🎯 Kerjakan! · 🎯 HANDS-ON · ⏱️ 10'
**➡️ Peserta ke section `Final · Laporan Harian v1.0`** (template di [bagian 7](#template-peserta)).

**Di layar (biarkan tampil selama peserta bekerja):** "Tangga petunjuk" kalau stuck:
1. 🔎 Cek komentar di template: konsep dari **bab berapa**?
2. 📓 Scroll ke latihan bab itu di notebook-mu sendiri
3. 🙋 Tanya teman sebelah (boleh *pair programming*)
4. 🔴 Angkat sinyal merah, trainer datang

**Catatan trainer:**
- Keliling (atau buka breakout room). Prioritaskan peserta 🔴.
- Yang selesai cepat: arahkan ke 🟡/🔴, atau minta jadi "asisten" bagi teman sebelah.
- Di menit ke-8, umumkan "2 menit lagi".

---

### Slide 64 · Momen "aha": dari notebook ke script · 💻 VSCODE · ⏱️ 3'
**➡️ Pindah ke VSCode**, buka `kopi-senja/laporan.py` (isi kode final, sudah disiapkan).

**Demo:**
```bash
python3 laporan.py
```
Isi nama & tanggal → laporan muncul.

**Ngomongnya (penutup arc cerita):** "Ini yang sekarang dijalankan Raka tiap pagi. Satu perintah. **65 menit jadi 1 detik.** Nggak ada lagi salah ketik nol. Bu Sari dapat laporan yang sama rapinya setiap hari. Dan yang nulis kodenya... kalian."

**Show & tell:** Minta 1–2 peserta share screen hasil mereka (terutama yang mengerjakan bonus). Beri apresiasi.

---

## EPILOG: Bersambung...
**02:22 – 02:30 (8 menit)**

### Slide 65 · Isi kotak perkakas Raka · 🖥️ SLIDE · ⏱️ 2'
**Di layar:**

| Masalah Raka | Alat yang dipakai |
|---|---|
| Angka berserakan | Variabel & konstanta |
| Hitung total, rata-rata, selisih | Operator, `sum`, `max`, `min`, `round` |
| Cek target | Boolean & perbandingan |
| Nama menu berantakan | `.strip()`, `.title()` |
| Ambil info dari kode transaksi | Indexing, slicing, `int()` |
| Data banyak cabang | `list`, `dict` |
| Laporan rapi | f-string, `\t`, `"=" * 40` |
| Laporan bisa diisi | `input()` |
| Error | Baca dari baris paling bawah |

**Interaksi:** "Dari semua ini, mana yang paling bikin kalian 'ooh!'?" (1–2 jawaban)

---

### Slide 66 · 📖 Tapi Raka masih punya masalah... · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** 4 kartu cliffhanger:
1. 😐 "Data omzetnya masih **diketik manual** di kode." → **Baca file Excel/CSV** (pandas)
2. 🚨 "Kalau target **nggak tercapai**, aku mau kasih peringatan otomatis." → **`if` / `else`** (boolean tadi jadi otaknya!)
3. 🔁 "Kalau cabangnya **30**, masa nulis 30 baris print?" → **Loop** (`for`)
4. ♻️ "Aku pengen bikin **mesin sendiri** kayak `print()`." → **Function** buatan sendiri

**Ngomongnya:** "Kalian sendiri ngerasain kan waktu nulis 3 baris print per cabang di final project? Bayangin 30. Itu yang akan kita selesaikan di pertemuan berikutnya. **Bersambung...** ☕"

**Catatan trainer:** Sesuaikan kartu dengan silabus pertemuan berikutnya.

---

### Slide 67 · Latihan mandiri: mulai dari mana? · 🖥️ SLIDE · ⏱️ 2'
**Di layar (urut dari paling ramah pemula):**

| Urutan | Platform | Kenapa | Mulai dari |
|---|---|---|---|
| 1 | [Codesaya](https://codesaya.com/python) | Bahasa Indonesia, interaktif, ramah pemula | Modul Python dasar |
| 2 | [Kaggle Learn: Python](https://www.kaggle.com/learn/python) | Gratis, berbasis notebook, orientasi data | Lesson 1–2 |
| 3 | [HackerRank](https://www.hackerrank.com/domains/python) | Soal bertingkat + auto-check | Introduction, Basic Data Types, Strings |
| 4 | [LeetCode](https://leetcode.com) | Soal algoritma | **Nanti dulu**, setelah paham `if`, loop, function |

**PR (opsional tapi disarankan):**
> Tambahkan ke Laporan Harian v1.0:
> 1. Baris "Cabang terbaik" & "Cabang terlemah"
> 2. Persentase kontribusi Jakarta terhadap total omzet (2 desimal)
> 3. Data cabang ke-4 (Yogyakarta, omzet 1.980.000, 88 transaksi). Rasakan berapa baris yang harus kamu ubah. Itu bekal diskusi pertemuan berikutnya.

**Catatan trainer:** PR nomor 3 sengaja membuat peserta *merasakan* sakitnya tanpa loop, jadi motivasi alami untuk materi berikutnya.

---

### Slide 68 · Exit ticket 3-2-1 · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** QR / link form:
- **3** hal yang aku pelajari hari ini
- **2** hal yang masih bikin bingung
- **1** pertanyaan yang masih ingin aku tanyakan

**Catatan trainer:** Baca jawaban "2 hal bingung" sebelum pertemuan berikutnya. Topik yang paling sering muncul → buka pertemuan berikutnya dengan review 5 menit soal itu.

---

### Slide 69 · Terima kasih & Q&A · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** Kartu stempel penuh 8/8 + ☕ "Kopi gratis sudah ditukar!" · Kontak trainer · Link komunitas PythonID · Link notebook & slide.

**Ngomongnya:** "Hari ini kalian udah nulis program pertama yang benar-benar berguna. Error akan terus datang. Itu tanda kalian sedang belajar, bukan tanda kalian nggak bisa."

---

## 7. Kode final + template peserta

### Kode final (kunci jawaban, sudah dites)
Ada di [kopi-senja/laporan.py](kopi-senja/laporan.py) (VSCode), section `00 · Demo Final` di `01_materi_kopi_senja.ipynb`, dan section `Final` di `03_kunci_jawaban.ipynb`.

```python
# ==============================================
# Laporan Harian Kopi Senja v1.0
# Penulis: Raka (dan kamu!)
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
```

**Kunci bonus 🟡:**
```python
cabang_terbaik = cabang[omzet.index(max(omzet))]
print(f"Cabang terbaik   : {cabang_terbaik}")    # Jakarta
```

### Template peserta
Sudah ada di section `Final · Laporan Harian v1.0` pada `02_latihan_peserta.ipynb` dan di [kopi-senja/laporan_template.py](kopi-senja/laporan_template.py). Bagian 1–3 sudah diisi supaya fokus ke logika; peserta mengisi `___`.

```python
# ==============================================
# Laporan Harian Kopi Senja v1.0
# Penulis: ___ (ganti dengan namamu)
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
total_omzet = ___                 # TODO: jumlahkan semua omzet            [Bab 7]
total_transaksi = ___             # TODO: jumlahkan semua transaksi        [Bab 7]
rata_rata = ___                   # TODO: total omzet / total trx, dibulatkan [Bab 5]
selisih = ___                     # TODO: omzet tertinggi - terendah       [Bab 5]
persen_target = ___               # TODO: total omzet / target * 100       [Bab 5]
target_tercapai = ___             # TODO: apakah total omzet >= target?    [Bab 5]

menu_terlaris = ___               # TODO: rapikan menu_terlaris_mentah     [Bab 6]
kode_cabang = ___                 # TODO: ambil "JKT" dari kode trx        [Bab 6]
nomor_trx = ___                   # TODO: ambil "0170", ubah jadi angka    [Bab 6]

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
```

**Catatan trainer:** Kalau peserta menjalankan template yang belum lengkap, `___` akan memicu `NameError: name '___' is not defined`. Itu justru penanda "masih ada yang belum diisi". Sampaikan di awal Slide 63.

---

## 8. Kamus Error

Tampilkan bertahap selama kelas (entri ditambah saat error itu pertama muncul). Di akhir kelas, peserta sudah "kenal" 7 error.

| Error | Bahasa manusianya | Muncul di | Contoh | Biasanya karena |
|---|---|---|---|---|
| `NameError` | "Aku nggak kenal nama ini" | Slide 15, 23, 27 | `prnt(...)`, `print(Kopi)`, `true` | Typo, lupa kutip, cell belum di-run, huruf besar/kecil |
| `SyntaxError` | "Tata bahasanya salah" | Slide 30, 33 | `2cabang = 3`, `omzet bandung = ...` | Melanggar aturan penulisan, kurung/kutip tidak ditutup |
| `IndentationError` | "Ada spasi nyasar di awal baris" | (antisipasi) | `   print("hai")` | Copy-paste dari web/chat |
| `TypeError` | "Tipenya nggak cocok untuk operasi ini" | Slide 31, 47, 52, 57 | `"Total: " + 10645000`, `kode_trx[0] = "X"` | Campur teks & angka, mengubah yang immutable, nama built-in ketimpa |
| `IndexError` | "Nomor urutnya kelewatan" | Slide 44 | `kode_trx[21]`, `omzet[3]` | Lupa index mulai dari 0 |
| `ValueError` | "Tipenya benar, nilainya nggak masuk akal" | Slide 49 | `int("17O")` | Konversi teks yang bukan angka |
| `KeyError` | "Kunci ini nggak ada di dict" | Slide 54 | `harga["teh tarik"]` | Typo / kunci memang belum ada |

**Tentang `IndentationError`:** Kalau muncul (biasanya saat peserta paste kode dari chat), jelaskan: *"Di Python, spasi di awal baris itu bermakna, nanti dipakai di `if` dan loop. Untuk sekarang, semua baris mulai dari paling kiri."*

---

## 9. FAQ trainer

**"Sekarang kan ada AI yang bisa ngoding. Ngapain belajar?"**
AI adalah asisten yang hebat, tapi kalian tetap harus bisa **membaca, mengecek, dan memperbaiki** kodenya. Tanpa paham dasar, kalian nggak bisa tahu kode dari AI itu benar atau salah, persis seperti nggak bisa mengecek laporan keuangan kalau nggak paham akuntansi. Fundamental bikin kalian jadi "pemberi perintah" yang baik untuk AI.

**"Python lambat ya?"**
Dibanding C, iya, untuk eksekusi murni. Tapi library data populer (numpy, pandas) di dalamnya ditulis dengan C, jadi tetap cepat. Untuk data analyst, yang lebih penting adalah **cepat sampai ke jawaban**, dan di situ Python unggul.

**"Python 2 atau 3?"**
Selalu Python 3. Python 2 sudah pensiun sejak 2020.

**"Harus hafal semua function & method?"**
Tidak. Cukup tahu *ada*, lalu tahu cara mencarinya: `?`, `help()`, Tab di Colab, dokumentasi, Google, AI.

**"Kenapa `0.1 + 0.2` hasilnya `0.30000000000000004`?"**
Komputer menyimpan desimal dalam basis 2, dan beberapa desimal (seperti 0.1) tidak bisa disimpan persis. Ini terjadi di hampir semua bahasa pemrograman. Untuk uang: pakai `int` (Rupiah) atau modul `decimal`; untuk tampilan: bulatkan dengan `round()` atau f-string `:.2f`.

**"Kenapa `round(2.5)` hasilnya 2, bukan 3?"**
Python memakai *banker's rounding*: angka .5 dibulatkan ke **genap** terdekat (`round(2.5)` → 2, `round(3.5)` → 4). Tujuannya mengurangi bias pembulatan di data besar.

**"Kenapa `True + True` hasilnya 2?"**
Di Python, `bool` adalah turunan `int`: `True` = 1, `False` = 0. Berguna untuk menghitung, misalnya berapa cabang yang mencapai target.

**"Python beneran interpreted?"**
Lihat catatan trainer di Slide 14.

**"Bedanya pip dan uv?"**
Dua-duanya package manager. `pip` bawaan Python. `uv` lebih baru, jauh lebih cepat, dan sekaligus bisa mengelola virtual environment & versi Python.

**"Colab vs Jupyter vs VSCode?"**
Colab = Jupyter di cloud milik Google (tanpa install, butuh internet). Jupyter = notebook di laptop sendiri. VSCode = editor serbaguna; bisa membuka file `.py` maupun notebook `.ipynb`.

**"Petik satu atau petik dua?"**
Sama saja. Pakai yang konsisten. Kalau teksnya mengandung petik satu (`Jum'at`), bungkus dengan petik dua, dan sebaliknya.

**"Kenapa `input()` di Colab kayak nyangkut?"**
Colab menunggu kamu mengetik di kotak isian lalu menekan Enter. Kalau benar-benar macet, tekan tombol stop/interrupt di cell.

---

## 10. Rencana cadangan

### Kalau telat (urutan yang dipangkas duluan)
| Telat | Pangkas | Hemat |
|---|---|---|
| ≥ 3' | Slide 46 (step slicing): cukup sebut `[::-1]` | ~1' |
| ≥ 5' | Slide 58: tampilkan saja, tanpa ketik `%` & `.format()` | ~1' |
| ≥ 8' | Slide 52–53 (tuple, set) digabung jadi 1 slide "kenalan", tanpa demo | ~2' |
| ≥ 10' | Slide 16–17 digabung; Slide 20 cukup ditampilkan | ~2' |
| ≥ 15' | Final project: peserta isi bagian 4 saja (olah data), bagian 5 (print) didemokan trainer, sisanya jadi PR | ~5' |

**Yang jangan pernah dipangkas:** Slide 6 (demo hasil akhir), Slide 23 (cara baca error), Slide 28 (`=` bukan sama dengan), Slide 48 (method + jebakan immutable), Slide 60 (tebak `1010`), Slide 64 (momen aha VSCode). Ini tulang punggung pemahaman dan cerita.

### Kalau kecepatan
- Jalankan `import this` dan bahas 2–3 baris Zen of Python
- Eksplorasi `dir(str)`: minta peserta menemukan 1 method baru dan menjelaskannya ke kelas
- Kuis kilat "tebak output" berbentuk kompetisi tim
- Mulai PR nomor 3 di kelas

### Kalau level peserta campur
- Siapkan **"kartu jalur ngebut"** (tantangan 🔴) di setiap latihan supaya peserta berpengalaman tidak bosan
- Pasangkan peserta berpengalaman dengan pemula (*pair programming*: satu mengetik, satu mengarahkan, tukar tiap latihan)
- Minta yang cepat jadi "asisten" di final project: menjelaskan ke teman memperkuat pemahaman mereka sendiri

### Kalau teknis bermasalah
- **Colab lambat / down**: pakai Jupyter lokal / VSCode dengan notebook yang sama (sudah diunduh sebagai `.ipynb`)
- **Internet peserta putus**: pasangkan dengan teman (satu layar berdua)
- **VSCode trainer error saat demo**: tunjukkan di terminal biasa (`python3 laporan.py`), pesannya tetap sama

---

## 11. Catatan perubahan dari outline asli

Supaya kamu tahu apa yang aku ubah dari [python_dbb.md](python_dbb.md) dan alasannya.

### Urutan
| Perubahan | Alasan |
|---|---|
| **"Kenapa perlu coding" dipindah sebelum "Apa itu Python"** | Motivasi dulu, solusi kemudian. Peserta perlu merasakan masalahnya sebelum dikenalkan alatnya |
| **Basic Code diurutkan ulang:** komentar & print → variabel → angka & bool → string → koleksi → formatting & input | `print` & variabel dibutuhkan untuk mencoba apa pun; string sebelum list supaya ilmu indexing bisa dipakai ulang; formatting di akhir karena itu "hadiah" yang menyatukan semuanya |
| **Built-in function disebar** ke bab yang relevan (bukan satu blok) | Function dikenalkan saat dibutuhkan (`type` di variabel, `max/min/round` di angka, `len` di string, `sum` di list) |
| **Hands-on dipecah** jadi kecil-kecil di tiap bab + 1 final project | Aturan 10 menit; latihan langsung setelah konsep lebih efektif daripada satu blok besar di akhir |

### Koreksi istilah
| Di outline | Seharusnya | Catatan |
|---|---|---|
| `boox` | `bool` | typo |
| "Pake true sama false" | `True` / `False` | Huruf depan wajib kapital; `true` → `NameError`. Dijadikan demo error di Slide 38 |
| "bisa di casing juga, int("10")" | **casting** (konversi tipe) | Dipindah ke Slide 49 sebagai konsep sendiri, bukan bagian operasi string |
| "Capital case untuk nama kelas" | **PascalCase** / CapWords | Istilah di PEP 8 |
| "Fradulent" | rawan salah & rawan manipulasi | Dibingkai di Slide 9 |
| "how not to name a variable, reserved: built in function" | Yang benar-benar **reserved** adalah **keyword** (`if`, `class`, `True`, ...). Nama built-in function **boleh** dipakai tapi berbahaya | Dipisah jadi 2 slide: aturan wajib (Slide 30) vs jebakan (Slide 31) |
| "di notebook bisa pake ?" | `?` (khusus notebook) + `help()` (di mana saja) | Ditambah `help()` supaya berlaku juga di VSCode |

### Tambahan
- `sum()`, `sorted()`, `%` (modulo), `.split()`, `.center()`: sangat sering dipakai & dibutuhkan final project
- **Cara membaca error** (Slide 23) + **Kamus Error**: skill paling penting supaya pemula bisa belajar mandiri
- **IndexError** dan **KeyError**: muncul alami saat belajar string/list/dict
- Catatan jebakan notebook: urutan menjalankan cell

### Penyesuaian kedalaman (karena 2,5 jam untuk pemula)
- ⚪ **Kenalan saja**: `complex`, `frozenset`, `%` formatting, `.format()`, nuansa interpreted vs compiled, package manager, virtual env
- 🟢 **Fokus dikuasai**: variabel, int/float/str/bool, operator, indexing/slicing dasar, string method, list & dict, f-string, input + casting
- **LeetCode** diposisikan "nanti dulu": soal-soalnya butuh `if`, loop, dan function, yang belum diajarkan

---

## 12. Lampiran: Cheat sheet peserta

> Bisa dibagikan sebagai 1 halaman PDF atau text cell di akhir notebook.

```python
# ===== CHEAT SHEET PYTHON PERTEMUAN 1 · KOPI SENJA =====

# Komentar: diawali #, dilewati Python
print("Halo", 3)              # tampilkan ke layar
type(170)                     # cek tipe data → int

# VARIABEL: nama = nilai  (snake_case, KONSTANTA pakai UPPER_CASE)
omzet_jakarta = 4_250_000
TARGET_HARIAN = 10_000_000
del omzet_jakarta             # hapus variabel

# ANGKA
10 / 2      # 5.0  (selalu float)
7 // 2      # 3    (bagi bulat)
7 % 2       # 1    (sisa bagi)
2 ** 3      # 8    (pangkat)
abs(-5), round(3.456, 2), max(1, 5, 3), min(1, 5, 3)

# BOOLEAN: True / False (kapital!)
5 > 3, 5 == 5, 5 != 3         # perbandingan  (= masukkan, == bandingkan)
True and False, True or False, not True

# STRING
s = "TRX-20261005-JKT-0170"
s[0], s[-1]                   # index (mulai dari 0)
s[4:12], s[:3], s[-4:]        # slicing [start:stop], stop tidak ikut
s[::-1]                       # dibalik
len(s)                        # panjang
"  latte ".strip().title()    # method bisa dirantai, hasilnya string BARU
s.replace("JKT", "BDG"), s.split("-"), s.lower(), s.upper(), s.count("0")
int("170"), float("23.5"), str(170)   # casting

# KOLEKSI
omzet = [4250000, 2875000, 3520000]   # list : urut, bisa diubah
jam = (7, 22)                         # tuple: urut, dikunci
menu = {"kopi", "latte", "kopi"}      # set  : unik, tanpa urutan
harga = {"latte": 28000}              # dict : kunci → nilai
sum(omzet), len(omzet), sorted(omzet), omzet.append(1980000), harga["latte"]

# OUTPUT & INPUT
print(f"Total: Rp{10645000:,}".replace(",", "."))   # Rp10.645.000
print(f"Capaian: {106.4512:.2f}%")                   # 106.45%
print("Baris1\nBaris2\tTab \"kutip\"")
nama = input("Nama: ")                 # input SELALU string
trx = int(input("Jumlah trx: "))       # ubah ke angka

# BINGUNG?  round?   help(round)   ketik "teks." lalu Tab
# ERROR?    baca baris PALING BAWAH dulu → cek nomor baris → cek typo/kutip/kurung
```
