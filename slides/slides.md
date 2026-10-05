---
theme: default
title: Laporan Pagi Raka — Python Fundamentals & Logic
info: |
  Kelas Python untuk pemula (2,5 jam), satu cerita: membantu Raka, data analyst Kopi Senja,
  mengotomasi laporan harian. Neo-brutalist × toska × kuning.
author: thosangs
colorSchema: auto
class: text-left
transition: slide-left
mdc: true
canvasWidth: 980
aspectRatio: 16/9
fonts:
  sans: Space Grotesk
  mono: JetBrains Mono
  provider: none
drawings:
  enabled: false
presenter: true
download: false
lineNumbers: false
layout: cover
section: Prolog · Senin Pagi di Kopi Senja
bab: 0
footer: false
---

<div class="cover-frame"></div>

<div class="eyebrow">// Python Fundamentals &amp; Logic · Pertemuan 1</div>

# Laporan Pagi <span class="hl">Raka</span>

<div class="lead">Dari Excel manual ke laporan otomatis.</div>

<div class="row mt-8" style="max-width: 700px">
  <div class="card pop"><div class="box-h">Durasi</div><b>2,5 jam</b></div>
  <div class="card pop"><div class="box-h">Level</div><b>Pemula</b></div>
  <div class="card pop"><div class="box-h">Mode</div><b>Cerita + live coding</b></div>
</div>

<div class="sticker" style="position:absolute; right: 70px; top: 90px; font-size: 1rem">☕ Kopi Senja Edition</div>

<!--
⏱️ 00:00 · 1 menit

- Perkenalan singkat diri (maks 30 detik), langsung ke slide berikutnya.
- "Satu cerita, 2,5 jam, dan kalian yang nulis kodenya."
- Tips navigasi: `o` = overview, `g` = loncat ke nomor slide, `d` = toggle dark/light. Mode presenter: tambahkan `/presenter` di URL.
-->

---

<div class="eyebrow">// Sebelum mulai</div>

## Angkat tangan ✋

<div class="grid grid-cols-3 gap-6 mt-8">
  <div class="card pop"><div class="num">01</div><div class="point mt-4">Pakai Excel tiap hari?</div></div>
  <div class="card pop-yl"><div class="num">02</div><div class="point mt-4">Kerjaan sama, berulang?</div></div>
  <div class="card pop"><div class="num">03</div><div class="point mt-4">Pernah ngoding?</div></div>
</div>

<div class="mt-10 lead">Kenalin, Raka 👉</div>

<!--
⏱️ 1 menit · KALIBRASI

Tanyakan:
1. Siapa yang pakai Excel/Spreadsheet hampir tiap hari?
2. Siapa yang pernah ngerjain hal yang sama berulang-ulang tiap hari/minggu di laptop?
3. Siapa yang pernah ngoding, bahasa apa pun?

- Catat dalam hati proporsi yang pernah ngoding. Banyak → siapkan tantangan 🔴. Hampir semua belum → lambatkan Bab 4–6.
- "Kalau nomor 2 banyak yang angkat tangan... kalian nggak sendirian. Kenalin, Raka."
-->

---

<div class="eyebrow">// Tokoh utama</div>

## Kenalan sama Raka

<div class="grid grid-cols-[1fr_1.3fr] gap-10 mt-4 items-center">
  <div class="card pop-yl" style="text-align:center; padding: 26px">
    <div style="font-size: 6rem; line-height: 1">🧑‍💻</div>
    <div class="huge" style="font-size: 3rem; margin-top: 12px">RAKA</div>
    <div class="muted mono small">Data analyst · 3 bulan</div>
  </div>
  <div class="stack">
    <div class="card">
      <div class="point sm">☕ Kopi Senja · 3 cabang</div>
      <div class="mt-3 flex gap-2">
        <span class="tag wajib">JKT</span>
        <span class="tag wajib">BDG</span>
        <span class="tag wajib">SBY</span>
      </div>
    </div>
    <div class="card"><div class="point sm">📱 Bu Sari nunggu laporan jam 08.00</div></div>
  </div>
</div>

<!--
⏱️ 1 menit

- Raka: data analyst baru (3 bulan) di Kopi Senja, kedai kopi dengan 3 cabang (Jakarta, Bandung, Surabaya).
- Bu Sari: owner, tiap pagi jam 08.00 nunggu laporan penjualan kemarin di WhatsApp.
- "Raka ini mirip banyak dari kita: jago Excel, rajin, tapi kerjaannya makin hari makin banyak."
-->

---

<div class="eyebrow">// 📖 Cerita</div>

## Senin pagi Raka

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2">

<div class="stack" style="gap: 10px">
  <div class="flowrow"><span class="tag paham">07.00</span> Download 3 file kasir</div>
  <div class="flowrow"><span class="tag paham">07.15</span> Gabung di Excel</div>
  <div class="flowrow"><span class="tag paham">07.25</span> Benerin nama menu</div>
  <div class="flowrow"><span class="tag paham">07.40</span> Hitung & cek target</div>
  <div class="flowrow"><span class="tag paham">07.55</span> Ketik laporan di WA</div>
  <div class="flowrow"><span class="tag wajib">08.05</span> <b>Besok ulang lagi 😮‍💨</b></div>
</div>

<div>

```text
"  es kopi SUSU gula aren "
"ES KOPI SUSU GULA AREN"
"Es Kopi susu Gula Aren   "
```

<div class="mt-6 huge" style="font-size: 3rem"><span class="hl">65 menit</span></div>
<div class="muted mono">setiap hari</div>
</div>

</div>

<!--
⏱️ 1 menit

Rutinitas Raka tiap pagi:
1. Download 3 file penjualan dari aplikasi kasir tiap cabang
2. Gabungin di Excel
3. Benerin nama menu yang ditulis beda-beda tiap kasir (lihat kotak kanan)
4. Hitung total, rata-rata, cek target
5. Ketik ulang laporan di WhatsApp ke Bu Sari

"Ini terjadi setiap hari kerja." Nama menu yang berantakan akan jadi masalah di Bab 6.
-->

---

<div class="eyebrow">// 📖 Sampai suatu hari...</div>

## Satu nol nyelip

<div class="chat mt-8" style="max-width: 720px; margin-left: auto; margin-right: auto">
  <div class="bubble me"><small>RAKA · 08.04</small>Omzet Jakarta kemarin <b>Rp12.500.000</b> Bu 🙏</div>
  <div class="bubble them"><small>BU SARI · 08.05</small>WAH 😍 ...kok 10x lipat? 😨</div>
  <div v-click class="bubble me"><small>RAKA · 08.11</small>Maaf Bu, harusnya <b>Rp1.250.000</b> 🙇</div>
</div>

<!--
⏱️ 30 detik

"Satu nol nyelip. Capek, ngantuk, manusiawi. Tapi Bu Sari jadi nggak percaya lagi sama laporan."
-->

---
mode: colab-demo
where: 00 · Demo Final
---

<div class="eyebrow">// Misi hari ini</div>

# Gimana kalau cuma <span class="hl" style="white-space: nowrap">1 detik</span>?

<div class="grid grid-cols-[1fr_1.15fr] gap-10 mt-6 items-center">
  <div class="stack">
    <div class="point">Kalian yang bikin 💪</div>
    <div class="mt-4"><Goto to="colab" where="Materi · 00 · Demo Final" /></div>
  </div>

<div class="code-xs">

```text
============================================
         LAPORAN HARIAN KOPI SENJA
============================================
Tanggal          : 05-10-2026
Analis           : Raka Pratama
--------------------------------------------
Total omzet      : Rp10.645.000
Rata-rata/trx    : Rp23.396
Menu terlaris    : Es Kopi Susu Gula Aren
Capaian          : 106.45%
Target tercapai? : True
============================================
```

</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 PINDAH KE COLAB → notebook 01_materi_kopi_senja, section "00 · Demo Final"

1. Jalankan cell, isi nama & tanggal saat diminta input.
2. Biarkan output laporan tampil penuh. Scroll cepat: kodenya "cuma" ±50 baris.
3. "Di akhir kelas, KALIAN sendiri yang bikin script laporan otomatis ini. Semua materi hari ini = potongan puzzle untuk script itu."
4. Jangan jelaskan kodenya sekarang. Tujuannya bikin penasaran.

➡️ Balik ke slide 7.
-->

---

<div class="eyebrow">// Peta perjalanan</div>

## 8 bab · 8 stempel · 1 kopi gratis

<div class="grid grid-cols-[1.55fr_1fr] gap-8 mt-4">
  <StampCard :done="0" />
  <div class="card pop">
    <div class="box-h">Aturan main</div>
    <ul class="bullets">
      <li>Error itu wajar</li>
      <li>Tanya kapan saja</li>
      <li>🟢 aman · 🔴 stuck</li>
      <li>Ketik sendiri</li>
    </ul>
  </div>
</div>

<!--
⏱️ 1 menit

- Tujuan versi peserta: "Hari ini kalian akan kenalan sama Python, nulis & jalanin kode sendiri, dan bikin laporan otomatis buat Kopi Senja."
- "Setiap selesai satu bab, kita cap satu stempel. 8 stempel = kopi gratis: laporan otomatis."
- Aturan main: error itu wajar (programmer senior pun kena tiap hari), tanya kapan saja, sinyal 🟢/🔴, ketik sendiri jangan copy-paste.
- Footer: kotak kecil di tengah = progres stempel, label kanan = kita lagi di mana (Colab/VSCode/Hands-on).
-->

---
section: Bab 1 · Kenapa Raka Harus Ngoding?
bab: 1
---

<div class="ghostnum">01</div>
<div class="eyebrow">// Bab 1 · Kenapa Raka harus ngoding?</div>

## Data datang dari mana-mana

<div class="flowrow mt-8" style="gap: 18px">
  <div class="stack" style="flex: 1">
    <div class="node"><div class="t">🧾 Kasir 3 cabang</div></div>
    <div class="node"><div class="t">🛵 Ojol</div></div>
    <div class="node"><div class="t">📦 Stok gudang</div></div>
    <div class="node"><div class="t">💳 Mutasi bank</div></div>
  </div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="node yl" style="flex: 0.7; text-align:center; padding: 24px 14px">
    <div style="font-size: 3rem">🧑‍💻</div>
    <div class="t" style="font-size: 1.2rem">Raka</div>
  </div>
  <div class="card pop" style="flex: 1.3">
    <div class="huge" style="font-size: 2.4rem">Bukan cuma 1 file Excel.</div>
  </div>
</div>

<!--
⏱️ 00:07 · 2 menit

"Excel itu alat yang bagus. Masalahnya, data di dunia nyata datang dari banyak tempat (kasir, aplikasi ojol, stok gudang, mutasi bank), tiap hari, dengan format beda-beda. Excel nggak didesain buat kerja ulang yang sama tiap pagi."

Tanya: "Di kerjaan/kampus kalian, data datang dari mana aja?" (1–2 jawaban saja)
-->

---

<div class="eyebrow">// Bab 1</div>

## 3 musuh kerja manual

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="card pop"><div class="icon">🔁</div><div class="point mt-3">Repetitif</div></div>
  <div class="card pop"><div class="icon">😴</div><div class="point mt-3">Membosankan</div></div>
  <div class="card err"><div class="icon">⚠️</div><div class="point mt-3" style="color: var(--err)">Rawan salah</div></div>
</div>

<div class="card mt-8 flowrow" style="gap: 24px">
  <div class="mono" style="font-size: 1.3rem"><b>65</b> menit × <b>22</b> hari =</div>
  <div v-click class="huge" style="font-size: 2.6rem"><span class="hl">±24 jam/bulan</span></div>
</div>

<!--
⏱️ 2,5 menit

- Repetitif: kerjaan sama, tiap hari. Membosankan: bikin lengah. Rawan salah: typo, rumus ketimpa, angka bisa diubah tanpa jejak.
- Minta peserta hitung dulu sebelum klik: 65 × 22 = 1.430 menit ≈ 24 jam ≈ 3 hari kerja penuh tiap bulan, cuma buat copy-paste.
- "Yang paling bahaya bukan capeknya, tapi SALAHNYA. Proses manual juga susah diaudit: kalau ada angka berubah, siapa yang ngubah? Kapan?"
- Di outline tertulis "Fradulent": dibingkai sebagai rawan salah & rawan manipulasi (tidak ada jejak).
-->

---

<div class="eyebrow">// Bab 1</div>

## Kode itu <span class="hl">resep</span>

<div class="grid grid-cols-[1fr_auto_1fr] gap-6 mt-6 items-center">
  <div class="card"><div class="box-h">Manual</div><div class="huge" style="font-size:3.2rem">65 menit</div></div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="card tk"><div class="box-h">Script</div><div class="huge" style="font-size:3.2rem">1 detik</div></div>
</div>

<div class="mt-6 point">Tulis sekali, jalan berkali-kali.</div>

<div class="mt-5"><StampCard :done="1" :stamping="1" compact /></div>

<!--
⏱️ 1,5 menit · 🎟️ STEMPEL 1

"Kode itu kayak resep. Ditulis sekali, bisa dimasak berkali-kali, rasanya selalu sama. Otomasi, repetitif → konsisten. Kalau Raka nulis resep laporannya dalam bentuk kode, besok pagi tinggal 'masak' ulang."

➡️ "Oke, Raka mau ngoding. Tapi pakai BAHASA apa?"
-->

---
section: Bab 2 · Kenalan sama Python
bab: 2
---

<div class="ghostnum">02</div>
<div class="eyebrow">// Bab 2 · Kenalan sama Python</div>

## Low level vs high level

<div class="flowrow mt-4" style="gap: 8px">
  <div class="node"><div class="t">0101</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">Assembly</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">C</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">Java, PHP</div></div>
  <div class="arw">›</div>
  <div class="node tk"><div class="t">Python</div></div>
</div>
<div class="flex justify-between mono small mt-2" style="max-width: 640px"><span>◀ dekat ke mesin</span><span>dekat ke manusia ▶</span></div>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="card">
    <div class="box-h">☕ Low level</div>
    <div class="muted">"Giling 18 g, tamper 15 kg, 9 bar, 25 detik..."</div>
  </div>
  <div class="card pop">
    <div class="box-h">☕ High level</div>
    <div class="point">"Es kopi susu satu."</div>
  </div>
</div>

<!--
⏱️ 00:13 · 1,5 menit

"Bayangin kalian pesan kopi. Low level: 'Ambil 18 gram biji, giling ukuran 3, tekan tamper 15 kg, seduh 9 bar selama 25 detik, tuang susu 150 ml...' High level: 'Mas, es kopi susu satu, gulanya dikit ya.' Hasilnya sama-sama kopi. Bedanya: siapa yang mikirin detailnya. Di bahasa high level, detail ribetnya diurus oleh bahasanya."
-->

---

<div class="eyebrow">// Bab 2</div>

## Python: satu baris

<div class="grid grid-cols-2 gap-x-6 gap-y-1 code-sm">
<div>
<div class="box-h">Assembly</div>

```text
mov edx, len
mov ecx, msg
mov ebx, 1
mov eax, 4
int 0x80
```

<div class="box-h mt-3">Java</div>

```java
public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, Kopi Senja!");
    }
}
```

</div>
<div>
<div class="box-h">Python</div>
<div class="code-lg code-yl">

```python
print("Halo, Kopi Senja!")
```

</div>
<div class="point mt-8">Simple syntax ✨</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Semua kode ini sama-sama menulis 'Halo, Kopi Senja!'. Java juga high level, tapi lihat bedanya. Python satu baris. Itu yang dimaksud simple syntax."
-->

---

<div class="eyebrow">// Bab 2</div>

## Gampang dibaca

<div class="grid grid-cols-[1.25fr_1fr] gap-8 mt-2 items-start">
<div>

```python
menu_tersedia = ["kopi susu", "latte"]
pesanan = "latte"

if pesanan in menu_tersedia:
    print("Siap, pesanan dibuat!")
else:
    print("Maaf, menu habis.")
```

</div>
<div class="stack">
  <div class="card pop-yl"><div class="point sm">Tebak: ini ngapain? 🤔</div></div>
  <div v-click class="card tk"><div class="point sm">"Readability counts"</div></div>
</div>
</div>

<!--
⏱️ 1,5 menit

- "Kalian BELUM belajar Python sama sekali. Tapi coba tebak: program ini ngapain?" Tunggu 2–3 jawaban, baru klik.
- "Bisa nebak, kan? Python didesain dengan prinsip readability: kode harus gampang dibaca manusia. 'Readability counts' adalah salah satu prinsip resmi Python (Zen of Python, `import this`)."
- `if` sengaja dipakai sebagai teaser (pertemuan berikutnya). Jangan jelaskan sintaksnya.
-->

---

<div class="eyebrow">// Bab 2 <span class="tag paham">paham</span></div>

## Interpreted vs compiled

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="card pop">
    <div class="box-h">Interpreted · Python</div>
    <div class="icon mt-2">☕</div>
    <div class="point mt-3">Barista: baris per baris</div>
    <ul class="mt-4">
      <li>✅ cepat dicoba</li>
      <li>⚠️ jalan lebih lambat</li>
    </ul>
  </div>
  <div class="card">
    <div class="box-h">Compiled · C, Java</div>
    <div class="icon mt-2">🥫</div>
    <div class="point mt-3">Pabrik kaleng: bungkus dulu</div>
    <ul class="mt-4">
      <li>✅ jalan lebih cepat</li>
      <li>⚠️ compile ulang tiap ubah</li>
    </ul>
  </div>
</div>

<!--
⏱️ 2 menit

- Interpreted: dibaca & dijalankan baris per baris. Error ketahuan saat baris itu dijalankan, baris sebelumnya sudah jalan.
- Compiled: seluruh kode "dibungkus" jadi bahasa mesin dulu. Error ketahuan sebelum program jalan.
- "Barista baca resep langkah demi langkah. Kalau di langkah ke-3 susunya habis, langkah 1 & 2 udah terjadi. Pabrik kopi kaleng: resep diproses semua dulu. Kalau salah, ketahuan sebelum produksi, tapi tiap ganti resep harus produksi ulang."

Kalau ada yang kritis:
- CPython juga mengompilasi ke bytecode dulu, tetap dikategorikan interpreted.
- Java/C# dikompilasi ke bytecode lalu dijalankan VM.
- SyntaxError dicek di awal (seluruh cell tidak jalan). Yang berhenti di tengah = error runtime seperti NameError. Karena itu demo berikutnya pakai NameError.
-->

---
mode: colab-demo
where: Materi · Bab 3
---

<div class="eyebrow">// Bab 2 · Demo</div>

## Barista baca resep

<div class="grid grid-cols-[1.25fr_1fr] gap-8 mt-2 items-start">
<Predict :options="['0 baris', '2 baris', '4 baris']" :answer="1">

```python
print("1. Download Jakarta... beres")
print("2. Download Bandung... beres")
prnt("3. Download Surabaya...")
print("4. Kirim laporan")
```

</Predict>
<div class="stack">
  <Goto to="colab" where="Materi · Bab 3" />
  <div v-click="2" class="code-sm code-err">

```text
1. Download Jakarta... beres
2. Download Bandung... beres
NameError: name 'prnt' ...
```

  </div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 3 · Halo Kopi Senja" (peserta nonton saja)

- "Ada typo di baris 3. Berapa baris yang tercetak?" Tanya tebakan dulu, klik untuk reveal, lalu jalankan di Colab.
- "Baris 1–2 jalan, baris 3 error, baris 4 nggak pernah dijalankan. Persis barista tadi."
- Jangan bahas cara baca error dulu: itu di slide 23 saat peserta mengalaminya sendiri.
-->

---

<div class="eyebrow">// Bab 2 <span class="tag kenalan">kenalan</span></div>

## Satu bahasa, banyak dapur

<div class="grid grid-cols-5 gap-4 mt-6">
  <div class="card pop"><div class="icon">📊</div><h3 class="mt-3">Data</h3><span class="small">pandas</span></div>
  <div class="card"><div class="icon">🤖</div><h3 class="mt-3">AI</h3><span class="small">PyTorch</span></div>
  <div class="card"><div class="icon">🌐</div><h3 class="mt-3">Web</h3><span class="small">Django</span></div>
  <div class="card"><div class="icon">🎮</div><h3 class="mt-3">Game</h3><span class="small">pygame</span></div>
  <div class="card pop-yl"><div class="icon">⚙️</div><h3 class="mt-3">Otomasi</h3><span class="small">openpyxl</span></div>
</div>

<div class="point mt-10">Library = bahan setengah jadi 🍯</div>

<!--
⏱️ 1 menit

- General purpose: data (pandas, numpy, matplotlib), AI/ML (scikit-learn, PyTorch), web (Django, Flask, FastAPI), game (pygame), otomasi (openpyxl untuk Excel, requests).
- "Library itu kayak bahan setengah jadi. Kopi Senja nggak bikin sirup gula aren dari tebu, tinggal beli yang udah jadi. Mau baca Excel nggak perlu bikin dari nol. Raka nanti pakai pandas buat baca file kasir (pertemuan berikutnya)."
-->

---

<div class="eyebrow">// Bab 2</div>

## Kenapa Python?

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="card pop"><div class="icon">🆓</div><div class="point sm mt-3">Gratis & open source</div></div>
  <div class="card pop"><div class="icon">👥</div><div class="point sm mt-3">Komunitas besar</div></div>
  <div class="card pop"><div class="icon">🏆</div><div class="point sm mt-3">#1 di dunia data</div></div>
</div>

<div class="mt-8"><StampCard :done="2" :stamping="2" compact /></div>

<!--
⏱️ 1 menit · 🎟️ STEMPEL 2

- Komunitas di Indonesia: PythonID (Telegram/FB) dan PyCon ID tiap tahun.
- "Komunitas besar artinya kalau kalian error, 99% kemungkinan sudah ada orang lain yang pernah kena dan nanya duluan di internet."
- Ringkasan bab: Python = bahasa high-level, mudah dibaca, interpreted, serbaguna, gratis, dan jagoan di dunia data.
- Kalau mau sebut angka peringkat, cek data terbaru (TIOBE / IEEE Spectrum / Stack Overflow Survey).

➡️ "Bahasanya udah kepilih. Sekarang, Raka ngodingnya DI MANA?"
-->

---
section: Bab 3 · Nyiapin Meja Kerja
bab: 3
---

<div class="ghostnum">03</div>
<div class="eyebrow">// Bab 3 · Nyiapin meja kerja</div>

## Dev environment = dapur

<div class="grid grid-cols-2 gap-8 mt-10">
  <div class="card">
    <div class="box-h">🌐 Bikin web</div>
    <div class="huge" style="font-size: 1.8rem">VSCode · Cursor · PhpStorm</div>
  </div>
  <div class="card pop">
    <div class="box-h">📊 Ngolah data</div>
    <div class="huge" style="font-size: 1.8rem">VSCode · Cursor · <span class="hl">Notebook</span></div>
  </div>
</div>

<!--
⏱️ 00:23 · 1,5 menit

"Development environment = tempat kita menulis, menjalankan, dan mengembangkan aplikasi. Barista butuh dapur, programmer butuh dev environment. Dan dapurnya tergantung mau masak apa."
-->

---

<div class="eyebrow">// Bab 3</div>

## Isi dapur Python

<div class="grid grid-cols-4 gap-5 mt-6">
  <div class="card pop"><div class="icon">☕</div><h3 class="mt-3">Interpreter</h3><div class="small">yang menjalankan</div><div class="mt-3"><span class="tag paham">paham</span></div></div>
  <div class="card pop"><div class="icon">📒</div><h3 class="mt-3">Editor</h3><div class="small">tempat nulis</div><div class="mt-3"><span class="tag paham">paham</span></div></div>
  <div class="card"><div class="icon">🚚</div><h3 class="mt-3">pip · uv</h3><div class="small">install library</div><div class="mt-3"><span class="tag kenalan">kenalan</span></div></div>
  <div class="card"><div class="icon">🍳</div><h3 class="mt-3">Virtual env</h3><div class="small">dapur per proyek</div><div class="mt-3"><span class="tag kenalan">kenalan</span></div></div>
</div>

<div class="point mt-10">Di Colab: semua sudah siap ✅</div>

<!--
⏱️ 2 menit

- Interpreter = barista / mesin kopi: yang benar-benar menjalankan kode.
- Code editor = meja racik + buku resep: tempat menulis kode.
- Package manager (pip, uv) = supplier bahan: download & install library.
- Virtual environment = dapur terpisah per menu: ruang terpisah per proyek, biar versi library nggak bentrok.

"Hari ini cukup ingat dua yang pertama. Kabar baiknya: di Google Colab, semuanya udah disiapin."
-->

---

<div class="eyebrow">// Bab 3</div>

## 3 gaya dapur

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="card"><h3>Editor + terminal</h3><div class="point sm mt-3">Dapur minimalis</div><div class="small muted mt-2">Notepad++</div></div>
  <div class="card"><h3>IDE</h3><div class="point sm mt-3">Dapur lengkap</div><div class="small muted mt-2">VSCode · PyCharm</div></div>
  <div class="card pop-yl"><h3>Notebook</h3><div class="point sm mt-3">Test kitchen 🧪</div><div class="small muted mt-2">Colab · Jupyter</div></div>
</div>

<div class="point mt-10">Notebook = kode per <span class="hl">cell</span>, langsung lihat hasil.</div>

<!--
⏱️ 2 menit

- Text editor + terminal (Notepad++): dapur minimalis, cocok script kecil & server.
- IDE (VSCode, PyCharm): dapur produksi lengkap, cocok aplikasi & script yang dipakai rutin.
- Notebook (Jupyter, Google Colab, Marimo): test kitchen, cocok belajar, eksplorasi & analisis data.

"Notebook itu kayak dapur uji coba: kodenya dipotong-potong per cell, tiap cell bisa dijalankan dan langsung kelihatan hasilnya."
-->

---

<div class="eyebrow">// Bab 3</div>

## Hari ini pakai yang mana?

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="card pop" style="padding: 22px">
    <div class="icon">🧪</div>
    <div class="huge mt-3" style="font-size: 2.4rem">Colab</div>
    <div class="point sm mt-2">Belajar & coba-coba</div>
    <span class="sticker tk mt-4">sepanjang kelas</span>
  </div>
  <div class="card" style="padding: 22px">
    <div class="icon">💻</div>
    <div class="huge mt-3" style="font-size: 2.4rem">VSCode</div>
    <div class="point sm mt-2">Script tiap pagi</div>
    <span class="sticker r mt-4">tujuan akhir</span>
  </div>
</div>

<div class="mt-8"><Goto to="hands-on" where="Hands-on 1 · Halo, Kopi Senja!" /></div>

<!--
⏱️ 1,5 menit

"Colab = tempat belajar & coba-coba, nggak perlu install apa pun. VSCode = tempat script 'beneran' yang dijalankan rutin tiap pagi. Sepanjang kelas kita pakai Colab. Di akhir kelas, kita pindahin hasilnya ke VSCode."

Kenapa semua pakai Colab: nol instalasi = nol waktu terbuang buat troubleshooting setup; beban kognitif fokus ke Python, bukan tools.

➡️ "Saatnya pegang kode!"
-->

---
mode: hands-on
where: Latihan · Bab 3
---

<div class="eyebrow">// Hands-on 1</div>

## Halo, Kopi Senja!

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2">
<div>
<ol class="bullets">
  <li>Buka link → <b>Save a copy in Drive</b></li>
  <li>Rename: <code>KopiSenja_Nama</code></li>
  <li>Section <b>Bab 3</b></li>
  <li>Ketik → <span class="kbd">Shift</span> + <span class="kbd">Enter</span></li>
  <li>Sinyal 🟢 / 🔴</li>
</ol>
</div>
<div class="stack">
  <Goto to="hands-on" where="Buka notebook latihan" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
  <div class="code-lg">

```python
print("Halo, Kopi Senja!")
```

  </div>
</div>
</div>

<!--
⏱️ 00:30 · 6 menit · 🎯 HANDS-ON (share screen Colab, kerjakan bareng langkah demi langkah)

Langkah lengkap:
1. Buka link notebook latihan (tombol di slide / chat) → File → Save a copy in Drive
2. Ganti nama: KopiSenja_NamaKamu
3. Scroll ke section "Bab 3 · Halo Kopi Senja"
4. Klik + Code, ketik print("Halo, Kopi Senja!"), tekan Shift + Enter
5. Ganti tulisannya jadi nama sendiri, jalankan lagi
6. Klik + Text, tulis "Catatan kelas Python pertamaku ☕"
7. Sinyal 🟢 berhasil / 🔴 stuck

Tunjukkan: kotak abu-abu = cell (code cell & text cell). Angka [1] di kiri = urutan cell dijalankan. Run pertama agak lama karena Colab lagi nyiapin runtime.

- Lupa kutip → NameError; kurung tidak ditutup → SyntaxError. Bagus! Pakai sebagai bahan slide 23.
- Bonus buat yang cepat: `import this`.
-->

---
mode: hands-on
where: Latihan · Bab 3
---

<div class="eyebrow">// Hands-on 1</div>

## Cara baca error

<div class="grid grid-cols-[1.15fr_1fr] gap-8 mt-2">
<div class="code-sm code-err">

```text
NameError       Traceback (most recent call last)
Cell In[2], line 3
      1 print("1. Download Jakarta... beres")
      2 print("2. Download Bandung... beres")
----> 3 prnt("3. Download Surabaya...")

NameError: name 'prnt' is not defined
```

</div>
<div class="stack">
  <div class="card pop flowrow"><span class="num" style="font-size:1.8rem">1</span><b>Baca baris paling bawah</b></div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.8rem">2</span><b>Cari nomor baris</b></div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.8rem">3</span><b>Cek typo · kutip · kurung</b></div>
  <div class="card yl"><b>📕 NameError</b> = nama tidak dikenal</div>
</div>
</div>

<!--
⏱️ 2,5 menit

Peserta jalankan cell "Tebak dulu, baru jalankan" di notebook latihan. Tebak dulu berapa baris yang tercetak.

3 langkah baca error:
1. Baca baris paling bawah dulu: jenis error + pesannya
2. Cari nomor baris / tanda panah di kiri kode
3. Bandingkan dengan maksudmu: typo? lupa kutip? kurung belum ditutup?

"Pesan error itu bukan marah-marah, tapi PETUNJUK. Python sering bahkan kasih saran, misalnya 'Did you mean: print?'."

Mulai papan "Kamus Error": NameError = "Aku nggak kenal nama ini" (typo, lupa kutip, atau cell belum dijalankan).
-->

---
mode: vscode
where: kopi-senja/laporan.py
---

<div class="eyebrow">// Hands-on 1 · Demo</div>

## Dapur produksi: VSCode

<div class="grid grid-cols-[1fr_1fr] gap-8 mt-2">
<div>
<ol class="bullets">
  <li>Open Folder <code>kopi-senja</code></li>
  <li>File <code>laporan.py</code></li>
  <li>Save → ▶ Run</li>
</ol>

```bash
python3 laporan.py
```

</div>
<div class="stack">
  <Goto to="vscode" where="demo trainer" />
  <div class="card pop-yl"><div class="point sm"><code>.py</code> = resep tersimpan</div></div>
  <div class="sticker tk" style="align-self: flex-start">balik lagi di akhir kelas</div>
</div>
</div>

<!--
⏱️ 2,5 menit · 💻 PINDAH KE VSCODE (peserta yang sudah install boleh ikut)

1. File → Open Folder → kopi-senja
2. File baru: laporan.py, ketik print("Halo, Kopi Senja!"), simpan (Cmd/Ctrl + S)
3. Klik ▶ Run Python File, atau terminal: python3 laporan.py (Mac/Linux) / python laporan.py (Windows)

"Bedanya sama Colab: ini FILE .py, resep yang tersimpan rapi. Bisa dijalankan kapan saja tanpa browser, bahkan dijadwalkan tiap jam 7 pagi. Kita balik ke sini di akhir kelas."

- Tombol ▶ tidak muncul → cek extension Python & interpreter terpilih (pojok kanan bawah).
- Peserta yang belum install: kirim panduan setup untuk dikerjakan di rumah.
-->

---

<div class="eyebrow">// Hands-on 1</div>

## Colab vs VSCode

<table>
  <thead><tr><th></th><th>🧪 Colab</th><th>💻 VSCode</th></tr></thead>
  <tbody>
    <tr><td><b>Analogi</b></td><td>Test kitchen</td><td>Dapur produksi</td></tr>
    <tr><td><b>Jalan</b></td><td>Per cell</td><td>Satu file</td></tr>
    <tr><td><b>Buat</b></td><td>Belajar, eksplorasi</td><td>Script rutin</td></tr>
  </tbody>
</table>

<div class="card pop-yl mt-6"><b>💡 Error "nggak dikenal"?</b> → Runtime → Run all</div>

<div class="mt-5"><StampCard :done="3" :stamping="3" compact /></div>

<!--
⏱️ 1 menit · 🎟️ STEMPEL 3

Tips notebook: kalau Colab bilang variabel nggak dikenal padahal sudah ditulis, biasanya cell-nya belum di-run. Solusi pamungkas: Runtime → Run all.

➡️ "Meja kerja siap. Sekarang Raka mulai nulis resep laporannya. Mulai sekarang kita di COLAB terus."
-->

---
section: Bab 4 · Toples Berlabel
bab: 4
mode: colab-demo
where: Materi · Bab 4
---

<div class="ghostnum">04</div>
<div class="eyebrow">// Bab 4 · Toples berlabel <span class="tag wajib">wajib</span></div>

## Komentar: catatan untuk manusia

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-start">
<div>

```python
# Laporan harian Kopi Senja
print("Laporan dimulai")  # catatan
# print("nggak dijalankan")
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm"><code>#</code> = dilewati Python</div></div>
  <div class="card soft"><span class="kbd">Cmd</span> / <span class="kbd">Ctrl</span> + <span class="kbd">/</span></div>
</div>
</div>

<!--
⏱️ 00:42 · 1,5 menit · 🧪 COLAB → materi, section "Bab 4 · Toples Berlabel"

- Ketik live, jangan paste.
- Komentar dipakai untuk (1) menjelaskan KENAPA kode ditulis begitu, dan (2) "mematikan" kode sementara tanpa menghapusnya.
- Shortcut Cmd + / (Mac) atau Ctrl + / (Windows) untuk toggle komentar.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Function = mesin kopi

<div class="flowrow mt-4" style="gap: 14px">
  <div class="node"><div class="t">"Halo"</div><div class="s">argumen</div></div>
  <div class="arw">➜</div>
  <div class="node tk" style="padding: 14px 22px"><div class="t" style="font-size:1.3rem">☕ print( )</div><div class="s">function</div></div>
  <div class="arw">➜</div>
  <div class="node"><div class="t">Halo</div><div class="s">hasil</div></div>
</div>

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-start">
<div>

```python
print("Laporan Kopi Senja")
print(3)
print("Jumlah cabang:", 3)
print(Kopi)   # ❌ ?
```

</div>
<div class="stack">
  <div class="card pop-yl"><div class="point sm">Baris terakhir? 🤔</div></div>
  <div v-click class="card yl"><b>NameError</b>: lupa tanda kutip</div>
</div>
</div>

<!--
⏱️ 1,5 menit

- Function = mesin kopi: bahan masuk (argumen) dalam kurung ( ) → mesin bekerja → hasil keluar.
- Built-in function = mesin bawaan Python: print, type, len, max, round, input...
- print() bisa banyak nilai dipisah koma; print() kosong = baris kosong.
- "Teks pakai tanda kutip, angka tidak. Tanpa kutip, Python mengira Kopi itu nama sesuatu, dan dia nggak kenal → NameError, teman lama kita."
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Variabel = toples berlabel

<div class="grid grid-cols-[1.25fr_1fr] gap-8 items-start">
<div>
  <div class="flex gap-5 mt-1">
    <Jar label="nama_toko" value='"Kopi Senja"' type="str" />
    <Jar label="jumlah_cabang" value="3" type="int" accent="yl" />
    <Jar label="omzet_jakarta" value="4250000" type="int" />
  </div>
  <div class="card pop mt-6"><div class="point sm"><span class="hl">=</span> artinya MASUKKAN KE</div></div>
</div>
<Predict :options="['10', '12', 'Error']" :answer="1">

```python
stok_cup = 10
stok_cup = stok_cup - 3
stok_cup = stok_cup + 5
print(stok_cup)
```

</Predict>
</div>

<!--
⏱️ 2 menit

"Di Excel, Raka nyimpen omzet di sel B2, rumusnya =B2+B3. Masalahnya, B2 itu apa? Di Python, kita kasih NAMA yang bermakna."

Ketik di Colab: nama_toko = "Kopi Senja", jumlah_cabang = 3, omzet_jakarta = 4250000, lalu print.

"= artinya MASUKKAN KE, bukan SAMA DENGAN. Baca dari kanan ke kiri."
Tebak output → 12. "Di matematika x = x + 1 itu mustahil. Di Python normal: ambil isi toples, tambah 1, masukin lagi."

Miskonsepsi `=` sebagai "sama dengan" sangat umum. Tekankan sekarang karena di Bab 5 muncul `==`.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Isi toples bisa diganti

<div class="grid grid-cols-2 gap-8 mt-4">
<div>
<div class="box-h">Java: tipe dikunci</div>

```java
int omzet = 4250000;
omzet = "empat juta"; // ❌
```

<div class="box-h mt-5">Python: tipe ditebak</div>

```python
omzet = 4250000
print(type(omzet))  # int

omzet = "empat juta"
print(type(omzet))  # str
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm">Nama sama → isi lama hilang</div></div>
  <div class="card pop"><div class="point sm"><code>type()</code> = cek jenis isi</div></div>
</div>
</div>

<!--
⏱️ 1,5 menit

- "Kalau kita isi ulang toples dengan nama yang sama, isi lama hilang. Boleh, tapi hati-hati."
- Dynamic typing: Python menebak tipe data dari isinya. Fleksibel, tapi sebaiknya jangan ganti-ganti tipe di satu variabel (bikin bingung).
- Java: tipe ditulis & dikunci, ganti tipe = error saat compile.
- type() = built-in function buat ngecek isi toples itu jenisnya apa. Output lengkapnya: <class 'int'>.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Aturan kasih nama

<table>
  <thead><tr><th>❌ Salah</th><th>✅ Benar</th><th>Kenapa</th></tr></thead>
  <tbody>
    <tr><td><code>2cabang</code></td><td><code>cabang2</code></td><td>diawali angka</td></tr>
    <tr><td><code>omzet bandung</code></td><td><code>omzet_bandung</code></td><td>pakai spasi</td></tr>
    <tr><td><code>omzet-surabaya</code></td><td><code>omzet_surabaya</code></td><td>tanda <code>-</code></td></tr>
    <tr><td><code>class</code></td><td><code>kelas</code></td><td>keyword</td></tr>
    <tr><td><code>Total</code> ≠ <code>total</code></td><td>konsisten</td><td>case sensitive</td></tr>
  </tbody>
</table>

<div class="card yl mt-6"><b>📕 SyntaxError</b> = tata bahasa salah</div>

<!--
⏱️ 1,5 menit

Error yang muncul:
- `2cabang = 3` → SyntaxError: invalid decimal literal
- `omzet bandung = 875000` → SyntaxError: invalid syntax
- `omzet-surabaya = 3520000` → SyntaxError: cannot assign to expression here (tanda - dibaca sebagai PENGURANGAN)
- `class = "A"` → SyntaxError: invalid syntax (keyword = kata yang sudah "dipesan" Python: if, for, class, True...)
- `Total` vs `total` → NameError kalau salah huruf

Demo daftar keyword: `import keyword; print(keyword.kwlist)`.

Kamus Error #2: SyntaxError = "Tata bahasanya salah." Python menolak menjalankan cell sama sekali.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Jangan pakai nama bawaan

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
max = 4250000
print(max(3, 7, 5))
# ❌ TypeError
```

</div>
<div>

```python
del max
print(max(3, 7, 5))  # ✅ 7
```

</div>
</div>

<div class="card pop-yl mt-6"><div class="point sm">Hindari: <code>max</code> <code>min</code> <code>sum</code> <code>list</code> <code>str</code> <code>print</code></div></div>

<!--
⏱️ 1,5 menit

Cerita: "Raka pernah bikin variabel max buat nyimpen omzet tertinggi. 10 menit kemudian, max(...) error."

- Error lengkap: TypeError: 'int' object is not callable.
- "Nama function bawaan BUKAN keyword, jadi Python mengizinkan. Tapi mesin max aslinya ketimpa angka. Toples dikasih label 'mesin kopi', mesinnya jadi hilang."
- "del dipakai menghapus variabel. Setelah dihapus, kalau dipanggil lagi → NameError."
- Tips: kalau nama variabel berubah warna di editor (kayak print), itu nama bawaan, ganti namanya.
-->

---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Konvensi PEP 8

<table>
  <thead><tr><th>Jenis</th><th>Gaya</th><th>Contoh</th></tr></thead>
  <tbody>
    <tr><td>Variabel</td><td><code>snake_case</code></td><td><code>omzet_jakarta</code></td></tr>
    <tr><td>Konstanta</td><td><code>UPPER_CASE</code></td><td><code>TARGET_HARIAN</code></td></tr>
    <tr><td>Class (nanti)</td><td><code>PascalCase</code></td><td><code>LaporanHarian</code></td></tr>
  </tbody>
</table>

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="card err"><div class="box-h" style="color: var(--err)">❌ Jelek</div><code>x</code> <code>a1</code> <code>data2</code></div>
  <div class="card pop"><div class="box-h">✅ Bagus</div><code>omzet_jakarta</code></div>
</div>

<!--
⏱️ 1 menit

- Aturan (slide sebelumnya) = WAJIB: dilanggar → error.
- Konvensi = KESEPAKATAN komunitas (PEP 8): nggak error, tapi bikin kode gampang dibaca orang lain, termasuk diri kalian sendiri 3 bulan lagi.
- "Kode itu lebih sering dibaca daripada ditulis. Nama variabel yang baik = dokumentasi gratis."
-->

---
mode: hands-on
where: Latihan · Bab 4
---

<div class="eyebrow">// Bab 4 · Latihan</div>

## 🎯 Latihan Bab 4

<div class="grid grid-cols-[1.1fr_1fr] gap-8">
<div>
<ol class="bullets" style="font-size: 0.9em">
  <li>Variabel toko, nama, cabang</li>
  <li>Omzet & transaksi 3 cabang</li>
  <li>Konstanta <code>TARGET_HARIAN</code></li>
  <li><code>print()</code> + <code>type()</code></li>
</ol>
</div>
<div>
<div class="box-h">🕵️ Error atau tidak?</div>
<div class="code-sm">

```python
cabang_1 = "Jakarta"
1_cabang = "Bandung"
cabang surabaya = "Surabaya"
_catatan = "rahasia"
Omzet = 100
print(omzet)
```

</div>
<div v-click class="answer small mt-1">❌ baris 2, 3, 6</div>
</div>
</div>

<div class="mt-4"><StampCard :done="4" :stamping="4" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 4 · Toples Berlabel" · 🎟️ STEMPEL 4

Soal lengkap:
1. Buat variabel: nama toko, namamu (sebagai analis), jumlah cabang
2. Omzet & transaksi: JKT 4250000 / 170 · BDG 2875000 / 125 · SBY 3520000 / 160
3. Konstanta target harian: 10000000
4. Print semuanya, cek tipenya pakai type()

Pojok Error: baris 2 (diawali angka) & 3 (spasi) → SyntaxError; baris 6 → NameError (case sensitive). Baris 1, 4, 5 valid.
Di notebook latihan, Pojok Error sudah dipisah satu cell per baris: tebak dulu, baru jalankan satu per satu.

➡️ "Angka-angka udah masuk toples. Sekarang saatnya NGITUNG."
-->

---
section: Bab 5 · Ngitung Omzet
bab: 5
---

<div class="ghostnum">05</div>
<div class="eyebrow">// Bab 5 · Ngitung omzet</div>

## Peta tipe data

<table class="dense">
  <thead><tr><th>Tipe</th><th>Contoh</th><th>Bab</th></tr></thead>
  <tbody>
    <tr><td><code>int</code></td><td><code>170</code> transaksi</td><td>5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td><code>float</code></td><td><code>23395.6</code> rata-rata</td><td>5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td><code>complex</code></td><td><code>3+4j</code></td><td>5 <span class="tag kenalan">kenalan</span></td></tr>
    <tr><td><code>bool</code></td><td><code>True</code> target tercapai</td><td>5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td><code>str</code></td><td><code>"Es Kopi Susu"</code></td><td>6 <span class="tag wajib">wajib</span></td></tr>
    <tr><td><code>list</code> <code>tuple</code></td><td>daftar omzet, jam buka</td><td>7 <span class="tag wajib">wajib</span></td></tr>
    <tr><td><code>set</code></td><td>menu unik</td><td>7 <span class="tag paham">paham</span></td></tr>
    <tr><td><code>dict</code></td><td>papan menu harga</td><td>7 <span class="tag wajib">wajib</span></td></tr>
  </tbody>
</table>

<!--
⏱️ 00:57 · 1 menit (advance organizer)

"Ini peta semua jenis 'bahan' di Python. Kayak bahan di dapur: biji kopi dihitung per butir (int), susu ditakar (float), label menu berupa tulisan (str), lampu BUKA/TUTUP di pintu (bool). Kita kunjungi satu-satu."

Kategori: numeric (int, float, complex), boolean, text sequence (str), sequence (list, tuple), set (set, frozenset), mapping (dict).
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Angka

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-4 items-start">
<div>

```python
trx_jakarta = 170          # int
rata_rata = 23395.6        # float
omzet_jakarta = 4_250_000  # int

z = 3 + 4j                 # complex
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm"><code>23.5</code> ✅ &nbsp;<code>23,5</code> ❌</div></div>
  <div class="card pop"><div class="point sm"><code>4_250_000</code> = <code>4250000</code></div></div>
  <div class="card soft"><b>Rupiah → <code>int</code></b></div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 5 · Ngitung Omzet" (jalankan data kit dulu)

- "Desimal di Python pakai TITIK. 23,5 bukan angka desimal."
- "4_250_000 sama persis dengan 4250000. Underscore cuma buat mata manusia."
- "complex itu bilangan kompleks dari matematika/teknik. Cukup tahu ada."
- Uang Rupiah simpan sebagai int. Kalau ditanya kenapa: 0.1 + 0.2 = 0.30000000000000004 (lihat FAQ trainer).
- Demo type(): print(type(trx_jakarta), type(rata_rata)).
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Operator

<div class="grid grid-cols-[1.4fr_1fr] gap-8 items-start">
<table class="dense">
  <thead><tr><th>Op</th><th>Contoh</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td><code>+</code></td><td><code>4250000 + 2875000</code></td><td><code>7125000</code></td></tr>
    <tr><td><code>-</code></td><td><code>4250000 - 2875000</code></td><td><code>1375000</code></td></tr>
    <tr><td><code>*</code></td><td><code>25000 * 170</code></td><td><code>4250000</code></td></tr>
    <tr><td><code>/</code></td><td><code>4250000 / 170</code></td><td><code>25000.0</code></td></tr>
    <tr><td><code>//</code></td><td><code>455 // 50</code></td><td><code>9</code></td></tr>
    <tr><td><code>%</code></td><td><code>455 % 50</code></td><td><code>5</code></td></tr>
    <tr><td><code>**</code></td><td><code>1.1 ** 3</code></td><td><code>1.331...</code></td></tr>
  </tbody>
</table>
<div class="stack">
  <Predict :options="['5', '5.0']" :answer="1">

```python
print(10 / 2)
```

  </Predict>
  <div class="card pop small"><b><code>**</code> → <code>* /</code> → <code>+ -</code></b></div>
</div>
</div>

<!--
⏱️ 3 menit · ketik di Colab, tanya hasil sebelum run

- + total, - selisih, * harga × cup, / rata-rata (SELALU float), // bagi bulat ke bawah, % sisa bagi, ** pangkat.
- total_omzet = omzet_jakarta + omzet_bandung + omzet_surabaya → 10645000
- Predict 10 / 2: kebanyakan jawab 5. "/ selalu menghasilkan float, walaupun hasil baginya bulat."
- "Cup dikirim per kardus isi 50. Total 455 cup: // = dapat berapa kardus penuh (9), % = sisanya berapa cup (5)."
- "Kalau omzet Jakarta naik 10% tiap bulan, 3 bulan lagi?" omzet_jakarta * 1.1 ** 3 → 5656750.000000002 (lalu round).
- Urutan operasi kayak matematika SD: ** dulu, lalu * / // %, lalu + -. Ragu? Pakai kurung.
- % tidak ada di outline asli, tapi sangat sering dipakai dan berpasangan dengan //.
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Function angka

<div class="code-sm">

```python
abs(2875000 - 4250000)   # 1375000
round(23395.6043)        # 23396
round(23395.6043, 1)     # 23395.6
max(4250000, 2875000)    # 4250000
min(4250000, 2875000)    # 2875000
int(3.99)                # 3 ← dipotong!
```

</div>

<div class="grid grid-cols-2 gap-6 mt-5">
  <div class="card pop-yl"><div class="point sm">🎣 <code>round?</code> · <code>help(round)</code></div></div>
  <div class="card tk"><div class="point sm">Nggak perlu hafal ✌️</div></div>
</div>

<!--
⏱️ 2 menit

Di Colab tulis dengan print(...), contoh: print(abs(omzet_bandung - omzet_jakarta)).
- abs = selisih tanpa minus; round(x) dan round(x, 1); max/min; int(3.99) → 3 (dipotong, BUKAN dibulatkan); float(170) → 170.0.
- Sebelum int(3.99): "3 atau 4?"

Cara mancing sendiri: `round?` di Colab/Jupyter, `help(round)` di mana saja.
"Kalian nggak perlu hafal semua function. Yang penting tahu cara nyari: ?, help(), Google, atau tanya AI. Programmer profesional pun buka dokumentasi tiap hari."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Boolean: <span class="hl-tk">True</span> / <span class="hl">False</span>

<div class="grid grid-cols-[1fr_1.35fr] gap-8 mt-4 items-start">
<table>
  <thead><tr><th>Tanda</th><th>Arti</th></tr></thead>
  <tbody>
    <tr><td><code>==</code> <code>!=</code></td><td>sama / beda</td></tr>
    <tr><td><code>&gt;</code> <code>&lt;</code></td><td>lebih / kurang</td></tr>
    <tr><td><code>&gt;=</code> <code>&lt;=</code></td><td>... atau sama</td></tr>
  </tbody>
</table>
<div>

```python
total_omzet >= TARGET_HARIAN  # True
trx_bandung != 125            # False
true                          # ❌ NameError
```

<div class="card yl mt-4"><div class="point sm"><code>=</code> masukkan · <code>==</code> bandingkan</div></div>
</div>
</div>

<!--
⏱️ 2,5 menit

- Analogi: lampu BUKA / TUTUP di pintu kedai. Cuma 2 nilai: True dan False, huruf depan KAPITAL.
- Di Colab tulis dengan print(...). Contoh lain: print(omzet_jakarta > omzet_surabaya) → True; print(type(True)) → <class 'bool'>.
- "= itu memasukkan ke toples. == itu bertanya 'apakah sama?'. Ini sumber error nomor satu pemula."
- "true huruf kecil → NameError. Python cuma kenal True dan False."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag paham">paham</span></div>

## <code>and</code> · <code>or</code> · <code>not</code>

<div class="grid grid-cols-3 gap-5 mt-6">
  <div class="card pop"><h3>and</h3><div class="point sm mt-2">dua-duanya True</div></div>
  <div class="card pop"><h3>or</h3><div class="point sm mt-2">salah satu True</div></div>
  <div class="card pop"><h3>not</h3><div class="point sm mt-2">dibalik</div></div>
</div>

<div class="code-sm mt-6">

```python
total_omzet >= TARGET_HARIAN and omzet_bandung > 3_000_000  # False
total_omzet >= TARGET_HARIAN or omzet_bandung > 3_000_000   # True
```

</div>

<!--
⏱️ 1 menit

- Baris 1: "Target tercapai DAN Bandung di atas 3 juta?" → False. Baris 2: "...ATAU..." → True. not True → False.
- Di Colab tulis dengan print(...).
- Teaser: "Sekarang boolean cuma bisa jawab benar/salah. Di pertemuan berikutnya, boolean ini jadi OTAK program: 'kalau target nggak tercapai, kirim peringatan ke Bu Sari'. Itu pakai if, kode yang tadi kalian tebak di slide 13."
-->

---
mode: hands-on
where: Latihan · Bab 5
---

<div class="eyebrow">// Bab 5 · Latihan</div>

## 🎯 Latihan Bab 5

<div class="grid grid-cols-[1fr_1fr_1.1fr] gap-6">
<ol class="bullets" style="font-size: 0.8em">
  <li>Total omzet</li>
  <li>Total transaksi</li>
  <li>Rata-rata / trx</li>
  <li>Selisih max – min</li>
</ol>
<ol class="bullets" start="5" style="font-size: 0.8em">
  <li>Target tercapai?</li>
  <li><span class="tag paham">bonus</span> % capaian</li>
  <li><span class="tag wajib">tantangan</span> kardus</li>
</ol>
<div class="stack">
  <Predict :options="['3.5 0', '3 1', '3 0.5']" :answer="1">

```python
print(7 // 2, 7 % 2)
```

  </Predict>
</div>
</div>

<div class="mt-3"><StampCard :done="5" :stamping="5" compact /></div>

<!--
⏱️ 4 menit · 🎯 HANDS-ON → latihan, section "Bab 5 · Ngitung Omzet" · 🎟️ STEMPEL 5

Jalankan cell data kit dulu, lalu kerjakan satu cell per soal:
1. Total omzet 3 cabang → 10645000
2. Total transaksi → 455
3. Rata-rata omzet per transaksi, bulatkan tanpa desimal → 23396
4. Selisih tertinggi & terendah (max, min) → 1375000
5. Target harian tercapai? → True
Bonus: persen capaian → 106.45
Tantangan: cup dikirim per kardus isi 50 → 9 kardus penuh, sisa 5 cup

Setelah latihan: tebak output 7 // 2, 7 % 2 (angkat 1/2/3 jari) → 3 1.

➡️ "Angka beres! Tapi Raka masih punya masalah besar: nama menu yang berantakan. Kita istirahat dulu."
-->

---
mode: break
footer: true
---

<div class="eyebrow">// Istirahat · 10 menit</div>

## ⏸️ Ngopi dulu

<div class="grid grid-cols-[1.1fr_1fr] gap-10 mt-4 items-center">
  <div style="text-align:center"><Countdown :minutes="10" /></div>
  <div class="stack">

```python
print("10" + "5")
print(10 + 5)
```

  <div class="card pop-yl"><div class="point sm">Kenapa beda? 🤔</div></div>
  </div>
</div>

<!--
⏱️ 01:12 – 01:22 · ISTIRAHAT

- Klik timer untuk mulai. Dobel klik = reset.
- Teka-teki: "Kenapa hasilnya beda? Jawabannya setelah istirahat."
- Pakai waktu ini untuk menghampiri peserta yang tadi 🔴. Cek semua sudah sampai latihan Bab 5.
-->

---
section: Bab 6 · Beresin Nama Menu
bab: 6
mode: colab-demo
where: Materi · Bab 6
---

<div class="ghostnum">06</div>
<div class="eyebrow">// Bab 6 · Beresin nama menu</div>

## Satu menu, tiga tulisan

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-4 items-start">
<div class="stack">
  <div class="card"><code>"  es kopi SUSU gula aren "</code></div>
  <div class="card"><code>"ES KOPI SUSU GULA AREN"</code></div>
  <div class="card"><code>"Es Kopi susu Gula Aren   "</code></div>
</div>
<div class="stack">

```python
menu_kasir_jkt == menu_kasir_bdg
# False 😱
```

  <div v-click class="card tk"><code>"10" + "5"</code> → <code>"105"</code> (teks digabung)</div>
</div>
</div>

<!--
⏱️ 01:22 · 1,5 menit · 🧪 COLAB → materi, section "Bab 6 · Beresin Nama Menu" (jalankan data kit teks)

- Kasir Jakarta, Bandung, Surabaya menulis menu yang sama dengan cara beda. "Buat manusia: menu yang sama. Buat komputer: tiga menu berbeda."
- Klik: jawaban teka-teki istirahat. "'10' + '5' itu teks digabung, makanya '105'. Hari ini kita kenalan sama teks (str), dan di akhir bab ini, False tadi akan berubah jadi True."
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## String = teks

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-4 items-start">
<div>

```python
nama_toko = "Kopi Senja"
slogan = 'Seduh rasa'

"Kopi" + " " + "Senja"   # gabung
"=" * 30                 # ulang
len(nama_toko)           # 10
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm"><code>+</code> gabung</div></div>
  <div class="card pop"><div class="point sm"><code>*</code> ulang</div></div>
  <div class="card soft"><code>'...'</code> = <code>"..."</code></div>
</div>
</div>

<!--
⏱️ 1,5 menit

- Kutip satu atau dua sama saja, yang penting konsisten. Kutip tiga """...""" bisa banyak baris (contoh alamat di notebook).
- "Kopi" + " " + "Senja" → Kopi Senja. "=" * 30 → garis pemisah laporan Bu Sari! len() menghitung jumlah karakter (spasi dihitung).
- Di Colab tulis dengan print(...).
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 2
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Indexing: nomor tiap karakter

<div class="mt-2"><IndexStrip text="TRX-20261005-JKT-0170" :sels="['[0]', '[-1]']" /></div>

<div class="grid grid-cols-3 gap-5 mt-6">
  <div class="card pop"><div class="point sm">Mulai dari 0</div></div>
  <div class="card pop"><div class="point sm">Minus = dari belakang</div></div>
  <div class="card yl"><b>📕 IndexError</b> = kelewatan</div>
</div>

<!--
⏱️ 2 menit

- Klik → sorot kode_trx[0] ('T'), klik lagi → kode_trx[-1] ('0').
- Struktur kode transaksi: TRX - tanggal - kode cabang - nomor urut.
- "Kenapa mulai dari 0? Anggap index itu jarak dari awal."
- Di Colab: print(len(kode_trx)) → 21. "Panjangnya 21, index terakhir berapa?" (20). print(kode_trx[21]) → IndexError: string index out of range.
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 5
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Slicing <code>[start:stop]</code>

<div class="mt-1"><IndexStrip text="TRX-20261005-JKT-0170" :sels="['[0:3]', '[4:12]', '[4:8]', '[13:16]', '[-4:]']" /></div>

<div class="grid grid-cols-3 gap-5 mt-6">
  <div class="card pop"><div class="point sm">stop nggak ikut</div></div>
  <div class="card pop"><div class="point sm">🔪 potong di antara</div></div>
  <div class="card pop-yl"><div class="point sm"><code>[:3]</code> · <code>[-4:]</code></div></div>
</div>

<!--
⏱️ 2,5 menit

- Tiap klik menyorot satu slice: [0:3] TRX, [4:12] tanggal, [4:8] tahun, [13:16] JKT, [-4:] 0170.
- Aturan: ambil dari start, sampai SEBELUM stop.
- Mental model: "Bayangkan pisau memotong DI ANTARA karakter. Angka di slicing = posisi pisau."
- Start kosong = dari awal ([:3]); stop kosong = sampai akhir ([-4:]).
- Sebelum klik ke-3: "Ambilkan tahunnya saja, index berapa sampai berapa?"
- "Kenapa stop nggak ikut? Biar gampang ngitung: [4:12] panjangnya pasti 12 - 4 = 8 karakter."
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 3
---

<div class="eyebrow">// Bab 6 <span class="tag paham">paham</span></div>

## Slicing dengan langkah

<div class="mt-2"><IndexStrip text="0123456789" name="angka" :neg="false" :sels="['[::2]', '[1::2]', '[::-1]']" /></div>

<div class="point mt-10"><code>[::-1]</code> = dibalik 🔄</div>

<!--
⏱️ 1 menit

- teks[start:stop:step], step = loncat berapa langkah.
- angka[::2] → 02468 (genap), angka[1::2] → 13579 (ganjil), kode_trx[::-1] → dibalik.
- "[::-1] itu trik terkenal buat membalik teks. Step jarang dipakai sehari-hari, cukup tahu cara bacanya."
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## String nggak bisa diubah

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
kode_trx[0] = "X"
# ❌ TypeError
```

</div>
<div>

```python
kode_baru = kode_trx.replace("JKT", "BDG")
```

</div>
</div>

<div class="grid grid-cols-2 gap-8 mt-6">
  <div class="card pop"><div class="point sm">Mau ganti? Bikin <span class="hl">baru</span></div></div>
  <div class="card yl"><b>📕 TypeError</b> = tipe nggak cocok</div>
</div>

<!--
⏱️ 1,5 menit

- Immutable = tidak bisa diubah sebagian. "Kayak tulisan yang dicetak di gelas: mau ganti, cetak gelas baru."
- Error lengkap: TypeError: 'str' object does not support item assignment.
- replace bikin string BARU: print(kode_baru) → TRX-20261005-BDG-0170, print(kode_trx) → yang lama tetap.
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Method: beres-beres teks

<div class="grid grid-cols-[1fr_1.15fr] gap-6 items-start">
<table class="dense">
  <thead><tr><th>Method</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td><code>.strip()</code></td><td>buang spasi</td></tr>
    <tr><td><code>.upper()</code> <code>.lower()</code></td><td>BESAR / kecil</td></tr>
    <tr><td><code>.title()</code></td><td>Huruf Depan</td></tr>
    <tr><td><code>.replace(a, b)</code></td><td>ganti</td></tr>
    <tr><td><code>.split("-")</code></td><td>pecah</td></tr>
  </tbody>
</table>
<div class="code-sm">

```python
bersih_jkt = menu_kasir_jkt.strip().title()
bersih_bdg = menu_kasir_bdg.strip().title()
bersih_jkt == bersih_bdg   # True 🎉
```

</div>
</div>

<div class="mt-4">
<Predict :options="['[LATTE]', '[  LATTE  ]', '[  latte  ]']" :answer="2">

```python
menu = "  latte  "; menu.upper(); print("[" + menu + "]")
```

</Predict>
</div>

<!--
⏱️ 3 menit · momen "aha" bab ini

- Contoh: "  latte  ".strip() → "latte"; "Latte".upper() → "LATTE"; "es kopi".title() → "Es Kopi"; kode_trx.split("-") → ['TRX', '20261005', 'JKT', '0170'].
- Method bisa DIRANTAI: .strip().title(). Tunjukkan bersih_jkt == bersih_bdg → True. False tadi jadi True!
- Jebakan tebak output → C. "Ingat, string immutable. Method TIDAK mengubah aslinya, tapi mengembalikan string BARU. Kalau mau disimpan: menu = menu.upper()."
- Method lain: .count(), .startswith(), .center(). Cari sendiri: ketik menu. lalu Tab di Colab, atau dir(str).
- .split() menghasilkan LIST → jembatan ke Bab 7: "Kurung siku ini namanya list."
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Casting: ganti tipe

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-4 items-start">
<div>

```python
int("0170")      # 170
str(170)         # "170"
float("23.5")    # 23.5
int("17O")       # ❌ ValueError
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm">Data sering datang sebagai teks</div></div>
  <div class="card yl"><b>📕 ValueError</b> = isinya bukan angka</div>
</div>
</div>

<!--
⏱️ 1,5 menit

- Di notebook: nomor = kode_trx[-4:] → '0170' (str); int(nomor) → 170 (nol di depan hilang).
- "Data dari file atau input sering datang sebagai teks, walaupun isinya angka."
- int("17O"): "Kasir kadang ngetik huruf O, bukan angka 0. Python langsung protes: tipenya benar (teks), tapi ISINYA nggak bisa jadi angka."
- Kamus Error: ValueError = "Tipenya benar, nilainya nggak masuk akal."
-->

---
mode: hands-on
where: Latihan · Bab 6
---

<div class="eyebrow">// Bab 6 · Latihan</div>

## 🎯 Latihan Bab 6

<div class="grid grid-cols-[1fr_1fr] gap-6">
<div>
<ol class="bullets" style="font-size: 0.85em">
  <li>Rapikan 3 nama menu</li>
  <li>Buktikan sama: <code>==</code></li>
  <li>Ambil tanggal, cabang, nomor</li>
  <li>Nomor → <code>170</code></li>
  <li><span class="tag paham">bonus</span> <code>"05-10-2026"</code></li>
</ol>
</div>
<div v-click class="code-xs">
<div class="box-h">Kunci</div>

```python
bersih = menu_kasir_jkt.strip().title()
print(kode_trx[4:12], kode_trx[13:16])
print(int(kode_trx[-4:]))       # 170
print(kode_trx[10:12] + "-" + kode_trx[8:10]
      + "-" + kode_trx[4:8])    # 05-10-2026
```

</div>
</div>

<div class="mt-3"><StampCard :done="6" :stamping="6" compact /></div>

<!--
⏱️ 5,5 menit · 🎯 HANDS-ON → latihan, section "Bab 6 · Beresin Nama Menu" · 🎟️ STEMPEL 6

Jalankan data kit teks dulu, jangan diketik ulang (supaya spasinya tetap berantakan).
1. Bersihkan ketiga nama menu jadi "Es Kopi Susu Gula Aren"
2. Buktikan ketiganya sama (pakai == dan and): bersih_jkt == bersih_bdg and bersih_bdg == bersih_sby → True
3. Dari kode_trx ambil: tanggal "20261005", kode cabang "JKT", nomor "0170"
4. Ubah nomor transaksi jadi angka 170
Bonus: tanggal format "05-10-2026"
Tantangan: berapa huruf "a" di nama menu bersih? bersih.lower().count("a") → 2

Klik untuk membuka kunci setelah waktu habis.

➡️ "Teks udah rapi. Tapi Raka mulai sadar ada masalah lain..."
-->

---
section: Bab 7 · Wadah Banyak Barang
bab: 7
mode: colab-demo
where: Materi · Bab 7
---

<div class="ghostnum">07</div>
<div class="eyebrow">// Bab 7 · Wadah banyak barang <span class="tag wajib">wajib</span></div>

## 30 cabang? → <code>list</code>

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-2 items-start">
<div class="code-sm">

```python
omzet = [4_250_000, 2_875_000, 3_520_000]

omzet[0]               # 4250000
omzet[-1]              # 3520000
sum(omzet)             # 10645000
max(omzet)             # 4250000

omzet[1] = 2_900_000   # bisa diubah
omzet.append(1_980_000)
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm">Urut · bisa diubah</div></div>
  <div class="card pop-yl"><div class="point sm">Indexing = sama kayak string</div></div>
</div>
</div>

<!--
⏱️ 01:42 · 3,5 menit · 🧪 COLAB → materi, section "Bab 7 · Wadah Banyak Barang"

- Cerita: "Kopi Senja buka 30 cabang. Berarti omzet_jakarta, omzet_bandung, ... 30 variabel? Plus 30 variabel transaksi?" → list.
- List = antrean pesanan: urut, bisa ditambah, bisa diubah.
- Di Colab tulis dengan print(...). Contoh lain: cabang = ["Jakarta", "Bandung", "Surabaya"], cabang[0:2], len(omzet), min(omzet), sorted(omzet, reverse=True), cabang.append("Yogyakarta").
- Sebelum omzet[0]: "Kalian udah tahu caranya dari Bab 6. Tebak hasilnya?"
- "Semua ilmu indexing string berlaku juga di list. Bedanya: string immutable, list mutable."
- "sum() di list ini andalan Raka: 30 cabang pun tetap satu baris."
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag paham">paham</span></div>

## <code>tuple</code>: list yang dikunci

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-start">
<div>

```python
JAM_OPERASIONAL = (7, 22)
JAM_OPERASIONAL[0]       # 7
JAM_OPERASIONAL[0] = 8   # ❌ TypeError
```

</div>
<div class="card pop"><div class="icon">🔒</div><div class="point sm mt-3">Data yang nggak boleh berubah</div></div>
</div>

<!--
⏱️ 1 menit

- Tuple pakai kurung biasa ( ). Contoh lain: LOKASI_JKT = (-6.2, 106.8) (koordinat).
- "Tuple itu kayak list yang DIKUNCI. Cocok buat data yang memang nggak boleh berubah: jam buka di pintu, koordinat."
- Error lengkap: TypeError: 'tuple' object does not support item assignment.
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag paham">paham</span></div>

## <code>set</code>: hanya yang unik

<div class="grid grid-cols-[1.4fr_1fr] gap-8 mt-6 items-start">
<div>

```python
terjual = ["latte", "kopi susu", "latte"]
set(terjual)
# {'latte', 'kopi susu'}
```

</div>
<div class="stack">
  <div class="card pop"><div class="point sm">Buang duplikat · tanpa urutan</div></div>
  <div class="card soft"><span class="tag kenalan">kenalan</span> <code>frozenset</code></div>
</div>
</div>

<!--
⏱️ 1,5 menit

- Contoh di notebook: menu_terjual = ["kopi susu", "latte", "kopi susu", "americano", "latte"] → set → 3 jenis menu.
- "Set otomatis membuang duplikat dan tidak punya urutan, jadi nggak bisa diakses pakai index." Urutan print bisa beda-beda, normal.
- frozenset = set yang nggak bisa diubah. Cukup tahu.
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag wajib">wajib</span></div>

## <code>dict</code>: papan menu

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-4 items-start">
<div>

```python
harga = {
    "kopi susu": 25000,
    "latte": 28000,
}
harga["latte"]       # 28000
harga["teh tarik"]   # ❌ KeyError
```

</div>
<div class="stack">
  <div class="card pop-yl">
    <div class="box-h">📋 Papan menu</div>
    <div class="mono">kopi susu ... 25.000<br>latte ....... 28.000</div>
  </div>
  <div class="card yl"><b>📕 KeyError</b> = kunci nggak ada</div>
</div>
</div>

<!--
⏱️ 2 menit

- dict = {kunci: nilai}. Tambah menu: harga["matcha latte"] = 30000.
- "Di list, kita nyari pakai nomor urut. Di dict, kita nyari pakai NAMA. Kayak papan menu: kita nggak bilang 'menu nomor 2', tapi 'latte berapa?'."
- Contoh lain di notebook: omzet_cabang = {"Jakarta": 4_250_000, ...}; sum(omzet_cabang.values()) → 10645000.
-->

---

<div class="eyebrow">// Bab 7</div>

## Pilih wadah

<table class="dense">
  <thead><tr><th>Wadah</th><th>Tanda</th><th>Urut?</th><th>Diubah?</th><th>Dobel?</th></tr></thead>
  <tbody>
    <tr><td><code>list</code></td><td><code>[ ]</code></td><td>✅</td><td>✅</td><td>✅</td></tr>
    <tr><td><code>tuple</code></td><td><code>( )</code></td><td>✅</td><td>❌</td><td>✅</td></tr>
    <tr><td><code>set</code></td><td><code>{ }</code></td><td>❌</td><td>✅</td><td>❌</td></tr>
    <tr><td><code>dict</code></td><td><code>{k: v}</code></td><td>✅</td><td>✅</td><td>kunci ❌</td></tr>
  </tbody>
</table>

<div class="grid grid-cols-4 gap-4 mt-3 small">
  <div class="card flex justify-between items-center gap-2">Transaksi urut<span v-click class="answer">list</span></div>
  <div class="card flex justify-between items-center gap-2">Koordinat<span v-click class="answer">tuple</span></div>
  <div class="card flex justify-between items-center gap-2">Pelanggan unik<span v-click class="answer">set</span></div>
  <div class="card flex justify-between items-center gap-2">Stok per bahan<span v-click class="answer">dict</span></div>
</div>

<div class="mt-3"><StampCard :done="7" :stamping="7" compact /></div>

<!--
⏱️ 2 menit · kuis cepat, jawab serentak / di chat · 🎟️ STEMPEL 7

Analogi: list = antrean pesanan, tuple = jam buka di pintu, set = daftar jenis menu terjual, dict = papan menu.
Kuis: daftar transaksi hari ini urut waktu → list; koordinat lokasi cabang → tuple; daftar pelanggan unik → set; stok bahan berdasarkan nama ("susu": 12) → dict.
dict menyimpan urutan dimasukkan (Python 3.7+).

➡️ "Semua data udah rapi di wadahnya. Tinggal satu: MENYAJIKAN laporannya ke Bu Sari."
-->

---
section: Bab 8 · Laporan buat Bu Sari
bab: 8
mode: colab-demo
where: Materi · Bab 8
---

<div class="ghostnum">08</div>
<div class="eyebrow">// Bab 8 · Laporan buat Bu Sari <span class="tag paham">paham</span></div>

## Escape character

<div class="grid grid-cols-[1fr_1.5fr] gap-8 mt-4 items-start">
<table>
  <thead><tr><th>Escape</th><th>Arti</th></tr></thead>
  <tbody>
    <tr><td><code>\n</code></td><td>baris baru</td></tr>
    <tr><td><code>\t</code></td><td>tab</td></tr>
    <tr><td><code>\"</code></td><td>kutip</td></tr>
    <tr><td><code>\\</code></td><td>backslash</td></tr>
  </tbody>
</table>
<div>

```python
print("Laporan \"Kopi Senja\"\nTgl:\t05-10")
```

<div class="code-yl">

```text
Laporan "Kopi Senja"
Tgl:	05-10
```

</div>
</div>
</div>

<!--
⏱️ 01:52 · 2 menit · 🧪 COLAB → materi, section "Bab 8 · Laporan buat Bu Sari"

- print() bisa pakai sep: print("Jakarta", "Bandung", "Surabaya", sep=" | ") → Jakarta | Bandung | Surabaya.
- \n baris baru, \t tab (rata kolom), \" \' kutip di dalam teks, \\ garis miring terbalik.
- Jebakan klasik (ceritakan saja): print("C:\data\new") → \n jadi baris baru. Solusi: "C:\\data\\new" atau raw string r"C:\data\new".
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8</div>

## Teks + angka = ❌

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-8 items-center">
<div class="code-lg code-err">

```python
total_omzet = 10645000
print("Total: " + total_omzet)
```

</div>
<div class="card err">
<div class="box-h" style="color: var(--err)">TypeError</div>
<div class="point sm">str + int nggak bisa</div>
</div>
</div>

<!--
⏱️ 1 menit

Cerita: Raka mencoba bikin laporan, langsung kena error.
- Error lengkap: TypeError: can only concatenate str (not "int") to str.
- "Teks + angka = nggak bisa. Kayak nyampur gula sama tulisan 'gula'. Gimana solusinya? Ternyata Python punya beberapa cara dari zaman ke zaman."
-->

---

<div class="eyebrow">// Bab 8 <span class="tag wajib">f-string wajib</span></div>

## 4 cara, pilih f-string

```python
"Total: " + str(total_omzet)        # 1. ribet
"Total: %d" % total_omzet           # 2. jadul
"Total: {}".format(total_omzet)     # 3. lama
f"Total: {total_omzet}"             # 4. ⭐ pakai ini
```

<div class="point mt-8"><code>f"..."</code> + variabel di <code>{ }</code></div>

<!--
⏱️ 2 menit

- Semua hasilnya sama: Total: 10645000.
- "Kalian perlu KENAL cara 2 (gaya %) dan 3 (.format) karena masih sering muncul di kode orang lain atau di internet. Tapi kalau nulis sendiri, pakai f-string: huruf f di depan kutip, variabel di dalam kurung kurawal { }."
- f-string ada sejak Python 3.6.
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8 <span class="tag wajib">wajib</span></div>

## f-string superpower

<div class="grid grid-cols-[1fr_1.2fr] gap-6 mt-4 items-start">
<table class="dense">
  <thead><tr><th>Format</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td><code>{total_omzet}</code></td><td>10645000</td></tr>
    <tr><td><code>{total_omzet:,}</code></td><td>10,645,000</td></tr>
    <tr><td><code>{106.4512:.2f}</code></td><td>106.45</td></tr>
    <tr><td><code>{toko.upper()}</code></td><td>KOPI SENJA</td></tr>
  </tbody>
</table>
<div class="code-sm">

```python
f"Rp{total_omzet:,}".replace(",", ".")
# Rp10.645.000
```

</div>
</div>

<div class="card pop-yl mt-6"><div class="point sm"><code>.replace</code> = ilmu Bab 6 🧩</div></div>

<!--
⏱️ 3 menit

- f-string bisa berisi variabel, ekspresi/hitungan (f"{total_omzet / 455}"), pemisah ribuan (:,), desimal (:.2f), dan method.
- Demo di Colab:
  persen_target = total_omzet / TARGET_HARIAN * 100
  print(f"Total omzet : Rp{total_omzet:,}")                    → Rp10,645,000 (gaya Inggris)
  print(f"Total omzet : Rp{total_omzet:,}".replace(",", "."))  → Rp10.645.000 (gaya Indonesia)
  print(f"Capaian     : {persen_target:.2f}%")                 → 106.45%
  print(f"Tercapai?   : {total_omzet >= TARGET_HARIAN}")       → True
- "Perhatikan trik .replace(",", "."): itu string method dari Bab 6. Semua yang kita pelajari mulai nyambung."
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8 <span class="tag wajib">wajib</span></div>

## <code>input()</code> selalu teks

<div class="grid grid-cols-[1fr_1.15fr] gap-8 mt-4 items-start">
<div class="stack">

```python
nama = input("Nama: ")
```

<div v-click="2">

```python
trx = int(input("Trx: "))
print(trx * 2)   # 20
```

</div>
</div>
<Predict :options="['20', '1010', 'Error']" :answer="1">

```python
trx = input("Trx: ")  # ketik 10
print(trx * 2)
```

</Predict>
</div>

<!--
⏱️ 2,5 menit · momen paling berkesan, JANGAN dilewati

- input() memunculkan kotak isian di Colab; cell "berputar" sampai kita tekan Enter (bukan hang!). Kalau macet: tombol ■ interrupt.
- Contoh: nama_analis = input("Nama analis: "); print(f"Laporan disusun oleh {nama_analis}").
- Tebak output → B "1010". "input() SELALU menghasilkan string, apa pun yang diketik. '10' * 2 = teks diulang 2 kali. Sama kayak teka-teki sebelum istirahat."
- Klik ke-2: perbaikan pakai casting dari Bab 6 → int(input(...)).
-->

---
mode: hands-on
where: Latihan · Bab 8
---

<div class="eyebrow">// Bab 8 · Latihan</div>

## 🎯 Latihan Bab 8

<div class="grid grid-cols-[1fr_1.1fr] gap-8">
<div>
<ol class="bullets" style="font-size: 0.85em">
  <li><code>input()</code> nama analis</li>
  <li>Cetak header →</li>
  <li>Format <code>Rp10.645.000</code></li>
  <li><span class="tag paham">bonus</span> % capaian</li>
</ol>
</div>
<div class="code-yl">

```text
========================================
LAPORAN HARIAN KOPI SENJA
Analis : Raka Pratama
========================================
Total omzet : Rp10.645.000
```

</div>
</div>

<div class="mt-4"><StampCard :done="8" :stamping="8" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 8 · Laporan buat Bu Sari" · 🎟️ STEMPEL 8

1. Minta nama analis lewat input(), rapikan pakai .strip().title()
2. Cetak header seperti contoh (garis = "=" * 40)
3. Cetak total omzet format Rupiah: f"Total omzet : Rp{total_omzet:,}".replace(",", ".")
Bonus: minta target lewat input() (pakai int()), hitung persen capaian dengan :.2f

Kunci lengkap ada di 03_kunci_jawaban.ipynb.

➡️ "8 stempel penuh. Saatnya tukar dengan kopi gratis: LAPORAN OTOMATIS RAKA."
-->

---
section: Final · Satu Klik, Laporan Jadi
bab: 9
---

<div class="eyebrow">// Final · Satu klik, laporan jadi</div>

## Misi: Laporan Harian v1.0

<div class="grid grid-cols-[1.15fr_1fr] gap-8 items-start">
<div class="code-xs">

```text
============================================
         LAPORAN HARIAN KOPI SENJA
============================================
Tanggal          : 05-10-2026
Analis           : Raka Pratama
--------------------------------------------
  Jakarta    : Rp4.250.000 (170 trx)
  Bandung    : Rp2.875.000 (125 trx)
  Surabaya   : Rp3.520.000 (160 trx)
--------------------------------------------
Total omzet      : Rp10.645.000
Rata-rata/trx    : Rp23.396
Menu terlaris    : Es Kopi Susu Gula Aren
--------------------------------------------
Capaian          : 106.45%
Target tercapai? : True
============================================
```

</div>
<div class="stack">
  <div class="card tk"><div class="box-h">🟢 Wajib</div><div class="point sm">Isi semua <code>___</code></div></div>
  <div class="card yl"><div class="box-h">🟡 Bonus</div><div class="point sm">Cabang terbaik</div></div>
  <div class="card"><div class="box-h">🔴 Tantangan</div><div class="point sm">Omzet via <code>input()</code></div></div>
</div>
</div>

<!--
⏱️ 02:07 · 2 menit

- Wajib: isi semua ___ di template sampai laporan tampil.
- Bonus: tambah baris "Cabang terbaik: Jakarta" (hint: cabang[omzet.index(max(omzet))]).
- Tantangan: omzet tiap cabang juga diminta lewat input().
- "Perhatikan: tiap baris laporan ini pakai sesuatu yang kalian pelajari hari ini. Coba tebak, baris 'Menu terlaris' pakai ilmu dari bab berapa?" (Bab 6)
-->

---
mode: hands-on
where: Latihan · Final
---

<div class="eyebrow">// Final</div>

## 🎯 Kerjakan!

<div class="grid grid-cols-[1fr_1.1fr] gap-8 mt-2">
<div class="stack">
  <Goto to="hands-on" where="Latihan · section Final" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
  <div><Countdown :minutes="10" small /></div>
</div>
<div>
<div class="box-h">🪜 Kalau stuck</div>
<div class="stack" style="gap: 10px">
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">1</span><b>Cek komentar <code>[Bab X]</code></b></div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">2</span><b>Lihat latihan bab itu</b></div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">3</span><b>Tanya teman</b></div>
  <div class="card pop-yl flowrow"><span class="num" style="font-size:1.6rem">4</span><b>Sinyal 🔴</b></div>
</div>
</div>
</div>

<!--
⏱️ 10 menit · 🎯 HANDS-ON → latihan, section "Final · Laporan Harian v1.0"

- Sampaikan di awal: kalau masih ada ___ yang tersisa, Python protes NameError: name '___' is not defined, artinya masih ada yang belum diisi.
- Tangga petunjuk: cek komentar [Bab X] di template → scroll ke latihan bab itu di notebook sendiri → tanya teman sebelah (boleh pair programming) → angkat sinyal 🔴.
- Keliling / buka breakout room. Prioritaskan peserta 🔴.
- Yang selesai cepat → 🟡/🔴, atau jadi "asisten" teman sebelah.
- Menit ke-8: "2 menit lagi".
-->

---
mode: vscode
where: kopi-senja/laporan.py
---

<div class="eyebrow">// Final · Momen "aha"</div>

## Notebook → script

<div class="grid grid-cols-[1fr_1.1fr] gap-10 mt-6 items-center">
<div>

```bash
python3 laporan.py
```

<div class="mt-6"><Goto to="vscode" where="kopi-senja/laporan.py" /></div>
</div>
<div class="stack">
  <div class="flowrow" style="gap: 16px">
    <div class="huge" style="font-size: 3.4rem; text-decoration: line-through; text-decoration-thickness: 6px; text-decoration-color: var(--err)">65 mnt</div>
    <div class="arw" style="font-size: 2.6rem">➜</div>
    <div class="huge" style="font-size: 3.4rem"><span class="hl-tk">1 dtk</span></div>
  </div>
  <div class="point mt-4">Yang nulis kodenya: <span class="hl">kalian</span>.</div>
</div>
</div>

<!--
⏱️ 3 menit · 💻 PINDAH KE VSCODE → kopi-senja/laporan.py (sudah disiapkan)

- Jalankan, isi nama & tanggal → laporan muncul.
- "Ini yang sekarang dijalankan Raka tiap pagi. Satu perintah. 65 menit jadi 1 detik. Nggak ada lagi salah ketik nol. Bu Sari dapat laporan yang sama rapinya setiap hari. Dan yang nulis kodenya... kalian."
- Show & tell: 1–2 peserta share screen hasil mereka (terutama yang mengerjakan bonus). Beri apresiasi.
-->

---
section: Epilog · Bersambung...
bab: 10
---

<div class="eyebrow">// Epilog</div>

## Kotak perkakas Raka

<table class="dense">
  <thead><tr><th>Masalah</th><th>Alat</th></tr></thead>
  <tbody>
    <tr><td>Angka berserakan</td><td>Variabel</td></tr>
    <tr><td>Hitung omzet</td><td>Operator, <code>sum</code> <code>max</code> <code>round</code></td></tr>
    <tr><td>Cek target</td><td>Boolean</td></tr>
    <tr><td>Nama menu berantakan</td><td><code>.strip()</code> <code>.title()</code></td></tr>
    <tr><td>Bongkar kode transaksi</td><td>Slicing, <code>int()</code></td></tr>
    <tr><td>Banyak cabang</td><td><code>list</code> <code>dict</code></td></tr>
    <tr><td>Laporan rapi</td><td>f-string, <code>input()</code></td></tr>
  </tbody>
</table>

<!--
⏱️ 02:22 · 2 menit

Recap: tiap masalah Raka → alatnya. Plus: error → baca dari baris paling bawah.
Tanya: "Dari semua ini, mana yang paling bikin kalian 'ooh!'?" (1–2 jawaban)
-->

---

<div class="eyebrow">// 📖 Tapi...</div>

## Raka masih punya PR

<div class="grid grid-cols-2 gap-5 mt-4">
  <div class="card pop"><div class="point sm">Data masih diketik</div><div class="mt-2">→ <b>pandas</b></div></div>
  <div class="card pop-yl"><div class="point sm">Target gagal? Kasih alert</div><div class="mt-2">→ <b><code>if</code> / <code>else</code></b></div></div>
  <div class="card pop"><div class="point sm">30 cabang = 30 print?</div><div class="mt-2">→ <b>loop <code>for</code></b></div></div>
  <div class="card pop-yl"><div class="point sm">Bikin mesin sendiri</div><div class="mt-2">→ <b>function</b></div></div>
</div>

<div class="mt-8 flex items-center gap-6">
  <div class="huge" style="font-size: 3rem">Bersambung...</div>
  <span class="sticker">☕ pertemuan berikutnya</span>
</div>

<!--
⏱️ 2 menit

1. "Data omzetnya masih diketik manual di kode." → baca file Excel/CSV (pandas)
2. "Kalau target nggak tercapai, aku mau kasih peringatan otomatis." → if / else (boolean tadi jadi otaknya)
3. "Kalau cabangnya 30, masa nulis 30 baris print?" → loop (for)
4. "Aku pengen bikin mesin sendiri kayak print()." → function buatan sendiri

"Kalian sendiri ngerasain kan waktu nulis 3 baris print per cabang di final project? Bayangin 30. Bersambung..."
Sesuaikan kartu dengan silabus pertemuan berikutnya.
-->

---

<div class="eyebrow">// Epilog</div>

## Latihan mandiri

<div class="grid grid-cols-[1.3fr_1fr] gap-6 items-start">
<table>
  <thead><tr><th>#</th><th>Platform</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://codesaya.com/python" target="_blank">Codesaya</a> · bahasa Indonesia</td></tr>
    <tr><td>2</td><td><a href="https://www.kaggle.com/learn/python" target="_blank">Kaggle Learn</a> · notebook</td></tr>
    <tr><td>3</td><td><a href="https://www.hackerrank.com/domains/python" target="_blank">HackerRank</a> · soal bertingkat</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com" target="_blank">LeetCode</a> · <b>nanti dulu</b></td></tr>
  </tbody>
</table>
<div class="card pop-yl">
<div class="box-h">📝 PR</div>
<ol>
  <li>Cabang terbaik & terlemah</li>
  <li>% kontribusi Jakarta</li>
  <li>Tambah cabang ke-4 😉</li>
</ol>
</div>
</div>

<!--
⏱️ 2 menit

Platform (urut dari paling ramah pemula):
1. Codesaya: bahasa Indonesia, interaktif
2. Kaggle Learn Python: gratis, berbasis notebook, orientasi data (lesson 1–2)
3. HackerRank: Introduction, Basic Data Types, Strings
4. LeetCode: nanti dulu, setelah paham if, loop, function

PR:
1. Baris "Cabang terbaik" & "Cabang terlemah"
2. Persentase kontribusi Jakarta terhadap total omzet (2 desimal)
3. Data cabang ke-4 (Yogyakarta, omzet 1.980.000, 88 transaksi). Rasakan berapa baris yang harus diubah → motivasi alami untuk loop.
-->

---

<div class="eyebrow">// Epilog</div>

## Exit ticket 3-2-1

<div class="grid grid-cols-3 gap-6 mt-8">
  <div class="card pop" style="text-align:center; padding: 26px"><div class="huge">3</div><div class="point sm mt-3">yang dipelajari</div></div>
  <div class="card pop-yl" style="text-align:center; padding: 26px"><div class="huge">2</div><div class="point sm mt-3">yang bingung</div></div>
  <div class="card pop" style="text-align:center; padding: 26px"><div class="huge">1</div><div class="point sm mt-3">pertanyaan</div></div>
</div>

<!--
⏱️ 1 menit

- 3 hal yang aku pelajari hari ini · 2 hal yang masih bikin bingung · 1 pertanyaan yang masih ingin ditanyakan.
- Bagikan link form di chat.
- Baca jawaban "2 hal bingung" sebelum pertemuan berikutnya → buka dengan review 5 menit soal topik yang paling sering muncul.
-->

---
layout: default
class: closing
footer: false
---

<div class="cover-frame"></div>

<div class="eyebrow">// Terima kasih ☕</div>

# Laporan sudah <span class="hl">jadi</span>.

<div class="grid grid-cols-[1.5fr_1fr] gap-8 mt-6 items-start" style="max-width: 980px">
  <StampCard :done="8" />
  <div class="stack small">
    <a href="https://github.com/thosangs/python_lecture" target="_blank">📦 Repo</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/01_materi_kopi_senja.ipynb" target="_blank">📓 Materi (Colab)</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/03_kunci_jawaban.ipynb" target="_blank">🔑 Kunci (Colab)</a>
  </div>
</div>

<!--
⏱️ 1 menit · Q&A

"Hari ini kalian udah nulis program pertama yang benar-benar berguna. Error akan terus datang. Itu tanda kalian sedang belajar, bukan tanda kalian nggak bisa."
Komunitas: PythonID · PyCon ID.
-->
