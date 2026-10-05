# ☕ Laporan Pagi Raka: Python Fundamentals & Logic

Materi kelas Python untuk **pemula total** (1 pertemuan, 2,5 jam), dibangun sebagai **satu cerita**: membantu Raka, data analyst di kedai *Kopi Senja*, mengubah laporan harian yang dikerjakan manual selama 65 menit menjadi script Python yang selesai dalam 1 detik.

> 📊 **Slide:** https://thosangs.github.io/python_lecture/ · neo-brutalist × toska × kuning, dark mode default

| Notebook | Isi | Buka |
|---|---|---|
| `01_materi_kopi_senja.ipynb` | Semua demo per bab, **sudah dijalankan** (termasuk error yang sengaja dibuat) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/01_materi_kopi_senja.ipynb) |
| `02_latihan_peserta.ipynb` | Lembar latihan peserta: data kit, latihan per bab, template final (sengaja **tanpa output**) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb) |
| `03_kunci_jawaban.ipynb` | Kunci jawaban latihan, **sudah dijalankan** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/03_kunci_jawaban.ipynb) |

## Alur cerita

| Bab | Masalah Raka | Konsep |
|---|---|---|
| Prolog | Laporan manual 65 menit/hari | Demo hasil akhir |
| 1 · Kenapa Raka Harus Ngoding? | Repetitif, membosankan, rawan salah | Otomasi & konsistensi |
| 2 · Kenalan sama Python | "Pakai bahasa apa?" | High-level, interpreted, general purpose |
| 3 · Nyiapin Meja Kerja | "Ngodingnya di mana?" | Dev environment, Colab, VSCode |
| 4 · Toples Berlabel | Angka berserakan | Komentar, `print`, variabel, aturan nama |
| 5 · Ngitung Omzet | Total, rata-rata, cek target | `int`, `float`, operator, boolean |
| 6 · Beresin Nama Menu | Nama menu berantakan | String, indexing, slicing, method, casting |
| 7 · Wadah Banyak Barang | "Kalau cabangnya 30?" | `list`, `tuple`, `set`, `dict` |
| 8 · Laporan buat Bu Sari | Laporan harus rapi & bisa diisi | Escape char, f-string, `input()` |
| Final · Satu Klik, Laporan Jadi | Gabungkan semuanya | [`kopi-senja/laporan.py`](kopi-senja/laporan.py) |

## Isi repo

```
.
├── slides/                    # deck Slidev → GitHub Pages
│   ├── slides.md              # 69 slide + catatan presenter
│   ├── style.css              # tema neo-brutalist (dark default, light tersedia)
│   ├── slide-bottom.vue       # navigasi: bab · kartu stempel · penanda Colab/VSCode · nomor slide
│   ├── slide-top.vue          # progress bar
│   └── components/            # StampCard, Goto, Predict, IndexStrip, Jar, Countdown
├── notebooks/                 # 3 notebook (materi & kunci sudah dijalankan)
├── kopi-senja/
│   ├── laporan.py             # script final, untuk demo VSCode
│   └── laporan_template.py    # template isi-titik-titik
├── tools/run_notebooks.py     # jalankan ulang notebook & simpan output
├── python_dbb_alur_slide.md   # panduan trainer: alur per slide, pedagogi, FAQ, rencana cadangan
└── .github/workflows/deploy-slides.yml
```

## Menjalankan

**Slide (lokal)**

```bash
cd slides
npm install
npm run dev
```

Buka http://localhost:3030. Navigasi: panah kiri/kanan · `o` overview · `g` loncat ke slide · `d` dark/light · `f` fullscreen. Mode presenter (dengan catatan trainer per slide): http://localhost:3030/presenter.

**Script laporan**

```bash
cd kopi-senja
python3 laporan.py
```

**Jalankan ulang notebook** (setelah mengedit `01` atau `03`)

```bash
pip install nbformat nbclient ipykernel
python tools/run_notebooks.py
```

Cell yang memakai `input()` diberi jawaban otomatis lewat metadata `mock_input`, jadi output di notebook tetap terlihat seperti diketik di Colab.

## Deploy

Setiap push ke `main` yang mengubah `slides/` otomatis membangun dan men-deploy slide ke GitHub Pages lewat GitHub Actions. Sekali saja di awal: **Settings → Pages → Source: GitHub Actions**.

## Navigasi slide

Footer setiap slide menampilkan:
- **bab aktif** (kiri)
- **progres kartu stempel**: 8 kotak, hijau toska = selesai, kuning = sedang berjalan (tengah)
- **penanda lokasi**: 🧪 Colab · demo, 🎯 Hands-on, 💻 VSCode, ⏸️ Istirahat, beserta section notebook yang harus dibuka (kanan)
- **nomor slide**, sama persis dengan penomoran di [panduan trainer](python_dbb_alur_slide.md)
