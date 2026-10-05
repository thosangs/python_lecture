# Alur Slide — Python Fundamentals & Logic
### Pertemuan 1 · 2,5 jam · "Ijazah Raka"

> Dokumen ini pendamping [python_dbb.md](python_dbb.md). Isinya alur per slide, contoh kode (sudah dites di Python 3.12), kapan pindah ke Colab/VSCode, latihan, dan catatan trainer.

---

## Daftar Isi

0. [Cara pakai dokumen ini](#0-cara-pakai-dokumen-ini)
1. [Ceritanya: Ijazah Raka](#1-ceritanya-ijazah-raka)
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

**Deck slide:** https://thosangs.github.io/python_lecture/ (sumber: [slides/slides.md](slides/slides.md)). Nomor slide di dokumen ini **sama persis** dengan nomor di deck. Footer tiap slide sudah menampilkan bab aktif, progres transkrip, dan penanda lokasi (🧪/🎯/💻) beserta section notebook yang harus dibuka. Poin "Ngomongnya" & "Catatan trainer" juga ada di **mode presenter** (`/presenter`).

**Notebook** (folder [notebooks/](notebooks/)):
- `01_materi_ijazah_raka.ipynb`: notebook **trainer** untuk live coding (= "Materi" di footer slide), sudah dijalankan
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
| 🎓 **NILAI A** | Akhir bab, transkrip kelas dapat nilai A (lihat bagian 1) |

**Legend level materi** (biar jelas mana yang harus dikuasai, mana yang cukup dikenalkan):

| Tag | Artinya | Implikasi di kelas |
|---|---|---|
| 🟢 **Wajib** | Harus bisa dipraktikkan di akhir kelas | Ada latihan, muncul di final project |
| 🟡 **Paham** | Ngerti konsepnya, belum harus lancar | Demo + 1 contoh |
| ⚪ **Kenalan** | Cukup tahu "ada" | 1 kalimat + 1 contoh, jangan didalami |

**Format tiap slide:**
- **Di layar**: apa yang tampil di slide
- **Ngomongnya**: poin bicara / skrip (dalam tanda kutip = kalimat yang bisa langsung kamu pakai)
- **Kode**: yang diketik live (bukan di-paste, kecuali data)
- **Interaksi**: pertanyaan / tebak output / polling
- **Catatan trainer**: jebakan, nuansa, antisipasi pertanyaan
- **➡️ Lanjut**: transisi ke slide/lokasi berikutnya

---

## 1. Ceritanya: Ijazah Raka

### Tokoh
- **Raka Pratama Putra**: fresh graduate S1 Statistika dari **Universitas Kenanga Raya** (fiktif). Wisuda 15 September 2026, IPK 3.45, lulus tepat 4 tahun. Sedang berburu kerja pertama sebagai **Data Analyst**.
- **HRD PT Data Maju**: perusahaan (fiktif) yang Raka lamar.
- Perusahaan fiktif lain: **PT Awan Biru** (minta IPK 3.50), **CV Tiga Kode** (minta IPK 2.75).

> Semua nama kampus, perusahaan, dan nomor ijazah fiktif. Cerita sengaja tidak menyinggung kasus ijazah tokoh publik mana pun.

### Masalahnya
Tiap malam Raka menghabiskan **±90 menit** untuk:
1. Membuka 5 portal lowongan
2. Menyalin lowongan baru ke Excel
3. Mengecek syarat satu-satu: IPK minimal, jurusan
4. Mengetik ulang data diri di form tiap perusahaan. Namanya pun ditulis beda-beda: `"  raka PRATAMA putra "` (form), `"RAKA PRATAMA PUTRA"` (KTP), `"Raka Pratama Putra   "` (CV)
5. Mengedit surat lamaran: ganti nama perusahaan dan posisi

Suatu hari surat untuk **PT Data Maju** terkirim dengan pembuka *"Yth. HRD **PT Awan Biru**"* karena lupa ganti nama setelah copy-paste. HRD membalas: *"Lamarannya buat kami atau buat PT Awan Biru?"* 😅

### Misinya
Di akhir kelas, peserta membantu Raka membuat **Kartu Lamaran otomatis**: script yang menghitung IPK, merapikan nama, membongkar nomor ijazah, mengecek syarat lowongan, dan menulis pembuka surat lamaran yang **tidak mungkin salah nama perusahaan**. Semuanya selesai dalam 1 detik.

### Kenapa satu cerita?
Konteks yang konsisten bikin setiap konsep punya **alasan untuk ada**. Peserta tidak belajar "string slicing" sebagai teori abstrak, tapi sebagai "cara Raka mengambil tanggal lulus dari nomor ijazah". Ceritanya juga dekat dengan peserta: banyak yang sedang atau akan berburu kerja. Setiap bab selalu dibuka dengan **masalah Raka**, lalu **konsep** yang menyelesaikannya.

### Peta cerita (story arc)

| Bab | Masalah Raka | Konsep | Hasil yang dibawa ke final project |
|---|---|---|---|
| Prolog | Urusan lamaran 90 menit/malam, salah nama perusahaan | – | Melihat target akhir (demo) |
| 1. Kenapa Raka Harus Ngoding? | Repetitif, membosankan, rawan salah. Lowongan minta Python | Otomasi & konsistensi | Motivasi |
| 2. Kenalan sama Python | "Pakai bahasa apa?" | High-level, interpreted, general purpose | – |
| 3. Nyiapin Meja Kerja | "Ngodingnya di mana?" | Dev environment, Colab, VSCode | Notebook & file `kartu_lamaran.py` |
| 4. Map Berlabel | Data diri berserakan | Komentar, `print`, variabel, aturan nama | Konstanta & variabel data |
| 5. Ngitung IPK | Hitung IPK, lama studi, cek syarat | int, float, operator, built-in angka, boolean | IPK & status memenuhi syarat |
| 6. Beresin Data Diri | Nama beda-beda, nomor ijazah panjang | String, indexing, slicing, method, casting | Nama rapi, tanggal lulus, lulusan ke- |
| 7. Wadah Banyak Barang | "8 semester = 8 variabel?" | list, tuple, set, dict | IPS per semester, tanggal lahir, skill |
| 8. Surat Lamaran Rapi | Surat & kartu harus rapi dan bisa diisi | `print`, escape char, f-string, `input` | Tampilan kartu & pembuka surat |
| Final: Satu Klik, Lamaran Jadi | Gabungkan semuanya | Semua di atas | **Kartu Lamaran v1.0** |
| Epilog: Bersambung... | Masih ada yang manual | Teaser: if, loop, function, pandas | Hook pertemuan berikutnya |

### Gamifikasi: Transkrip Kelas Python 🎓
Di slide peta perjalanan ada **transkrip** dengan 8 mata kuliah (PY-01 sampai PY-08, satu per bab). Tiap selesai bab, mata kuliah itu dapat stempel nilai **"A"** (animasi di slide). 8 nilai A = **LULUS** = final project. Footer slide juga menampilkan progres ini (8 kotak kecil).

### Data Kit (dipakai sepanjang kelas, angka konsisten)

```python
# ===== DATA KIT IJAZAH RAKA (dari ijazah & transkrip) =====
nama_lengkap = "Raka Pratama Putra"
jurusan = "Statistika"
tahun_masuk = 2022
tahun_lulus = 2026

total_sks = 144          # jumlah SKS yang lulus (18 SKS x 8 semester)
total_mutu = 497         # jumlah (bobot nilai x SKS) semua mata kuliah

IPK_MINIMAL = 3.00       # syarat lowongan PT Data Maju
GAJI_HARAPAN = 6_500_000

# ===== DATA KIT TEKS: satu nama, tiga versi (berantakan!) =====
nama_form = "  raka PRATAMA putra "      # diketik buru-buru di form online
nama_ktp  = "RAKA PRATAMA PUTRA"         # dari KTP
nama_cv   = "Raka Pratama Putra   "      # dari CV

nomor_ijazah = "IJZ-20260915-STA-0457"   # IJZ - tanggal lulus - kode prodi - nomor urut lulusan

# ===== Bab 7 =====
ips = [3.20, 3.35, 3.50, 3.41, 3.60, 3.52, 3.38, 3.65]   # IPS semester 1-8
TANGGAL_LAHIR = (12, 3, 2004)
```

**Angka kunci (buat cek jawaban cepat):** IPK `3.451388...` → dibulatkan `3.45` · lama studi `4` tahun / `8` semester · memenuhi IPK 3.00 `True` · memenuhi 3.50 `False` · cum laude `False` · legalisir `13` lembar sisa `2500` · rata-rata IPS `3.45125` · IPS tertinggi `3.65` · usia `22` · lulusan ke-`457` · huruf "a" di nama `6`.

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
8. **Menyusun** script sederhana yang menggabungkan semua konsep di atas (Kartu Lamaran v1.0).

> Versi ramah peserta (untuk Slide 7): *"Hari ini kalian akan (1) kenalan sama Python, (2) nulis & jalanin kode sendiri, (3) bikin kartu lamaran otomatis buat Raka."*

---

## 3. Prinsip pedagogis yang dipakai

| Prinsip | Kenapa penting untuk pemula | Cara diterapkan di kelas ini |
|---|---|---|
| **Narrative / contextual learning** | Otak lebih gampang mengingat cerita daripada daftar fakta | Satu cerita Raka dari awal sampai akhir; tiap konsep menjawab "masalah Raka yang mana?" |
| **Relevansi personal** | Motivasi naik kalau materi terasa berguna untuk hidup sendiri | Konteks berburu kerja: dekat dengan peserta yang baru/akan lulus. Bab 1 menyebut lowongan Data Analyst minta Python |
| **Tunjukkan tujuan di awal** (Gagné) | Peserta tahu "ujungnya ke mana", jadi tiap materi terasa relevan | Slide 6: demo kartu lamaran jadi dalam 1 detik |
| **Advance organizer** | Kasih "peta" sebelum detail biar informasi baru punya tempat | Peta perjalanan (Slide 7), peta tipe data (Slide 34) |
| **Masalah → Konsep → Contoh → Coba** | Konsep muncul sebagai solusi, bukan hafalan | Pola tetap di tiap bab |
| **PRIMM** (Predict-Run-Investigate-Modify-Make) | Menebak dulu bikin otak aktif dan miskonsepsi langsung kelihatan | "Tebak dulu sebelum di-run" di setiap demo; latihan bergerak dari modifikasi ke membuat sendiri |
| **Worked example → faded → mandiri** | Pemula kewalahan kalau langsung disuruh nulis dari nol | Demo lengkap → latihan isi titik-titik → final project dengan template |
| **Cognitive load** | Memori kerja pemula kecil (±4 hal baru sekaligus) | Satu konsep per slide; label 🟢🟡⚪; data di-paste (bukan diketik) supaya fokus ke logika |
| **Aturan 10 menit** | Atensi turun setelah ±10 menit mendengarkan | Tidak pernah lebih dari ±10 menit tanpa peserta ngetik / menjawab |
| **Error itu teman** (productive failure) | Pemula sering takut error dan berhenti | Sengaja bikin error di depan; "Kamus Error" yang bertambah tiap bab; skill membaca error diajarkan eksplisit |
| **Retrieval practice** | Mengingat kembali lebih efektif daripada membaca ulang | Tebak output tiap bab, latihan, final project, exit ticket |
| **Spiral** | Konsep diulang di konteks baru jadi makin kuat | Indexing string dipakai ulang di list; semua konsep muncul lagi di final project |
| **Analogi konsisten dari satu dunia** | Analogi yang konsisten mengurangi beban "pindah konteks" | Semua analogi dari dunia kampus & lamaran kerja: map berlabel, mesin fotokopi, ijazah yang salah cetak, transkrip |
| **Formative assessment** | Trainer tahu kapan harus melambat | Sinyal 🟢/🔴, tebak output, exit ticket 3-2-1 |
| **Psychological safety** | Pemula malu bertanya | Aturan main di awal; normalisasi error; trainer juga "kena error" |

### Peta analogi

| Konsep | Analogi di cerita Raka |
|---|---|
| Low vs high level | Instruksi detail mesin fotokopi vs "Mas, fotokopi ijazah 5 lembar ya" |
| Interpreted vs compiled | Penerjemah simultan saat wawancara vs penerjemah tersumpah ijazah |
| Library | Template CV siap pakai |
| Dev environment | Meja kerja; notebook = kertas coretan; IDE = meja kerja lengkap |
| Interpreter / editor / package manager / venv | Petugas loket / meja & kertas / koperasi kampus / map terpisah per lamaran |
| Function | Mesin fotokopi: dokumen masuk, hasil keluar |
| Variabel | Map dokumen berlabel |
| Boolean | Kotak centang: memenuhi syarat ✅ / ❌ |
| String immutable | Ijazah yang sudah dicetak: salah ketik harus cetak ulang |
| list / tuple / set / dict | IPS per semester / tanggal lahir / skill tanpa dobel / transkrip |
| f-string | Template surat lamaran yang nama perusahaannya diambil dari variabel |

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
| 00:00 | 7' | 1–7 | **Prolog**: Malam-malam Cari Kerja | 🖥️ → 🧪 (S6) → 🖥️ | Hook cerita, demo hasil akhir |
| 00:07 | 6' | 8–10 | **Bab 1**: Kenapa Raka Harus Ngoding? | 🖥️ | Diskusi, hitung jam terbuang |
| 00:13 | 10' | 11–17 | **Bab 2**: Kenalan sama Python | 🖥️ → 🧪 (S15) → 🖥️ | Tebak arti kode, demo interpreted |
| 00:23 | 7' | 18–21 | **Bab 3**: Nyiapin Meja Kerja | 🖥️ | Konsep dev environment |
| 00:30 | 12' | 22–25 | **Hands-on 1**: Halo, dunia kerja! | 🎯 Colab → 💻 VSCode → 🖥️ | Setup Colab, error pertama, demo VSCode |
| 00:42 | 15' | 26–33 | **Bab 4**: Map Berlabel | 🖥️ ⇄ 🧪, 🎯 di S33 | Komentar, print, variabel |
| 00:57 | 15' | 34–40 | **Bab 5**: Ngitung IPK | 🖥️ ⇄ 🧪, 🎯 di S40 | Angka, operator, boolean |
| 01:12 | 10' | 41 | ⏸️ **Istirahat** | – | Teaser puzzle di layar |
| 01:22 | 20' | 42–50 | **Bab 6**: Beresin Data Diri | 🖥️ ⇄ 🧪, 🎯 di S50 | String, slicing, method |
| 01:42 | 10' | 51–55 | **Bab 7**: Wadah Banyak Barang | 🖥️ ⇄ 🧪 | list, tuple, set, dict |
| 01:52 | 15' | 56–61 | **Bab 8**: Surat Lamaran Rapi | 🖥️ ⇄ 🧪, 🎯 di S61 | f-string, input |
| 02:07 | 15' | 62–64 | **Final**: Satu Klik, Lamaran Jadi | 🎯 Colab → 💻 VSCode | Mini project |
| 02:22 | 8' | 65–69 | **Epilog**: Bersambung... | 🖥️ | Recap, teaser, PR, exit ticket |

**Rasio kegiatan:** ±45% peserta aktif (ngetik/menjawab), ±55% penjelasan + demo. Bagian teori murni (Prolog–Bab 3) dibatasi 30 menit supaya peserta cepat pegang kode.

**Buffer tersembunyi** (kalau telat, ini yang dipadatkan duluan): ⚪ complex & frozenset, `%` & `.format()`, step slicing, tuple & set (lihat [Rencana cadangan](#10-rencana-cadangan)).

### Struktur notebook Colab
Ketiga notebook punya section yang sama persis:

| Section | `01_materi` (trainer, live coding) | `02_latihan_peserta` | `03_kunci_jawaban` |
|---|---|---|---|
| `00 · Demo Final` | Script final siap run | – | – |
| `Bab 3 · Halo Python` | Contoh print, demo interpreted | Cell kosong + demo tebak output | Jawaban |
| `Bab 4 · Map Berlabel` | Semua demo Bab 4 | Latihan + Pojok Error (1 cell per baris) | Jawaban + tabel Pojok Error |
| `Bab 5 · Ngitung IPK` | Semua demo Bab 5 | Data kit angka + 1 cell per soal | Jawaban |
| `Bab 6 · Beresin Data Diri` | Semua demo Bab 6 | Data kit teks + 1 cell per soal | Jawaban |
| `Bab 7 · Wadah Banyak Barang` | Semua demo Bab 7 | Cell coba-coba + kuis | Jawaban kuis |
| `Bab 8 · Surat Lamaran Rapi` | Semua demo Bab 8 | Latihan | Jawaban |
| `Final · Kartu Lamaran v1.0` | Penutup + teaser | Template isi titik-titik | Kunci final + bonus |

Di slide yang ada 🧪/🎯, sebut **nama section-nya** supaya peserta tahu harus scroll ke mana. Link Colab peserta: https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb

---

## 5. Persiapan sebelum kelas

### Peserta (kirim H-3, ingatkan H-1)
- [ ] Punya akun Google, bisa buka [colab.research.google.com](https://colab.research.google.com)
- [ ] *(Opsional, untuk ikut demo VSCode)* Install Python 3.12+ dan VSCode + extension "Python" (Microsoft). Tes di terminal: `python3 --version` (Mac/Linux) atau `python --version` (Windows)
- [ ] Laptop dicas, internet stabil

### Trainer
- [ ] Buka `01_materi_ijazah_raka.ipynb` di Colab (link dari README repo), *Save a copy in Drive* supaya bisa diedit saat live coding
- [ ] Link Colab `02_latihan_peserta.ipynb` siap di-paste ke chat (peserta nanti *Save a copy in Drive*)
- [ ] Section `00 · Demo Final` sudah dites, termasuk `input()`
- [ ] Clone repo, buka folder `lamaran-raka/` di VSCode: `kartu_lamaran.py` (isi final) siap, terminal sudah terbuka, interpreter Python terpilih
- [ ] Font size Colab & VSCode diperbesar
- [ ] Deck terbuka (https://thosangs.github.io/python_lecture/), mode presenter di layar kedua kalau ada
- [ ] Link notebook + link form exit ticket siap di-paste ke chat
- [ ] Papan/area **"Kamus Error"** (whiteboard, atau 1 slide yang diisi bertahap)
- [ ] **Backup**: kalau Colab bermasalah, pakai Jupyter lokal / VSCode dengan file `.ipynb` yang sama

---

## 6. Alur per slide

---

## PROLOG: Malam-malam Cari Kerja
**00:00 – 00:07 (7 menit)**

### Slide 1 · Judul · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** "Ijazah Raka". Subjudul: "Dari copy-paste lamaran ke kartu lamaran otomatis. Satu cerita, 2,5 jam, dan kamu yang nulis kodenya." Stiker "🎓 Edisi Fresh Graduate".

**Ngomongnya:** Perkenalan singkat diri (maks 30 detik). Langsung masuk ke kalibrasi.

---

### Slide 2 · Angkat tangan dulu! · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** 3 pertanyaan:
1. Siapa yang **pakai Excel/Spreadsheet** hampir tiap hari?
2. Siapa yang pernah ngisi **form yang itu-itu lagi** berulang-ulang? Misalnya form lamaran kerja.
3. Siapa yang **pernah ngoding** (bahasa apa pun)?

**Interaksi:** Angkat tangan / reaction. Catat dalam hati proporsi yang pernah ngoding.

**Catatan trainer:** Ini **kalibrasi**. Kalau banyak yang sudah pernah ngoding, siapkan "jalur ngebut" (tantangan 🔴). Kalau hampir semua belum, lambatkan Bab 4–6. Pertanyaan 2 jadi jembatan emosional ke cerita Raka: *"Nah, kalian nggak sendirian. Kenalin, Raka."*

---

### Slide 3 · 📖 Kenalan sama Raka · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** Kartu Raka 🧑‍🎓 "Fresh graduate · wisuda Sept 2026". Ijazahnya: S1 Statistika, Universitas Kenanga Raya (fiktif), tag `144 SKS` · `IPK 3.45` · `lulus 4 tahun`. Misinya: kerja pertama sebagai Data Analyst.

**Ngomongnya:** "Raka ini mirip banyak dari kita: baru lulus, semangat, jago Excel. Tapi ngurus lamaran ternyata makan waktu banget."

---

### Slide 4 · 📖 Malam-malam Raka · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** Timeline:
```
21.00  Buka 5 portal lowongan
21.15  Salin lowongan baru ke Excel
21.35  Cek syarat satu-satu: IPK minimal, jurusan
21.55  Ketik ulang data diri di form tiap perusahaan
22.15  Edit surat lamaran: ganti nama perusahaan
22.30  Kirim... besok ulang lagi. 😮‍💨
```
Plus nama Raka di 3 dokumen:
```
"  raka PRATAMA putra "  | form online
"RAKA PRATAMA PUTRA"     | KTP
"Raka Pratama Putra   "  | CV
```

**Ngomongnya:** "Ini terjadi **setiap malam** selama Raka cari kerja." Tunjuk data nama: orangnya sama, tulisannya beda-beda. Ini akan jadi masalah di Bab 6.

---

### Slide 5 · 📖 Lupa ganti satu nama · 🖥️ SLIDE · ⏱️ 0,5'
**Di layar:** Bubble chat:
> Raka → PT Data Maju: "Yth. HRD **PT Awan Biru**, dengan ini saya melamar posisi Data Analyst..."
> HRD PT Data Maju: "Terima kasih, Mas Raka. Tapi... lamarannya buat kami atau buat PT Awan Biru? 😅"
> *(klik)* Raka: "Mohon maaf, salah copy-paste surat 🙇"

**Ngomongnya:** "Copy-paste surat lamaran, lupa ganti nama perusahaan. Capek, ngantuk, manusiawi. Tapi kesan pertama ke HRD jadi jelek."

---

### Slide 6 · Hari ini kita bantu Raka · 🧪 COLAB-DEMO · ⏱️ 1,5'
**Di layar (sebelum pindah):** "Gimana kalau semuanya selesai dalam **1 detik**?" + potongan output kartu lamaran.

**➡️ Pindah ke Colab, notebook `01_materi_ijazah_raka`, section `00 · Demo Final`.** Jalankan cell, isi nama perusahaan (`pt data maju`), posisi (`data analyst`), dan IPK minimal (`3.00`). Biarkan output kartu tampil penuh.

**Ngomongnya:** "Ini yang **kalian sendiri** bakal bikin di akhir kelas. Bukan saya, kalian. Dan perhatikan baris terakhirnya: nama perusahaan di surat diambil otomatis, jadi nggak mungkin ketuker lagi."

**Catatan trainer:** Jangan jelaskan kodenya sekarang. Scroll cepat untuk menunjukkan kodenya "cuma" ±50 baris. Tujuannya membuat penasaran.

**➡️ Lanjut:** balik ke 🖥️ Slide 7.

---

### Slide 7 · Peta perjalanan & aturan main · 🖥️ SLIDE · ⏱️ 1'
**Di layar:**
- Kiri: **Transkrip Kelas Python** (PY-01 sampai PY-08 + sel LULUS). "8 bab, 8 nilai A, lalu lulus 🎓"
- Kanan: Aturan main (lihat bagian 3)

**Ngomongnya:** Bacakan tujuan versi ramah peserta. "Setiap selesai satu bab, kalian dapat nilai A. 8 nilai A = lulus. Lihat juga footer slide: kotak kecil di tengah itu progres transkrip, label kanan menunjukkan kita lagi di Colab, VSCode, atau hands-on."

---

## BAB 1: Kenapa Raka Harus Ngoding?
**00:07 – 00:13 (6 menit)**

### Slide 8 · Masalahnya bukan di Excel-nya · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** Diagram: LinkedIn, Jobstreet, Glints, web karier perusahaan (format A/B/C/beda lagi) mengalir ke Raka. Tulisan besar: **"Di dunia data, datanya bukan cuma 1 file Excel."**

**Ngomongnya:** "Excel itu alat yang bagus. Masalahnya, data di dunia nyata datang dari banyak tempat, tiap hari, dengan format beda-beda. Lowongan kerja juga begitu: 5 portal, 5 format."

**Interaksi:** "Di kerjaan/kampus kalian, data datang dari mana aja?" (1–2 jawaban saja)

---

### Slide 9 · 3 musuh kerja manual · 🖥️ SLIDE · ⏱️ 2,5'
**Di layar:** 3 kartu:
1. 🔁 **Repetitif**: form yang sama, tiap lamaran
2. 😴 **Membosankan**: bikin kita lengah
3. ⚠️ **Rawan salah**: salah nama perusahaan, nomor ijazah ketuker, IPK `3.45` jadi `34.5`

**Interaksi: hitung bareng.** "Raka butuh 90 menit tiap malam, 30 malam sebulan. Berapa jam?"
> 90 × 30 = 2.700 menit = **45 jam ≈ hampir 6 hari kerja tiap bulan**, cuma buat copy-paste lamaran.

**Ngomongnya:** "Yang paling bahaya bukan capeknya, tapi **salahnya**. Satu digit nomor ijazah ketuker, HRD bisa langsung menganggap datanya tidak valid."

**Catatan trainer:** Di outline tertulis "Fradulent". Di sini dibingkai sebagai *rawan salah*: data yang diketik ulang manual tidak konsisten dan susah dicek.

---

### Slide 10 · Kode itu template · 🖥️ SLIDE · ⏱️ 1,5' · 🎓 NILAI A BAB 1
**Di layar:** Manual 90 menit (hasil bisa salah-salah) ➜ Script 1 detik (hasil selalu konsisten). "Bonusnya: hampir semua lowongan Data Analyst yang Raka lihat **minta Python**." Transkrip ringkas, PY-01 dapat A.

**Ngomongnya:** "Kode itu kayak **template surat**. Ditulis sekali, tinggal isi datanya, hasilnya selalu rapi. Dan sekalian, Python itu skill yang dicari di lowongan yang Raka incar."

**➡️ Transisi:** "Oke, Raka mau ngoding. Tapi pakai **bahasa** apa?"

---

## BAB 2: Kenalan sama Python
**00:13 – 00:23 (10 menit)**

### Slide 11 · Bahasa buat ngobrol sama komputer · 🖥️ SLIDE · ⏱️ 1,5' · ⚪
**Di layar:** Spektrum `0101 → Assembly → C → Java, PHP → Python` dengan label **Low level** (dekat ke mesin) ↔ **High level** (dekat ke manusia).

**Ngomongnya (analogi fotokopi):**
> "**Low level**: 'Ambil kertas A4 80 gram, buka tutup mesin, taruh ijazah menghadap kaca pojok kiri atas, kontras level 3, tekan tombol hijau 5 kali...'
> **High level**: 'Mas, fotokopi ijazah 5 lembar, sekalian legalisir ya.'
> Hasilnya sama-sama fotokopian. Bedanya: siapa yang mikirin detailnya."

---

### Slide 12 · Sama-sama bilang "Halo" · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:** Bahasa mesin (ilustrasi), Assembly, Java, dan Python, semuanya mencetak "Halo, dunia kerja!".

```python
print("Halo, dunia kerja!")
```

**Ngomongnya:** "Java juga high level, tapi lihat bedanya. Python satu baris. Itu yang dimaksud **simple syntax**."

---

### Slide 13 · Dirancang untuk mudah dibaca · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:**
```python
syarat_jurusan = ["statistika", "matematika"]
jurusan_raka = "statistika"

if jurusan_raka in syarat_jurusan:
    print("Siap, kirim lamaran!")
else:
    print("Cari lowongan lain.")
```

**Interaksi:** "Kalian **belum belajar** Python sama sekali. Tapi coba tebak: program ini ngapain?" Tunggu 2–3 jawaban, lalu klik.

**Ngomongnya:** "Kalian bisa nebak, kan? Itu karena Python didesain dengan prinsip **readability**. Salah satu prinsip resminya bunyinya *'Readability counts'*."

**Catatan trainer:** `if` sengaja dipakai sebagai *teaser*. Jangan dijelaskan sintaksnya. Bonus: di Hands-on 1, peserta bisa jalankan `import this`.

---

### Slide 14 · Interpreted vs Compiled · 🖥️ SLIDE · ⏱️ 2' · 🟡
**Di layar:**

| | **Interpreted** (Python) | **Compiled** (C, C++, Java, C#) |
|---|---|---|
| Cara kerja | Dibaca & dijalankan **baris per baris** | Seluruh kode **dibungkus** jadi bahasa mesin dulu |
| Analogi | 🎙️ Penerjemah simultan saat wawancara: kalimat demi kalimat | 📜 Penerjemah tersumpah: seluruh ijazah diterjemahkan & dicetak dulu |
| Error ketahuan | Saat baris itu dijalankan; baris sebelumnya **sudah jalan** | Saat compile, **sebelum** program jalan |
| Kelebihan | Cepat dicoba, cocok eksplorasi data | Eksekusi lebih cepat |
| Kekurangan | Eksekusi relatif lebih lambat | Tiap ubah kode harus compile ulang |

**Ngomongnya:** "Penerjemah simultan menerjemahkan kalimat demi kalimat. Kalau di kalimat ke-3 dia salah, kalimat 1 & 2 sudah terlanjur diucapkan. Penerjemah tersumpah beda: seluruh ijazah diterjemahkan dulu, dicek, baru dicetak. Kalau salah, ketahuan sebelum dipakai, tapi tiap ada perubahan harus terjemah & cetak ulang."

**Catatan trainer (kalau ada yang kritis bertanya):**
- Secara teknis, Python (CPython) juga mengompilasi kode ke *bytecode* dulu, lalu dijalankan interpreter. Tetap dikategorikan "interpreted".
- Java & C# dikompilasi ke bytecode lalu dijalankan virtual machine (JVM / .NET).
- **Penting untuk demo:** `SyntaxError` dicek di awal, jadi **seluruh cell tidak jalan**. Yang berhenti di tengah adalah error saat runtime seperti `NameError`. Karena itu demo Slide 15 pakai `NameError`.

---

### Slide 15 · Demo: penerjemah kalimat demi kalimat · 🧪 COLAB-DEMO · ⏱️ 1,5'
**➡️ Pindah ke Colab materi, section `Bab 3 · Halo Python`** (peserta nonton saja).

**Kode:**
```python
print("1. Buka portal lowongan... beres")
print("2. Salin data lowongan... beres")
prnt("3. Cek syarat IPK...")
print("4. Kirim lamaran")
```

**Interaksi:** "Ada typo di baris 3. Tebak: berapa baris yang tercetak?" (A) 0 · (B) 2 · (C) 4

**Hasil:** 2 baris tercetak, lalu `NameError: name 'prnt' is not defined`. Baris 4 tidak dijalankan.

**Catatan trainer:** Jangan bahas cara baca error dulu, itu nanti di Slide 23 saat peserta mengalaminya sendiri.

---

### Slide 16 · General purpose · 🖥️ SLIDE · ⏱️ 1' · ⚪
**Di layar:** Data (pandas, numpy, matplotlib) · AI/ML (scikit-learn, PyTorch) · Web (Django, Flask, FastAPI) · Game (pygame) · Otomasi (openpyxl, requests).

**Ngomongnya:** "**Library** itu kayak template CV siap pakai. Raka nggak desain CV dari nol, tinggal pakai template yang sudah jadi. Raka nanti pakai **pandas** buat baca data lowongan, itu materi pertemuan selanjutnya."

---

### Slide 17 · Gratis, komunitas besar, jagoan di data · 🖥️ SLIDE · ⏱️ 1' · 🎓 NILAI A BAB 2
**Di layar:** 🆓 Free & open source · 👥 PythonID & PyCon ID · 🏆 nomor 1 di data. Ringkasan: **"Python = bahasa high-level, mudah dibaca, interpreted, serbaguna, gratis, dan jagoan di dunia data."**

**Ngomongnya:** "Komunitas besar artinya kalau kalian error, 99% kemungkinan sudah ada orang lain yang pernah kena dan nanya duluan di internet."

**Catatan trainer:** Kalau mau menyebut peringkat/angka spesifik, cek data terbaru (TIOBE, IEEE Spectrum, Stack Overflow Developer Survey) sebelum kelas.

**➡️ Transisi:** "Bahasanya udah kepilih. Sekarang, Raka ngodingnya **di mana**?"

---

## BAB 3: Nyiapin Meja Kerja
**00:23 – 00:30 (7 menit)**

### Slide 18 · Development environment = meja kerja · 🖥️ SLIDE · ⏱️ 1,5' · 🟡
**Di layar:** "Tempat kita menulis, menjalankan, dan mengembangkan aplikasi." Bikin web: VSCode · Cursor · PhpStorm. Ngolah data: VSCode · Cursor · **Notebook**.

**Ngomongnya:** "Mahasiswa butuh meja belajar. Programmer butuh **dev environment**. Mejanya tergantung mau ngerjain apa."

---

### Slide 19 · Isi meja kerja Python · 🖥️ SLIDE · ⏱️ 2'
**Di layar:**

| Komponen | Fungsinya | Analogi | Level |
|---|---|---|---|
| **Python interpreter** | Yang benar-benar menjalankan kode | 🏢 Petugas loket yang memproses berkas kita | 🟡 |
| **Code editor** | Tempat menulis kode | 📝 Meja & kertas buat nulis | 🟡 |
| **Package manager** (pip, uv) | Download & install library | 🛒 Koperasi kampus: beli perlengkapan | ⚪ |
| **Virtual environment** | Ruang terpisah per proyek | 🗂️ Map terpisah per lamaran | ⚪ |

**Ngomongnya:** "Hari ini cukup ingat dua yang pertama. Kabar baiknya: di Google Colab, semuanya udah disiapin."

---

### Slide 20 · 3 gaya meja kerja · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** Text editor + terminal (meja lipat minimalis) · IDE (meja kerja lengkap) · Notebook (**kertas coretan**: hitung per bagian, langsung lihat hasil).

**Ngomongnya:** "Notebook itu kayak kertas coretan waktu ujian: kodenya dipotong-potong per **cell**, tiap cell bisa dijalankan dan langsung kelihatan hasilnya."

---

### Slide 21 · Hari ini pakai yang mana? · 🖥️ SLIDE · ⏱️ 1,5'
**Di layar:** 🧪 Google Colab (belajar & coba-coba, dipakai sepanjang kelas) · 💻 VSCode (script "beneran", tujuan akhir Raka).

**Ngomongnya:** "Sepanjang kelas kita pakai Colab. Di akhir kelas, kita pindahin hasilnya ke VSCode, karena itulah yang nanti dijalankan Raka tiap ada lowongan baru."

**Catatan trainer:** Alasan semua peserta pakai Colab: **nol instalasi** = nol waktu terbuang buat troubleshooting setup, dan beban kognitif fokus ke Python, bukan ke tools.

**➡️ Lanjut:** "Saatnya pegang kode!" → 🎯 Hands-on 1.

---

## HANDS-ON 1: Halo, dunia kerja!
**00:30 – 00:42 (12 menit)**

### Slide 22 · Meja kerja pertamamu · 🎯 HANDS-ON · ⏱️ 6'
**Di layar (biarkan tampil, tombol Colab bisa diklik):**
1. Buka link notebook `02_latihan_peserta` (tombol di slide / di chat) → **File → Save a copy in Drive**
2. Ganti nama: `IjazahRaka_NamaKamu`
3. Scroll ke section **`Bab 3 · Halo Python`**
4. Ketik `print("Halo, dunia kerja!")` → **Shift + Enter**
5. Ganti tulisannya jadi namamu, jalankan lagi
6. **+ Text** → "Catatan kelas Python pertamaku 🎓"
7. Sinyal 🟢 / 🔴

**Ngomongnya / tunjukkan:**
- "Kotak abu-abu ini namanya **cell**. Ada **code cell** dan **text cell**."
- "Angka `[1]` di kiri cell = urutan cell itu dijalankan."
- "Run pertama agak lama karena Colab lagi nyiapin 'meja kerja' (runtime) di server Google."

**Catatan trainer:** Lupa tanda kutip → `NameError`; kurung tidak ditutup → `SyntaxError`. Bagus! Pakai sebagai bahan Slide 23. Bonus buat yang cepat: `import this`.

---

### Slide 23 · Error pertamamu (dan cara bacanya) · 🎯 HANDS-ON · ⏱️ 2,5'
**Kegiatan:** Di notebook latihan, cell demo Slide 15 sudah disiapkan. Peserta **tebak dulu** berapa baris yang tercetak, lalu jalankan.

**Di layar: cara baca error dalam 3 langkah**
1. 👇 **Baca baris paling bawah dulu**: jenis error + pesannya
2. 🔍 **Cari nomor baris / tanda panah** `---->`
3. 🤔 **Bandingkan dengan maksudmu**: typo? lupa kutip? kurung belum ditutup?

**Ngomongnya:** "Pesan error itu bukan marah-marah, tapi **petunjuk**. Python sering bahkan kasih saran, misalnya *'Did you mean: print?'*."

**Mulai "Kamus Error":** **NameError** = "Aku nggak kenal nama ini."

---

### Slide 24 · Meja kerja lengkap: VSCode · 💻 VSCODE · ⏱️ 2,5'
**➡️ Pindah ke VSCode** (demo trainer; peserta yang sudah install boleh ikut).

**Langkah demo:**
1. **File → Open Folder** → `lamaran-raka` (folder di repo)
2. File baru: `kartu_lamaran.py` (atau file baru apa saja untuk demo halo)
3. Ketik `print("Halo, dunia kerja!")` → **simpan**
4. Jalankan lewat tombol ▶ **Run Python File**, atau terminal:
   ```bash
   python3 kartu_lamaran.py
   ```
   *(Windows: `python kartu_lamaran.py`)*

**Ngomongnya:** "Bedanya sama Colab: ini **file** `.py`, dokumen yang tersimpan rapi. Bisa dijalankan kapan saja tanpa browser, tiap kali ada lowongan baru. **Kita balik ke sini di akhir kelas.**"

**Catatan trainer:** Kalau tombol ▶ tidak muncul, cek extension Python terpasang dan interpreter terpilih (pojok kanan bawah VSCode).

---

### Slide 25 · Colab vs VSCode · 🖥️ SLIDE · ⏱️ 1' · 🎓 NILAI A BAB 3
**Di layar:** Tabel Colab (kertas coretan, per cell) vs VSCode (meja kerja lengkap, seluruh file). Tips: variabel "nggak dikenal" padahal sudah ditulis → cell-nya belum di-run → **Runtime → Run all**.

**➡️ Transisi:** "Meja kerja siap. Sekarang Raka mulai menyusun data lamarannya. Mulai sekarang kita di **Colab** terus."

---

## BAB 4: Map Berlabel
**00:42 – 00:57 (15 menit)**
*Komentar, print, variabel*

### Slide 26 · Langkah pertama Raka: catatan · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
**➡️ 🧪 Colab materi, section `Bab 4 · Map Berlabel`.**

```python
# Kartu lamaran Raka
# Dibuat oleh: Raka
print("Mulai menyusun lamaran")  # komentar di ujung
# print("baris ini nggak dijalankan")
```

**Ngomongnya:** "Komentar dipakai untuk (1) menjelaskan **kenapa** kode ditulis begitu, dan (2) 'mematikan' kode sementara." Shortcut **Cmd + /** / **Ctrl + /**.

---

### Slide 27 · `print()` dan konsep function · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
**Di layar:** `"Halo"` (dokumen = argumen) ➜ 🖨️ `print( )` (mesin = function) ➜ Halo (hasil di layar).

```python
print("Lamaran Data Analyst")
print(144)
print("Total SKS:", 144)  # dipisah koma
print()                   # baris kosong
print(Raka)               # ❌ lupa kutip
```

**Interaksi:** Sebelum baris terakhir: "Ini bakal jalan nggak?"

**Ngomongnya:** "Function itu kayak **mesin fotokopi**: dokumen masuk, hasil keluar. Teks pakai tanda kutip, angka tidak. Tanpa kutip, Python mengira `Raka` itu nama sesuatu → `NameError`."

---

### Slide 28 · Variabel = map berlabel · 🧪 COLAB-DEMO · ⏱️ 2' · 🟢
**Di layar:** 3 map dokumen berlabel: `nama_lengkap` → `"Raka Pratama Putra"` (str), `total_sks` → `144` (int), `ipk` → `3.45` (float). **"`=` artinya MASUKKAN KE, bukan SAMA DENGAN."**

**Ngomongnya:** "Di Excel, Raka nyimpen IPK di sel `B2`. Masalahnya, `B2` itu apa? Di Python, kita kasih **nama yang bermakna**, kayak label di map dokumen."

```python
nama_lengkap = "Raka Pratama Putra"
total_sks = 144
ipk = 3.45
print(nama_lengkap)
print(ipk)
```

**Interaksi: tebak output** ("Raka punya 10 lamaran aktif, 3 ditolak, lalu kirim 5 lagi"):
```python
lamaran_aktif = 10
lamaran_aktif = lamaran_aktif - 3
lamaran_aktif = lamaran_aktif + 5
print(lamaran_aktif)
```
(A) 10 · (B) 12 · (C) Error → **B (12)**

**Catatan trainer:** Miskonsepsi `=` sebagai "sama dengan" sangat umum pada pemula. Tekankan sekarang, karena di Bab 5 akan muncul `==`.

---

### Slide 29 · Isi map bisa diganti · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟡
**Di layar:** Java (`double ipk = 3.45; ipk = "tiga koma empat lima"; // ❌ error`) vs Python:
```python
ipk = 3.45
print(type(ipk))  # <class 'float'>

ipk = "tiga koma empat lima"  # ✅ boleh, tapi
print(type(ipk))  # <class 'str'>
```

**Ngomongnya:** "Isi map dengan nama yang sama → **isi lama hilang**. Python menebak tipe dari isinya. Fleksibel, tapi **jangan ganti-ganti tipe**. `type()` buat ngecek jenis isinya."

---

### Slide 30 · Aturan wajib kasih label · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢

| Aturan | ❌ Salah | ✅ Benar | Error-nya |
|---|---|---|---|
| Tidak boleh diawali angka | `1nama = "Raka"` | `nama1` | `SyntaxError: invalid decimal literal` |
| Tidak boleh pakai spasi | `nama lengkap = ...` | `nama_lengkap` | `SyntaxError: invalid syntax` |
| Hanya huruf, angka, `_` | `total-sks = 144` | `total_sks` | `SyntaxError: cannot assign to expression here` |
| Bukan *keyword* | `class = "Statistika"` | `kelas` | `SyntaxError: invalid syntax` |
| *Case sensitive* | `Ipk` ≠ `ipk` | konsisten | `NameError` kalau salah huruf |

```python
import keyword
print(keyword.kwlist)
```

**Ngomongnya:** "Kenapa `total-sks` salah? Tanda `-` dibaca Python sebagai **pengurangan**."

**Kamus Error:** **SyntaxError** = "Tata bahasanya salah." Python menolak menjalankan cell sama sekali.

**Catatan trainer:** Kalau ada yang iseng mencoba `1jurusan = ...`, muncul *"invalid imaginary literal"* karena `1j` dibaca sebagai bilangan kompleks. Tetap sama-sama SyntaxError, cukup jadi fun fact.

---

### Slide 31 · Jebakan: boleh, tapi bikin celaka · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟡
**Di layar:** 📖 "Raka pernah bikin variabel `max` buat nyimpen IPS tertinggi. 10 menit kemudian..."

```python
max = 3.65                    # IPS tertinggi
print(max)                    # 3.65 (normal)
print(max(3.20, 3.65, 3.41))  # ❌ TypeError: 'float' object is not callable
```
Perbaikan:
```python
del max
print(max(3.20, 3.65, 3.41))  # ✅ 3.65
```

**Ngomongnya:** "Nama function bawaan **bukan** keyword, jadi Python mengizinkan. Tapi mesin `max` aslinya ketimpa angka. Kayak map dikasih label 'mesin fotokopi', mesinnya jadi hilang. `del` menghapus variabel."

**Tips:** Hindari `max`, `min`, `sum`, `list`, `str`, `print`, `type`, `input`. Kalau nama variabel **berubah warna** di editor, ganti namanya.

---

### Slide 32 · Konvensi PEP 8 · 🖥️ SLIDE · ⏱️ 1' · 🟢
**Di layar:** `snake_case` (`nama_lengkap`) · `UPPER_CASE` untuk konstanta (`IPK_MINIMAL = 3.00`) · `PascalCase` untuk class nanti (`KartuLamaran`). Nama jelek: `x a1 data2 tmp`. Nama bagus: `total_sks tahun_lulus`.

**Ngomongnya:** "Aturan = **wajib** (dilanggar → error). Konvensi = **kesepakatan**: nggak error, tapi kode lebih sering dibaca daripada ditulis. Rekan kerja di kantor pertama kalian akan berterima kasih."

---

### Slide 33 · 🎯 Latihan Bab 4 · 🎯 HANDS-ON · ⏱️ 4,5' · 🎓 NILAI A BAB 4
**➡️ Peserta ke section `Bab 4 · Map Berlabel`.**

1. Buat variabel data diri Raka: nama lengkap, jurusan, tahun masuk `2022`, tahun lulus `2026`
2. Buat variabel transkrip: total SKS `144`, total mutu `497`
3. Buat **konstanta** IPK minimal lowongan: `3.00`
4. Print semuanya, cek tipenya pakai `type()`

**Pojok Error (tebak dulu, error atau tidak?):**
```python
jurusan_1 = "Statistika"
1prodi = "Matematika"
tahun lulus = 2026
_catatan = "rahasia"
Ipk = 3.45
print(ipk)
```

**Jawaban:** baris 2 (diawali angka) & 3 (spasi) → `SyntaxError`; baris 6 → `NameError` (case sensitive). Baris 1, 4, 5 valid.

**Catatan trainer:** Di notebook latihan, Pojok Error sudah dipisah **satu cell per baris**: tebak dulu, lalu jalankan satu per satu. Variabel dari latihan ini dipakai lagi di Bab 5 (data kit juga tersedia di section Bab 5).

**➡️ Transisi:** "Data diri udah masuk map. Sekarang saatnya **ngitung IPK**."

---

## BAB 5: Ngitung IPK
**00:57 – 01:12 (15 menit)**

### Slide 34 · Peta tipe data · 🖥️ SLIDE · ⏱️ 1'

| Kategori | Tipe | Contoh di cerita Raka | Gampangnya | Dibahas |
|---|---|---|---|---|
| Numeric | `int` | `144` total SKS | dihitung bulat | Bab 5 🟢 |
| | `float` | `3.45` IPK | ada komanya | Bab 5 🟢 |
| | `complex` | `3+4j` | – | Bab 5 ⚪ |
| Boolean | `bool` | `True` memenuhi syarat | kotak centang ✅/❌ | Bab 5 🟢 |
| Text | `str` | `"Raka Pratama Putra"` | tulisan di ijazah | Bab 6 🟢 |
| Sequence | `list`, `tuple` | IPS per semester, tanggal lahir | daftar urut | Bab 7 🟢/🟡 |
| Set | `set`, `frozenset` | skill tanpa dobel | daftar unik | Bab 7 🟡/⚪ |
| Mapping | `dict` | transkrip | mata kuliah → nilai | Bab 7 🟢 |

**Ngomongnya:** "Ini peta semua jenis data di Python. Kita kunjungi satu-satu."

---

### Slide 35 · Angka: int, float, complex · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
**➡️ 🧪 Colab materi, section `Bab 5 · Ngitung IPK`** (jalankan data kit dulu).

```python
total_sks = 144            # int  : bilangan bulat
ipk = 3.45                 # float: desimal (TITIK)
GAJI_HARAPAN = 6_500_000   # underscore boleh
print(type(total_sks), type(ipk))
z = 3 + 4j                 # complex: kenalan aja
```

**Ngomongnya:** "IPK di ijazah ditulis `3,45` pakai koma. Di Python wajib pakai **titik**: `3.45`. `6_500_000` sama persis dengan `6500000`."

**Catatan trainer:** Untuk uang Rupiah, pakai `int` (lihat FAQ soal `0.1 + 0.2`).

---

### Slide 36 · Operator: kalkulator Raka · 🧪 COLAB-DEMO · ⏱️ 3' · 🟢 (`//` `%` `**`: 🟡)

| Operator | Arti | Contoh cerita Raka | Hasil |
|---|---|---|---|
| `+` | tambah | `tahun_masuk + 4` | `2026` |
| `-` | kurang | `tahun_lulus - tahun_masuk` | `4` |
| `*` | kali | `18 * 8` (SKS × semester) | `144` |
| `/` | bagi (**selalu float**) | `total_mutu / total_sks` (IPK) | `3.451388...` |
| `//` | bagi, bulat ke bawah | `100_000 // 7_500` (lembar legalisir) | `13` |
| `%` | sisa bagi | `100_000 % 7_500` (sisa uang) | `2500` |
| `**` | pangkat | `1.1 ** 3` | `1.3310000000000004` |

**Kode (tanya hasilnya sebelum run):**
```python
ipk = total_mutu / total_sks
print(ipk)                          # 3.451388888888889

lama_studi = tahun_lulus - tahun_masuk
print(lama_studi, lama_studi * 2)   # 4 8
print(total_sks / 8)                # 18.0 ← kok ada .0?

# Legalisir ijazah Rp7.500 per lembar. Uang Raka Rp100.000:
print(100_000 // 7_500)    # 13 lembar
print(100_000 % 7_500)     # 2500 sisa uang

# Gaji pertama naik 10% tiap tahun, 3 tahun lagi:
print(GAJI_HARAPAN * 1.1 ** 3)      # 8651500.000000002
```

**Interaksi:** Predict di slide: `print(144 / 8)` → 18 atau 18.0? (18.0)

**Ngomongnya:**
- "IPK = jumlah (bobot nilai × SKS) dibagi total SKS. `/` **selalu** menghasilkan float."
- "`//` dan `%` itu pasangan: `//` 'dapat berapa lembar legalisir', `%` 'sisa uangnya berapa'."
- "Urutan operasi: `**` dulu, lalu `* / // %`, lalu `+ -`. Ragu? Pakai **kurung**."

**Catatan trainer:** `%` tidak ada di outline asli, tapi sering dipakai dan berpasangan alami dengan `//`.

---

### Slide 37 · Built-in function untuk angka · 🧪 COLAB-DEMO · ⏱️ 2' · 🟢
```python
print(abs(tahun_masuk - tahun_lulus))  # 4 (selisih tanpa minus)
print(round(ipk, 2))                   # 3.45
print(round(ipk))                      # 3
print(max(3.20, 3.65, 3.41))           # 3.65 (IPS tertinggi)
print(min(3.20, 3.65, 3.41))           # 3.2
print(int(3.99))                       # 3 ← dipotong, BUKAN dibulatkan!
print(float(144))                      # 144.0
```

**Interaksi:** Sebelum `int(3.99)`: "IPK 3.99 kalau di-int jadi 3 atau 4?"

**Cara mancing sendiri:** `round?` (Colab/Jupyter) atau `help(round)` (di mana saja).

**Ngomongnya:** "Kalian **nggak perlu hafal** semua function. Yang penting tahu cara nyari."

---

### Slide 38 · Boolean: centang YA / TIDAK · 🧪 COLAB-DEMO · ⏱️ 2,5' · 🟢
**Di layar:** `True` / `False` (kapital!) + tabel perbandingan `== != > < >= <=`.

```python
ipk = round(total_mutu / total_sks, 2)
print(ipk >= IPK_MINIMAL)       # True ← memenuhi!
print(ipk >= 3.50)              # False (PT Awan Biru)
print(jurusan == "Statistika")  # True
print(type(True))               # <class 'bool'>
print(true)                     # ❌ NameError
```

**Ngomongnya:** "Lowongan PT Data Maju minta IPK minimal 3.00: Raka memenuhi. PT Awan Biru minta 3.50: belum. **`=` memasukkan ke map. `==` bertanya 'apakah sama?'.** Ini sumber error nomor satu pemula."

---

### Slide 39 · and, or, not · 🧪 COLAB-DEMO · ⏱️ 1' · 🟡
```python
# Cum laude: IPK di atas 3.50 DAN lulus maks 4 tahun?
print(ipk > 3.50 and lama_studi <= 4)   # False
# Lowongan B: IPK min 3.50 ATAU lulus maks 4 tahun?
print(ipk >= 3.50 or lama_studi <= 4)   # True
print(not True)                         # False
```

**Ngomongnya (teaser):** "Pertemuan berikutnya, boolean jadi **otak** program: *'kalau IPK nggak memenuhi syarat, jangan kirim lamaran'*. Itu pakai `if`, kode yang tadi kalian tebak di awal."

---

### Slide 40 · 🎯 Latihan Bab 5 · 🎯 HANDS-ON · ⏱️ 4' · 🎓 NILAI A BAB 5
**➡️ Peserta ke section `Bab 5 · Ngitung IPK`** (jalankan data kit dulu, lalu satu cell per soal).

1. Hitung IPK Raka (total mutu / total SKS)
2. Bulatkan IPK jadi 2 desimal
3. Berapa tahun Raka kuliah? Berapa semester?
4. IPK memenuhi `IPK_MINIMAL`?
5. Memenuhi lowongan lain yang minta `3.50`?
6. 🟡 Bonus: cum laude? (IPK > 3.50 **dan** lulus maks 4 tahun)
7. 🔴 Tantangan: legalisir Rp7.500/lembar, uang Rp100.000: berapa lembar & sisa?

**Kunci:** `3.4513...` · `3.45` · `4` tahun / `8` semester · `True` · `False` · `False` · `13` lembar sisa `2500`

**Tebak output cepat:** `print(7 // 2, 7 % 2)` → (1) `3.5 0` · (2) `3 1` · (3) `3 0.5` → **(2)**

**➡️ Transisi:** "IPK beres! Tapi data diri Raka ditulis beda-beda di tiap dokumen. Kita rehat dulu."

---

### Slide 41 · ⏸️ Istirahat 10 menit · ⏸️ ISTIRAHAT · 01:12 – 01:22
**Di layar:** Timer 10 menit (klik untuk mulai) + teka-teki:
```python
print("10" + "5")
print(10 + 5)
```
"Kenapa hasilnya beda? Jawabannya setelah istirahat."

**Catatan trainer:** Hampiri peserta yang tadi 🔴. Cek apakah semua sudah sampai latihan Bab 5.

---

## BAB 6: Beresin Data Diri
**01:22 – 01:42 (20 menit)**
*String, indexing, slicing, method, casting*

### Slide 42 · 📖 Satu nama, tiga versi · 🧪 COLAB-DEMO · ⏱️ 1,5'
**Di layar:** Form online `"  raka PRATAMA putra "` · KTP `"RAKA PRATAMA PUTRA"` · CV `"Raka Pratama Putra   "`. "Buat manusia: orang yang sama. Buat sistem HRD: **tiga nama berbeda**."

**➡️ 🧪 Colab materi, section `Bab 6 · Beresin Data Diri`** (jalankan data kit teks).
```python
print(nama_form == nama_ktp)    # False 😱
```

**Ngomongnya:** "Sistem HRD sering mencocokkan data form dengan dokumen. Jawaban teka-teki tadi: `"10" + "5"` itu **teks digabung**, makanya `"105"`. Di akhir bab ini, `False` tadi akan jadi `True`."

---

### Slide 43 · String: untaian karakter · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
```python
nama_kampus = "Universitas Kenanga Raya"  # kutip dua
motto = 'Lulus, lalu kerja'               # kutip satu
alamat = """Jl. Kenanga No. 12
Bandung"""                                # kutip tiga
print("Raka" + " " + "Pratama")  # gabung
print("=" * 30)                  # ulang 30 kali
print(len(nama_ktp))             # 18 (spasi dihitung)
```

**Ngomongnya:** "`"=" * 30` ini nanti kita pakai buat garis di kartu lamaran Raka."

---

### Slide 44 · Indexing · 🧪 COLAB-DEMO · ⏱️ 2' · 🟢
**Di layar (visual interaktif, klik untuk menyorot):**
```
nomor_ijazah = "IJZ-20260915-STA-0457"

 karakter:  I   J   Z   -   2   0   2   6   0   9   1   5   -   S   T   A   -   0   4   5   7
 index +:   0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
 index -: -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
```
Struktur: `IJZ` - `tanggal lulus` - `kode prodi` - `nomor urut lulusan`

```python
print(nomor_ijazah[0])    # I ← mulai dari 0!
print(nomor_ijazah[-1])   # 7 ← dari belakang
print(len(nomor_ijazah))  # 21
print(nomor_ijazah[21])   # ❌ IndexError
```

**Interaksi:** "Panjangnya 21, berarti index terakhir berapa?" (20)

**Kamus Error:** **IndexError** = "Nomor urutnya kelewatan."

**Catatan trainer:** Nomor ijazah ini fiktif, formatnya dibuat supaya gampang dibongkar.

---

### Slide 45 · Slicing · 🧪 COLAB-DEMO · ⏱️ 2,5' · 🟢
**Di layar:** strip interaktif, tiap klik menyorot satu slice. Mental model: **"gunting memotong DI ANTARA karakter."**

```python
print(nomor_ijazah[0:3])     # IJZ
print(nomor_ijazah[:3])      # IJZ  ← start kosong = dari awal
print(nomor_ijazah[4:12])    # 20260915 (tanggal lulus)
print(nomor_ijazah[4:8])     # 2026 (tahun)
print(nomor_ijazah[13:16])   # STA (kode prodi)
print(nomor_ijazah[-4:])     # 0457 ← stop kosong = sampai akhir
```

**Interaksi:** Sebelum klik ke-3: "Ambilkan tahun lulusnya saja, index berapa sampai berapa?" → `[4:8]`

**Ngomongnya:** "Kenapa stop-nya nggak ikut? Biar gampang ngitung: `[4:12]` panjangnya pasti `12 - 4 = 8` karakter."

---

### Slide 46 · Slicing dengan langkah · 🧪 COLAB-DEMO · ⏱️ 1' · 🟡
```python
angka = "0123456789"
print(angka[::2])          # 02468
print(angka[1::2])         # 13579
print(nomor_ijazah[::-1])  # 7540-ATS-51906202-ZJI → dibalik!
```

---

### Slide 47 · String itu immutable · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
**Di layar:** "Kayak **ijazah yang sudah dicetak**: salah ketik nggak bisa dicoret, harus **cetak ulang**."

```python
nomor_ijazah[0] = "X"   # ❌ TypeError: 'str' object does not support item assignment

baru = nomor_ijazah.replace("STA", "INF")   # ✅ bikin string BARU
print(baru)            # IJZ-20260915-INF-0457
print(nomor_ijazah)    # IJZ-20260915-STA-0457 ← yang lama tetap
```

**Kamus Error:** **TypeError** = "Tipe datanya nggak cocok untuk operasi ini."

**Catatan trainer:** Ini analogi yang paling nempel di cerita. Ijazah salah cetak nggak bisa dicoret pakai tipe-x, harus dicetak ulang.

---

### Slide 48 · String method · 🧪 COLAB-DEMO · ⏱️ 3' · 🟢
**Di layar:** `.strip()` · `.upper()`/`.lower()` · `.title()` · `.replace(a, b)` · `.split("-")` (lainnya: `.count()` `.startswith()` `.center()`).

**Kode: momen "aha" bab ini**
```python
bersih_form = nama_form.strip().title()   # method bisa DIRANTAI
bersih_ktp = nama_ktp.strip().title()
print(bersih_form)                 # Raka Pratama Putra
print(bersih_form == bersih_ktp)   # True 🎉
```

**Jebakan (tebak output):**
```python
nama = "  raka  "
nama.upper()
print("[" + nama + "]")   # kurung siku biar spasinya kelihatan
```
(A) `[RAKA]` · (B) `[  RAKA  ]` · (C) `[  raka  ]` → **(C)**!

**Ngomongnya:** "String immutable. Method **nggak mengubah** aslinya, tapi **mengembalikan string baru**. Kalau mau disimpan: `nama = nama.upper()`."

**Catatan trainer:**
- Fun fact: `"pt data maju".title()` → `"Pt Data Maju"` (t-nya kecil). Makanya di final project nama perusahaan pakai `.upper()`.
- `.split()` menghasilkan **list**, jembatan ke Bab 7.

---

### Slide 49 · Casting · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟢
```python
nomor = nomor_ijazah[-4:]
print(nomor, type(nomor))        # 0457 <class 'str'>
lulusan_ke = int(nomor)          # nol di depan hilang
print(lulusan_ke)                # 457
print("Lulusan ke-" + str(457))  # angka → teks
print(float("3.45"))             # 3.45
print(float("3,45"))             # ❌ ValueError
```

**Ngomongnya:** "Data dari form online sering datang sebagai teks. Raka ngetik IPK `3,45` pakai koma, kebiasaan dari ijazah. Python protes: teksnya ada, tapi nggak bisa jadi angka."

**Kamus Error:** **ValueError** = "Tipenya benar, nilainya nggak masuk akal."

---

### Slide 50 · 🎯 Latihan Bab 6 · 🎯 HANDS-ON · ⏱️ 5,5' · 🎓 NILAI A BAB 6
**➡️ Peserta ke section `Bab 6 · Beresin Data Diri`** (jalankan data kit teks, jangan diketik ulang).

1. Rapikan ketiga versi nama → `"Raka Pratama Putra"`
2. Buktikan ketiganya sama (pakai `==` dan `and`)
3. Dari `nomor_ijazah`: tanggal `"20260915"`, kode prodi `"STA"`, nomor urut `"0457"`
4. Ubah nomor urut jadi angka `457`
5. 🟡 Bonus: tanggal lulus `"15-09-2026"`
6. 🔴 Tantangan: berapa huruf "a" di nama rapi?

**Kunci:**
```python
bersih_form = nama_form.strip().title()
bersih_ktp = nama_ktp.strip().title()
bersih_cv = nama_cv.strip().title()
print(bersih_form == bersih_ktp and bersih_ktp == bersih_cv)   # True
print(nomor_ijazah[4:12], nomor_ijazah[13:16], nomor_ijazah[-4:])
print(int(nomor_ijazah[-4:]))                                  # 457
print(nomor_ijazah[10:12] + "-" + nomor_ijazah[8:10] + "-" + nomor_ijazah[4:8])   # 15-09-2026
print(bersih_form.lower().count("a"))                          # 6
```

**➡️ Transisi:** "Data diri udah rapi. Tapi Raka punya 8 semester nilai, dan lowongannya makin banyak..."

---

## BAB 7: Wadah Banyak Barang
**01:42 – 01:52 (10 menit)**

### Slide 51 · "8 semester = 8 variabel?" → list · 🧪 COLAB-DEMO · ⏱️ 3,5' · 🟢
**➡️ 🧪 Colab materi, section `Bab 7 · Wadah Banyak Barang`.**

```python
ips = [3.20, 3.35, 3.50, 3.41, 3.60, 3.52, 3.38, 3.65]   # semester 1-8
print(ips[0])        # 3.2 ← indexing SAMA kayak string!
print(ips[-1])       # 3.65
print(ips[0:2])      # [3.2, 3.35]
print(len(ips), sum(ips) / len(ips))   # 8 3.45125
print(max(ips), min(ips))              # 3.65 3.2
print(sorted(ips, reverse=True))

ips[3] = 3.45                          # nilai direvisi dosen: list BISA diubah
lowongan = ["PT Data Maju", "PT Awan Biru"]
lowongan.append("CV Tiga Kode")        # nemu lowongan baru
```

**Ngomongnya:**
- "Semua ilmu indexing string **berlaku juga di list**."
- "Bedanya: string **immutable**, list **mutable**."
- "Raka ambil 18 SKS tiap semester, jadi rata-rata IPS = IPK: 3.45."

---

### Slide 52 · tuple · 🧪 COLAB-DEMO · ⏱️ 1' · 🟡
```python
TANGGAL_LAHIR = (12, 3, 2004)
print(TANGGAL_LAHIR[2])          # 2004
print(2026 - TANGGAL_LAHIR[2])   # 22 (usia Raka)
TANGGAL_LAHIR[2] = 2005          # ❌ TypeError: 'tuple' object does not support item assignment
```

**Ngomongnya:** "Tuple = list yang **dikunci**. Cocok buat tanggal lahir: nggak bisa muda-in umur. 😄"

---

### Slide 53 · set · 🧪 COLAB-DEMO · ⏱️ 1,5' · 🟡 (frozenset ⚪)
```python
semua_skill = ["Python", "Excel", "SQL", "Python", "Excel", "Tableau"]
skill_unik = set(semua_skill)
print(skill_unik)        # {'Python', 'Excel', 'SQL', 'Tableau'} (urutan bisa beda!)
print(len(skill_unik))   # 4
skill_wajib = frozenset(["Python", "SQL"])   # kenalan aja
```

**Ngomongnya:** "Skill dari CV, LinkedIn, dan portofolio digabung, ada yang dobel. Set otomatis **membuang duplikat** dan **tidak punya urutan**."

---

### Slide 54 · dict: transkrip · 🧪 COLAB-DEMO · ⏱️ 2' · 🟢
```python
transkrip = {
    "Statistika Dasar": "A",
    "Basis Data": "A-",
    "Pemrograman Python": "B+",
}
print(transkrip["Basis Data"])       # A- ← akses pakai KUNCI
transkrip["Machine Learning"] = "A"  # tambah mata kuliah
print(transkrip["Kalkulus 3"])       # ❌ KeyError

biodata = {"nama": "Raka Pratama Putra", "ipk": 3.45}
print(biodata["ipk"])                # 3.45
```

**Ngomongnya:** "List: cari pakai nomor urut. Dict: cari pakai **nama**. HRD nggak nanya 'nilai mata kuliah nomor 2', tapi 'nilai Basis Data berapa?'"

**Kamus Error:** **KeyError** = "Kunci ini nggak ada di dict."

---

### Slide 55 · Pilih wadah yang tepat · 🖥️ SLIDE · ⏱️ 2' · 🎓 NILAI A BAB 7
**Di layar:** Tabel list/tuple/set/dict (urut? bisa diubah? duplikat? contoh Raka).

**Kuis cepat** (klik untuk buka jawaban):
1. Lowongan yang dilamar, urut tanggal → **list**
2. Koordinat kantor → **tuple**
3. Perusahaan unik yang pernah dilamar → **set**
4. Gaji per posisi (`"Data Analyst": 6500000`) → **dict**

**➡️ Transisi:** "Semua data udah rapi di wadahnya. Tinggal satu: **menyajikan** lamarannya ke HRD."

---

## BAB 8: Surat Lamaran Rapi
**01:52 – 02:07 (15 menit)**

### Slide 56 · print() lebih jauh & escape character · 🧪 COLAB-DEMO · ⏱️ 2' · 🟡
**➡️ 🧪 Colab materi, section `Bab 8 · Surat Lamaran Rapi`.**

| Escape | Arti |
|---|---|
| `\n` | baris baru |
| `\t` | tab |
| `\"` `\'` | kutip di dalam teks |
| `\\` | garis miring terbalik |

```python
print("Lampiran:", "Ijazah", "Transkrip", sep=" | ")
print("Hal:\tLamaran \"Data Analyst\"\nLampiran:\t3 berkas")
```

**Catatan trainer:** Jebakan klasik: `print("C:\data\new")` → `\n` jadi baris baru. Solusi: `"C:\\data\\new"` atau `r"C:\data\new"`.

---

### Slide 57 · 📖 Raka mencoba bikin surat... · 🧪 COLAB-DEMO · ⏱️ 1'
```python
ipk = 3.45
print("IPK saya: " + ipk)
# ❌ TypeError: can only concatenate str (not "float") to str
```

**Ngomongnya:** "Teks + angka = nggak bisa digabung langsung. Python punya beberapa solusi dari zaman ke zaman."

---

### Slide 58 · Evolusi string formatting · 🖥️ SLIDE · ⏱️ 2' · 🟢 f-string · ⚪ `%` & `.format`
```python
print("IPK saya: " + str(ipk))     # 1. casting manual → ribet
print("IPK saya: %.2f" % ipk)      # 2. gaya %  (jadul)
print("IPK saya: {}".format(ipk))  # 3. .format()
print(f"IPK saya: {ipk}")          # 4. f-string ⭐ pakai ini!
```

**Ngomongnya:** "Kenali cara 2 & 3 karena masih sering muncul di kode orang. Tapi kalau nulis sendiri, pakai **f-string**."

---

### Slide 59 · Kekuatan super f-string · 🧪 COLAB-DEMO · ⏱️ 3' · 🟢

| Format | Contoh | Hasil |
|---|---|---|
| Variabel | `f"{perusahaan}"` | `PT Data Maju` |
| Hitungan | `f"{total_mutu / total_sks}"` | `3.4513...` |
| Ribuan | `f"{GAJI_HARAPAN:,}"` | `6,500,000` |
| 2 desimal | `f"{3.451388:.2f}"` | `3.45` |
| Method | `f"{posisi.upper()}"` | `DATA ANALYST` |

```python
perusahaan = "PT Data Maju"
print(f"Yth. HRD {perusahaan},")                     # nggak ketuker lagi!
print(f"Gaji: Rp{GAJI_HARAPAN:,}")                   # Rp6,500,000
print(f"Gaji: Rp{GAJI_HARAPAN:,}".replace(",", "."))  # Rp6.500.000
print(f"IPK : {total_mutu / total_sks:.2f}")         # 3.45
```

**Ngomongnya:** "Ingat insiden *'Yth. HRD PT Awan Biru'*? Dengan f-string, nama perusahaan diambil dari variabel. Ganti satu variabel, semua surat ikut benar. Dan trik `.replace(",", ".")` itu **string method dari Bab 6**. Semua mulai nyambung."

---

### Slide 60 · input() · 🧪 COLAB-DEMO · ⏱️ 2,5' · 🟢
```python
perusahaan = input("Nama perusahaan: ")
print(f"Yth. HRD {perusahaan},")
```

**Tebak output (jangan dilewati!):** "Raka sudah melamar 10 lowongan, targetnya bulan depan 2x lipat."
```python
jumlah = input("Sudah melamar? ")   # ketik: 10
print(jumlah * 2)
```
(A) `20` · (B) `1010` · (C) Error → **(B) `1010`**

**Perbaikan:**
```python
jumlah = int(input("Sudah melamar? "))
print(jumlah * 2)    # 20
```

**Ngomongnya:** "**`input()` selalu menghasilkan string**. `"10" * 2` = teks diulang 2 kali. Sama kayak teka-teki sebelum istirahat."

**Catatan trainer:** Di Colab, `input()` memunculkan kotak isian dan cell terlihat "berputar" sampai kita tekan **Enter**. Pemula sering mengira Colab hang.

---

### Slide 61 · 🎯 Latihan Bab 8 · 🎯 HANDS-ON · ⏱️ 4,5' · 🎓 NILAI A BAB 8
**➡️ Peserta ke section `Bab 8 · Surat Lamaran Rapi`.**

1. Minta nama perusahaan & posisi lewat `input()`, rapikan posisi pakai `.strip().title()`
2. Cetak header:
   ```
   ==============================================
   KARTU LAMARAN RAKA
   Perusahaan : PT Data Maju
   Posisi     : Data Analyst
   ==============================================
   ```
3. Cetak ekspektasi gaji format Rupiah: `Rp6.500.000`
4. 🟡 Bonus: pembuka surat `Yth. HRD <perusahaan>,` dan `saya <nama>, ingin melamar posisi <posisi>.`

**Kunci:**
```python
perusahaan = input("Nama perusahaan: ").strip()
posisi = input("Posisi: ").strip().title()
garis = "=" * 46
print(garis)
print("KARTU LAMARAN RAKA")
print(f"Perusahaan : {perusahaan}")
print(f"Posisi     : {posisi}")
print(garis)
print(f"Ekspektasi gaji : Rp{GAJI_HARAPAN:,}".replace(",", "."))
print(f"Yth. HRD {perusahaan},")
print(f"saya {nama_lengkap}, ingin melamar posisi {posisi}.")
```

**➡️ Transisi:** "8 nilai A. Saatnya ujian akhir: **kartu lamaran otomatis Raka**."

---

## FINAL: Satu Klik, Lamaran Jadi
**02:07 – 02:22 (15 menit)**

### Slide 62 · Misi: Kartu Lamaran Raka v1.0 · 🖥️ SLIDE · ⏱️ 2'
**Di layar:** Target output (lihat [bagian 7](#7-kode-final--template-peserta)) + level:
- 🟢 **Wajib**: isi semua `___` di template sampai kartu tampil
- 🟡 **Bonus**: baris "Cum laude?" (IPK > 3.50 **and** lama studi <= 4)
- 🔴 **Tantangan**: rata-rata IPS 4 semester terakhir (`ips[-4:]`, `sum`, `len`)

**Ngomongnya:** "Tiap baris kartu ini pakai sesuatu yang kalian pelajari hari ini. Coba tebak, baris 'Tanggal lulus' pakai ilmu dari bab berapa?" (Bab 6: slicing nomor ijazah)

---

### Slide 63 · 🎯 Kerjakan! · 🎯 HANDS-ON · ⏱️ 10'
**➡️ Peserta ke section `Final · Kartu Lamaran v1.0`** (template di [bagian 7](#template-peserta)). Timer 10 menit ada di slide.

**Tangga petunjuk:**
1. 🔎 Cek komentar `[Bab X]` di template
2. 📓 Scroll ke latihan bab itu di notebook-mu
3. 🙋 Tanya teman sebelah (boleh *pair programming*)
4. 🔴 Angkat sinyal merah, trainer datang

**Catatan trainer:** Sampaikan di awal: `___` yang tersisa memicu `NameError: name '___' is not defined`. Keliling, prioritaskan peserta 🔴. Yang selesai cepat → 🟡/🔴 atau jadi asisten. Menit ke-8: "2 menit lagi".

---

### Slide 64 · Momen "aha": dari notebook ke script · 💻 VSCODE · ⏱️ 3'
**➡️ Pindah ke VSCode**, buka `lamaran-raka/kartu_lamaran.py`.

```bash
cd lamaran-raka
python3 kartu_lamaran.py
```

Jalankan **2 kali**: PT Data Maju (IPK minimal 3.00 → `True`), lalu PT Awan Biru (3.50 → `False`).

**Ngomongnya (penutup arc cerita):** "Ini yang sekarang dijalankan Raka tiap ada lowongan baru. Satu perintah. **90 menit jadi 1 detik.** Nggak ada lagi 'Yth. HRD PT Awan Biru'. Dan yang nulis kodenya... kalian."

**Show & tell:** 1–2 peserta share screen hasil mereka. Beri apresiasi.

---

## EPILOG: Bersambung...
**02:22 – 02:30 (8 menit)**

### Slide 65 · Isi tas Raka · 🖥️ SLIDE · ⏱️ 2'

| Masalah Raka | Alat yang dipakai |
|---|---|
| Data diri berserakan | Variabel & konstanta |
| Hitung IPK, lama studi | Operator, `round`, `max`, `min` |
| Cek syarat lowongan | Boolean & perbandingan |
| Nama beda-beda di tiap dokumen | `.strip()`, `.title()` |
| Ambil info dari nomor ijazah | Indexing, slicing, `int()` |
| Nilai per semester, transkrip | `list`, `dict`, `sum`, `len` |
| Surat & kartu lamaran rapi | f-string, `\t`, `"=" * 46`, `input()` |
| Error | Baca dari baris paling bawah |

**Interaksi:** "Dari semua ini, mana yang paling bikin kalian 'ooh!'?"

---

### Slide 66 · 📖 Raka masih punya masalah · 🖥️ SLIDE · ⏱️ 2'
1. 😐 "Data lowongan masih diketik manual." → **Baca file CSV/Excel** (pandas)
2. 🏅 "Predikatku apa: cum laude, sangat memuaskan?" → **`if` / `elif` / `else`**
3. 🔁 "30 lowongan = jalanin script 30 kali?" → **Loop** (`for`)
4. ♻️ "Pengen bikin mesin `cek_syarat()` sendiri." → **Function** buatan sendiri

**Ngomongnya:** "Kalian sendiri ngerasain kan: tiap lowongan baru, script harus dijalankan ulang. Bayangin 30 lowongan. Itu yang akan kita selesaikan di pertemuan berikutnya. **Bersambung...** 🎓"

**Catatan trainer:** Sesuaikan kartu dengan silabus pertemuan berikutnya.

---

### Slide 67 · Latihan mandiri · 🖥️ SLIDE · ⏱️ 2'

| Urutan | Platform | Kenapa | Mulai dari |
|---|---|---|---|
| 1 | [Codesaya](https://codesaya.com/python) | Bahasa Indonesia, interaktif | Modul Python dasar |
| 2 | [Kaggle Learn: Python](https://www.kaggle.com/learn/python) | Gratis, berbasis notebook | Lesson 1–2 |
| 3 | [HackerRank](https://www.hackerrank.com/domains/python) | Soal bertingkat + auto-check | Introduction, Basic Data Types, Strings |
| 4 | [LeetCode](https://leetcode.com) | Soal algoritma | **Nanti dulu**, setelah paham `if`, loop, function |

**PR:**
1. Baris "Cum laude?" di kartu lamaran
2. Rata-rata IPS 4 semester terakhir (2 desimal)
3. Bikin kartu untuk PT Awan Biru (IPK min 3.50) dan CV Tiga Kode (2.75). Rasakan berapa kali harus jalanin ulang.

**Catatan trainer:** PR nomor 3 sengaja membuat peserta *merasakan* repotnya tanpa loop. Bonus cerita: portofolio GitHub berisi script seperti ini juga nilai plus waktu melamar kerja.

---

### Slide 68 · Exit ticket 3-2-1 · 🖥️ SLIDE · ⏱️ 1'
**3** hal yang dipelajari · **2** hal yang masih bikin bingung · **1** pertanyaan.

**Catatan trainer:** Baca jawaban "2 hal bingung" sebelum pertemuan berikutnya, lalu buka pertemuan berikutnya dengan review 5 menit.

---

### Slide 69 · Selamat, kalian lulus · 🖥️ SLIDE · ⏱️ 1'
**Di layar:** "Selamat, kalian **lulus**." Transkrip penuh 8/8 + LULUS. Link repo, materi, kunci jawaban, komunitas.

**Ngomongnya:** "Hari ini kalian udah nulis program pertama yang benar-benar berguna. Error akan terus datang. Itu tanda kalian sedang belajar, bukan tanda kalian nggak bisa."

---

## 7. Kode final + template peserta

### Kode final (kunci jawaban, sudah dites)
Ada di [lamaran-raka/kartu_lamaran.py](lamaran-raka/kartu_lamaran.py) (VSCode), section `00 · Demo Final` di `01_materi_ijazah_raka.ipynb`, dan section `Final` di `03_kunci_jawaban.ipynb`.

```python
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
```

**Output** (input: `pt data maju`, ` data analyst `, `3.00`):
```
==============================================
       KARTU LAMARAN RAKA PRATAMA PUTRA
==============================================
Perusahaan       : PT DATA MAJU
Posisi           : Data Analyst
----------------------------------------------
Nama             : Raka Pratama Putra (22 th)
Kampus           : Universitas Kenanga Raya
Jurusan          : Statistika
Nomor ijazah     : IJZ-20260915-STA-0457
Tanggal lulus    : 15-09-2026 (lulusan ke-457)
----------------------------------------------
Total SKS        : 144
IPK              : 3.45
IPS terbaik      : 3.65
Skill            : Python, Excel, SQL
Ekspektasi gaji  : Rp6.500.000
----------------------------------------------
IPK minimal      : 3.00
Memenuhi syarat? : True
==============================================
Yth. HRD PT DATA MAJU,
saya Raka Pratama Putra, lulusan Statistika
Universitas Kenanga Raya dengan IPK 3.45,
ingin melamar posisi Data Analyst.
```

**Kunci bonus 🟡 & tantangan 🔴:**
```python
lama_studi = 2026 - 2022
cum_laude = ipk > 3.50 and lama_studi <= 4
print(f"Cum laude?       : {cum_laude}")             # False

rata_akhir = sum(ips[-4:]) / len(ips[-4:])
print(f"Rata-rata 4 smt  : {rata_akhir:.2f}")        # 3.54
```

### Template peserta
Ada di section `Final · Kartu Lamaran v1.0` pada `02_latihan_peserta.ipynb` dan di [lamaran-raka/kartu_lamaran_template.py](lamaran-raka/kartu_lamaran_template.py). Bagian data sudah diisi supaya fokus ke logika; peserta mengisi `___` di input (posisi, IPK minimal), olah data (IPK, IPS terbaik, usia, memenuhi syarat, nama rapi, lulusan ke-), dan beberapa baris `print`.

**Catatan trainer:** Kalau peserta menjalankan template yang belum lengkap, `___` akan memicu `NameError: name '___' is not defined`. Itu justru penanda "masih ada yang belum diisi".

---

## 8. Kamus Error

Tampilkan bertahap selama kelas (entri ditambah saat error itu pertama muncul). Di akhir kelas, peserta sudah "kenal" 7 error.

| Error | Bahasa manusianya | Muncul di | Contoh | Biasanya karena |
|---|---|---|---|---|
| `NameError` | "Aku nggak kenal nama ini" | Slide 15, 23, 27, 38 | `prnt(...)`, `print(Raka)`, `true` | Typo, lupa kutip, cell belum di-run, huruf besar/kecil |
| `SyntaxError` | "Tata bahasanya salah" | Slide 30, 33 | `1nama = "Raka"`, `tahun lulus = 2026` | Melanggar aturan penulisan, kurung/kutip tidak ditutup |
| `IndentationError` | "Ada spasi nyasar di awal baris" | (antisipasi) | `   print("hai")` | Copy-paste dari web/chat |
| `TypeError` | "Tipenya nggak cocok untuk operasi ini" | Slide 31, 47, 52, 57 | `"IPK saya: " + 3.45`, `nomor_ijazah[0] = "X"` | Campur teks & angka, mengubah yang immutable, nama built-in ketimpa |
| `IndexError` | "Nomor urutnya kelewatan" | Slide 44 | `nomor_ijazah[21]` | Lupa index mulai dari 0 |
| `ValueError` | "Tipenya benar, nilainya nggak masuk akal" | Slide 49 | `float("3,45")` | Desimal pakai koma, teks bukan angka |
| `KeyError` | "Kunci ini nggak ada di dict" | Slide 54 | `transkrip["Kalkulus 3"]` | Typo / kunci memang belum ada |

**Tentang `IndentationError`:** Kalau muncul (biasanya saat peserta paste kode dari chat), jelaskan: *"Di Python, spasi di awal baris itu bermakna, nanti dipakai di `if` dan loop. Untuk sekarang, semua baris mulai dari paling kiri."*

---

## 9. FAQ trainer

**"Sekarang kan ada AI yang bisa ngoding. Ngapain belajar?"**
AI adalah asisten yang hebat, tapi kalian tetap harus bisa **membaca, mengecek, dan memperbaiki** kodenya. Tanpa paham dasar, kalian nggak bisa tahu kode dari AI itu benar atau salah. Dan di wawancara kerja Data Analyst, tes coding dasar masih sering dipakai.

**"Python lambat ya?"**
Dibanding C, iya, untuk eksekusi murni. Tapi library data populer (numpy, pandas) di dalamnya ditulis dengan C, jadi tetap cepat. Untuk data analyst, yang lebih penting adalah **cepat sampai ke jawaban**.

**"Python 2 atau 3?"**
Selalu Python 3. Python 2 sudah pensiun sejak 2020.

**"Harus hafal semua function & method?"**
Tidak. Cukup tahu *ada*, lalu tahu cara mencarinya: `?`, `help()`, Tab di Colab, dokumentasi, Google, AI.

**"Kenapa `0.1 + 0.2` hasilnya `0.30000000000000004`?"**
Komputer menyimpan desimal dalam basis 2, dan beberapa desimal (seperti 0.1) tidak bisa disimpan persis. Untuk uang: pakai `int` (Rupiah) atau modul `decimal`; untuk tampilan: bulatkan dengan `round()` atau f-string `:.2f`.

**"Kenapa `round(2.5)` hasilnya 2, bukan 3?"**
Python memakai *banker's rounding*: angka .5 dibulatkan ke **genap** terdekat (`round(2.5)` → 2, `round(3.5)` → 4).

**"Kenapa `print(ips[0])` keluarnya `3.2`, bukan `3.20`?"**
Float tidak menyimpan nol di belakang koma. Kalau mau tampil 2 desimal, pakai f-string: `f"{ips[0]:.2f}"` → `3.20`.

**"Kenapa `True + True` hasilnya 2?"**
Di Python, `bool` adalah turunan `int`: `True` = 1, `False` = 0. Berguna untuk menghitung, misalnya berapa lowongan yang syaratnya terpenuhi.

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

**"Nomor ijazah asli formatnya begitu?"**
Tidak. Format `IJZ-20260915-STA-0457` dibuat khusus untuk kelas supaya gampang dibongkar dengan slicing. Semua data di cerita fiktif.

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
- Siapkan **"kartu jalur ngebut"** (tantangan 🔴) di setiap latihan
- Pasangkan peserta berpengalaman dengan pemula (*pair programming*)
- Minta yang cepat jadi "asisten" di final project

### Kalau teknis bermasalah
- **Colab lambat / down**: pakai Jupyter lokal / VSCode dengan notebook yang sama (unduh `.ipynb` dari repo)
- **Internet peserta putus**: pasangkan dengan teman (satu layar berdua)
- **VSCode trainer error saat demo**: tunjukkan di terminal biasa (`python3 kartu_lamaran.py`)

---

## 11. Catatan perubahan dari outline asli

Supaya kamu tahu apa yang aku ubah dari [python_dbb.md](python_dbb.md) dan alasannya.

### Urutan
| Perubahan | Alasan |
|---|---|
| **"Kenapa perlu coding" dipindah sebelum "Apa itu Python"** | Motivasi dulu, solusi kemudian. Peserta perlu merasakan masalahnya sebelum dikenalkan alatnya |
| **Basic Code diurutkan ulang:** komentar & print → variabel → angka & bool → string → koleksi → formatting & input | `print` & variabel dibutuhkan untuk mencoba apa pun; string sebelum list supaya ilmu indexing bisa dipakai ulang; formatting di akhir karena itu "hadiah" yang menyatukan semuanya |
| **Built-in function disebar** ke bab yang relevan | Function dikenalkan saat dibutuhkan (`type` di variabel, `round/max/min` di angka, `len` di string, `sum` di list) |
| **Hands-on dipecah** jadi kecil-kecil di tiap bab + 1 final project | Aturan 10 menit; latihan langsung setelah konsep lebih efektif |

### Koreksi istilah
| Di outline | Seharusnya | Catatan |
|---|---|---|
| `boox` | `bool` | typo |
| "Pake true sama false" | `True` / `False` | Huruf depan wajib kapital; `true` → `NameError`. Dijadikan demo error di Slide 38 |
| "bisa di casing juga, int("10")" | **casting** (konversi tipe) | Dipindah ke Slide 49 sebagai konsep sendiri |
| "Capital case untuk nama kelas" | **PascalCase** / CapWords | Istilah di PEP 8 |
| "Fradulent" | rawan salah | Dibingkai di Slide 9 |
| "reserved: built in function" | Yang benar-benar **reserved** adalah **keyword**. Nama built-in function **boleh** dipakai tapi berbahaya | Dipisah jadi 2 slide: aturan wajib (Slide 30) vs jebakan (Slide 31) |
| "di notebook bisa pake ?" | `?` (khusus notebook) + `help()` (di mana saja) | Ditambah `help()` supaya berlaku juga di VSCode |

### Tambahan
- `sum()`, `sorted()`, `%` (modulo), `.split()`, `.center()`: sering dipakai & dibutuhkan final project
- **Cara membaca error** (Slide 23) + **Kamus Error**
- **IndexError**, **ValueError** (`float("3,45")`), dan **KeyError**: muncul alami di cerita
- Catatan jebakan notebook: urutan menjalankan cell

### Penyesuaian kedalaman (karena 2,5 jam untuk pemula)
- ⚪ **Kenalan saja**: `complex`, `frozenset`, `%` formatting, `.format()`, nuansa interpreted vs compiled, package manager, virtual env
- 🟢 **Fokus dikuasai**: variabel, int/float/str/bool, operator, indexing/slicing dasar, string method, list & dict, f-string, input + casting
- **LeetCode** diposisikan "nanti dulu": soal-soalnya butuh `if`, loop, dan function

---

## 12. Lampiran: Cheat sheet peserta

```python
# ===== CHEAT SHEET PYTHON PERTEMUAN 1 · IJAZAH RAKA =====

# Komentar: diawali #, dilewati Python
print("Halo", 144)            # tampilkan ke layar
type(3.45)                    # cek tipe data → float

# VARIABEL: nama = nilai  (snake_case, KONSTANTA pakai UPPER_CASE)
total_sks = 144
IPK_MINIMAL = 3.00
del total_sks                 # hapus variabel

# ANGKA
144 / 8         # 18.0 (selalu float)
100_000 // 7_500  # 13 (bagi bulat)
100_000 % 7_500   # 2500 (sisa bagi)
2 ** 3          # 8 (pangkat)
abs(-4), round(3.4513, 2), max(3.2, 3.65), min(3.2, 3.65)

# BOOLEAN: True / False (kapital!)
3.45 >= 3.00, 3.45 == 3.45, 3.45 != 3.50   # perbandingan (= masukkan, == bandingkan)
True and False, True or False, not True

# STRING
s = "IJZ-20260915-STA-0457"
s[0], s[-1]                   # index (mulai dari 0)
s[4:12], s[:3], s[-4:]        # slicing [start:stop], stop tidak ikut
s[::-1]                       # dibalik
len(s)                        # panjang
"  raka PRATAMA  ".strip().title()   # method bisa dirantai, hasilnya string BARU
s.replace("STA", "INF"), s.split("-"), s.lower(), s.upper(), s.count("0")
int("0457"), float("3.45"), str(457)   # casting (desimal pakai TITIK!)

# KOLEKSI
ips = [3.20, 3.35, 3.50, 3.65]        # list : urut, bisa diubah
lahir = (12, 3, 2004)                 # tuple: urut, dikunci
skill = {"Python", "SQL", "Python"}   # set  : unik, tanpa urutan
transkrip = {"Basis Data": "A-"}      # dict : kunci → nilai
sum(ips), len(ips), sorted(ips), ips.append(3.70), transkrip["Basis Data"]

# OUTPUT & INPUT
print(f"Gaji: Rp{6500000:,}".replace(",", "."))   # Rp6.500.000
print(f"IPK: {3.451388:.2f}")                      # 3.45
print("Baris1\nBaris2\tTab \"kutip\"")
perusahaan = input("Perusahaan: ")      # input SELALU string
ipk_min = float(input("IPK minimal: ")) # ubah ke angka

# BINGUNG?  round?   help(round)   ketik "teks." lalu Tab
# ERROR?    baca baris PALING BAWAH dulu → cek nomor baris → cek typo/kutip/kurung
```
