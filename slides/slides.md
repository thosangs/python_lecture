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

<div class="lead" style="max-width: 640px">Dari Excel manual ke laporan otomatis. <b>Satu cerita, 2,5 jam</b>, dan kamu yang nulis kodenya.</div>

<div class="row mt-8" style="max-width: 760px">
  <div class="card pop"><div class="box-h">Durasi</div><b>2,5 jam</b></div>
  <div class="card pop"><div class="box-h">Level</div><b>Pemula total</b></div>
  <div class="card pop"><div class="box-h">Mode</div><b>Cerita + live coding</b></div>
</div>

<div class="sticker" style="position:absolute; right: 70px; top: 90px; font-size: 1rem">☕ Kopi Senja Edition</div>

<!--
⏱️ 00:00 · 1 menit

- Perkenalan singkat diri (maks 30 detik), langsung ke slide berikutnya.
- Tips navigasi: `o` = overview, `g` = loncat ke nomor slide, `d` = toggle dark/light. Mode presenter: tambahkan `/presenter` di URL.
-->

---

<div class="eyebrow">// Sebelum mulai</div>

## Angkat tangan dulu! ✋

<div class="grid grid-cols-3 gap-6 mt-6">
  <div class="card pop">
    <div class="num">01</div>
    <p class="mt-3">Siapa yang pakai <b>Excel / Spreadsheet</b> hampir tiap hari?</p>
  </div>
  <div class="card pop-yl">
    <div class="num">02</div>
    <p class="mt-3">Siapa yang pernah ngerjain <b>hal yang sama berulang-ulang</b> tiap hari/minggu?</p>
  </div>
  <div class="card pop">
    <div class="num">03</div>
    <p class="mt-3">Siapa yang <b>pernah ngoding</b>, bahasa apa pun?</p>
  </div>
</div>

<div class="mt-10 lead">Kalau nomor 2 banyak yang angkat tangan... <b>kalian nggak sendirian.</b> Kenalin, Raka. 👉</div>

<!--
⏱️ 1 menit · KALIBRASI

- Catat dalam hati proporsi yang pernah ngoding.
- Banyak yang sudah ngoding → siapkan tantangan 🔴. Hampir semua belum → lambatkan Bab 4–6.
- Pertanyaan 2 = jembatan emosional ke cerita Raka.
-->

---

<div class="eyebrow">// Tokoh utama</div>

## Kenalan sama Raka

<div class="grid grid-cols-[1fr_1.3fr] gap-10 mt-4 items-center">
  <div class="card pop-yl" style="text-align:center; padding: 26px">
    <div style="font-size: 6rem; line-height: 1">🧑‍💻</div>
    <div class="huge" style="font-size: 3rem; margin-top: 12px">RAKA</div>
    <div class="muted mono small">Data analyst · 3 bulan kerja</div>
  </div>
  <div class="stack">
    <div class="card">
      <div class="box-h">Kantornya</div>
      <b>Kopi Senja</b>: kedai kopi dengan 3 cabang
      <div class="mt-3 flex gap-2">
        <span class="tag wajib">Jakarta · JKT</span>
        <span class="tag wajib">Bandung · BDG</span>
        <span class="tag wajib">Surabaya · SBY</span>
      </div>
    </div>
    <div class="card">
      <div class="box-h">Bosnya</div>
      <b>Bu Sari</b>, owner. Tiap pagi jam 08.00 nunggu laporan penjualan di WhatsApp.
    </div>
    <div class="card soft">
      <div class="box-h">Orangnya</div>
      Jago Excel, rajin... tapi kerjaannya makin hari makin banyak.
    </div>
  </div>
</div>

<!--
⏱️ 1 menit

"Raka ini sebenernya mirip banyak dari kita: jago Excel, rajin, tapi kerjaannya makin hari makin banyak."
-->

---

<div class="eyebrow">// 📖 Cerita</div>

## Senin pagi Raka

<div class="grid grid-cols-[1.25fr_1fr] gap-8 mt-2">

<div class="stack" style="gap: 8px">
  <div class="flowrow"><span class="tag paham">07.00</span> Download 3 file penjualan dari kasir tiap cabang</div>
  <div class="flowrow"><span class="tag paham">07.15</span> Gabungin di Excel</div>
  <div class="flowrow"><span class="tag paham">07.25</span> Benerin nama menu yang ditulis beda-beda</div>
  <div class="flowrow"><span class="tag paham">07.40</span> Hitung total, rata-rata, cek target</div>
  <div class="flowrow"><span class="tag paham">07.55</span> Ketik ulang laporan di WhatsApp ke Bu Sari</div>
  <div class="flowrow"><span class="tag wajib">08.05</span> <b>Selesai... tiap hari. 😮‍💨</b></div>
</div>

<div>
<div class="box-h">// Data dari 3 kasir</div>

```text
"  es kopi SUSU gula aren "  | 4250000
"ES KOPI SUSU GULA AREN"     | 2875000
"Es Kopi susu Gula Aren   "  | 3520000
```

<div class="mt-6 lead">±<b class="hl">65 menit</b> setiap hari kerja.</div>
</div>

</div>

<!--
⏱️ 1 menit

"Ini terjadi setiap hari kerja." Tunjuk data yang berantakan: nama menu yang sama ditulis 3 cara berbeda. Ini akan jadi masalah di Bab 6.
-->

---

<div class="eyebrow">// 📖 Sampai suatu hari...</div>

## Satu nol nyelip

<div class="chat mt-8" style="max-width: 760px; margin-left: auto; margin-right: auto">
  <div class="bubble me"><small>RAKA · 08.04</small>Omzet Jakarta kemarin <b>Rp12.500.000</b> Bu 🙏</div>
  <div class="bubble them"><small>BU SARI · 08.05</small>WAH 😍 ...eh bentar, kok 10x lipat dari biasanya? 😨</div>
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

# Gimana kalau semuanya selesai dalam <span class="hl">1 detik</span>?

<div class="grid grid-cols-[1fr_1.1fr] gap-10 mt-8 items-center">
  <div>
    <p class="lead">Di akhir kelas, <b>kalian sendiri</b> yang bikin script laporan otomatis buat Raka.</p>
    <p class="muted">Semua materi hari ini = potongan puzzle untuk script itu.</p>
    <div class="mt-6"><Goto to="colab" where="Materi · section 00 · Demo Final" /></div>
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
3. "Ini yang KALIAN sendiri bakal bikin di akhir kelas."
4. Jangan jelaskan kodenya sekarang. Tujuannya bikin penasaran.

➡️ Balik ke slide 7.
-->

---

<div class="eyebrow">// Peta perjalanan</div>

## 8 bab, 8 stempel, 1 kopi gratis

<div class="grid grid-cols-[1.55fr_1fr] gap-8 mt-2">
  <StampCard :done="0" />
  <div class="card pop">
    <div class="box-h">Aturan main</div>
    <ul>
      <li><b>Error itu wajar.</b> Programmer senior pun kena tiap hari.</li>
      <li>Tanya kapan saja, nggak ada pertanyaan bodoh.</li>
      <li>Sinyal: 🟢 aman · 🔴 stuck, tolong</li>
      <li><b>Ketik sendiri</b>, jangan cuma copy-paste.</li>
    </ul>
  </div>
</div>

<div class="mt-6 lead">Hari ini kalian akan <b>kenalan sama Python</b>, <b>nulis & jalanin kode sendiri</b>, dan <b>bikin laporan otomatis</b> buat Kopi Senja.</div>

<!--
⏱️ 1 menit

- Bacakan tujuan versi ramah peserta (teks di bawah).
- "Setiap selesai satu bab, kita cap satu stempel. 8 stempel = kopi gratis: laporan otomatis."
- Lihat footer: kotak kecil di tengah = progres stempel, label kanan = kita lagi di mana (Colab/VSCode/Hands-on).
-->

---
section: Bab 1 · Kenapa Raka Harus Ngoding?
bab: 1
---

<div class="ghostnum">01</div>
<div class="eyebrow">// Bab 1 · Kenapa Raka harus ngoding?</div>

## Masalahnya bukan di Excel-nya

<div class="flowrow mt-6" style="gap: 18px">
  <div class="stack" style="flex: 1.1">
    <div class="node"><div class="t">🧾 Kasir 3 cabang</div><div class="s">3 file, tiap hari</div></div>
    <div class="node"><div class="t">🛵 Aplikasi ojol</div><div class="s">GoFood, GrabFood</div></div>
    <div class="node"><div class="t">📦 Stok gudang</div><div class="s">spreadsheet terpisah</div></div>
    <div class="node"><div class="t">💳 Mutasi bank</div><div class="s">format beda lagi</div></div>
  </div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="node yl" style="flex: 0.8; text-align:center; padding: 24px 14px">
    <div style="font-size: 3rem">🧑‍💻</div>
    <div class="t" style="font-size: 1.2rem">Raka</div>
    <div class="s">sendirian, tiap pagi</div>
  </div>
  <div class="card pop" style="flex: 1.4">
    <div class="huge" style="font-size: 2.3rem">Di dunia data, datanya bukan cuma 1 file Excel.</div>
    <p class="muted mt-3">Datang dari banyak tempat, tiap hari, dengan format beda-beda.</p>
  </div>
</div>

<!--
⏱️ 00:07 · 2 menit

"Excel itu alat yang bagus. Masalahnya, data di dunia nyata datang dari banyak tempat, tiap hari, dengan format beda-beda. Excel nggak didesain buat kerja ulang yang sama tiap pagi."

Tanya: "Di kerjaan/kampus kalian, data datang dari mana aja?" (1–2 jawaban saja)
-->

---

<div class="eyebrow">// Bab 1</div>

## 3 musuh kerja manual

<div class="grid grid-cols-3 gap-6 mt-4">
  <div class="card pop"><div style="font-size:2.2rem">🔁</div><h3 class="mt-2">Repetitif</h3>Kerjaan yang sama, tiap hari.</div>
  <div class="card pop"><div style="font-size:2.2rem">😴</div><h3 class="mt-2">Membosankan</h3>Bikin kita lengah.</div>
  <div class="card err"><div style="font-size:2.2rem">⚠️</div><h3 class="mt-2" style="color: var(--err)">Rawan salah</h3>Typo, rumus ketimpa, angka bisa diubah <b>tanpa jejak</b>.</div>
</div>

<div class="card mt-8 flowrow" style="gap: 20px">
  <div class="box-h" style="margin:0">Hitung bareng</div>
  <div class="mono"><b>65</b> menit × <b>22</b> hari kerja =</div>
  <div v-click class="huge" style="font-size: 2.4rem"><span class="hl">±24 jam/bulan</span></div>
  <div v-after class="muted">= 3 hari kerja penuh, cuma buat copy-paste.</div>
</div>

<!--
⏱️ 2,5 menit

- Minta peserta hitung dulu sebelum klik reveal: 65 × 22 = 1.430 menit ≈ 24 jam ≈ 3 hari kerja.
- "Yang paling bahaya bukan capeknya, tapi SALAHNYA. Proses manual juga susah diaudit: kalau ada angka berubah, siapa yang ngubah? Kapan? Nggak ada jejaknya."
-->

---

<div class="eyebrow">// Bab 1</div>

## Kode itu <span class="hl">resep</span>

<div class="grid grid-cols-[1fr_auto_1fr] gap-6 mt-4 items-center">
  <div class="card"><div class="box-h">Manual</div><div class="huge" style="font-size:3rem">65 menit</div><p class="muted">hasil bisa beda-beda tiap hari</p></div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="card tk"><div class="box-h">Script</div><div class="huge" style="font-size:3rem">1 detik</div><p>hasil selalu sama</p></div>
</div>

<div class="mt-6 lead">Ditulis <b>sekali</b>, dimasak <b>berkali-kali</b>, rasanya <b>selalu sama</b>. <span class="mono small tk">Otomasi · Repetitif → Konsisten</span></div>

<div class="mt-4"><StampCard :done="1" :stamping="1" compact /></div>

<!--
⏱️ 1,5 menit · 🎟️ STEMPEL 1

"Kode itu kayak resep. Ditulis sekali, bisa dimasak berkali-kali, rasanya selalu sama. Kalau Raka nulis resep laporannya dalam bentuk kode, besok pagi tinggal 'masak' ulang."

➡️ Transisi: "Oke, Raka mau ngoding. Tapi pakai BAHASA apa?"
-->

---
section: Bab 2 · Kenalan sama Python
bab: 2
---

<div class="ghostnum">02</div>
<div class="eyebrow">// Bab 2 · Kenalan sama Python <span class="tag kenalan">kenalan</span></div>

## Bahasa buat ngobrol sama komputer

<div class="flowrow mt-4" style="gap: 8px">
  <div class="node"><div class="t">0101</div><div class="s">bahasa mesin</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">Assembly</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">C</div></div>
  <div class="arw">›</div>
  <div class="node"><div class="t">Java, PHP</div></div>
  <div class="arw">›</div>
  <div class="node tk"><div class="t">Python</div></div>
</div>
<div class="flex justify-between mono small mt-2" style="max-width: 760px"><span>◀ LOW LEVEL · dekat ke mesin</span><span>dekat ke manusia · HIGH LEVEL ▶</span></div>

<div class="grid grid-cols-2 gap-6 mt-6">
  <div class="card">
    <div class="box-h">☕ Low level</div>
    "Ambil 18 gram biji, giling ukuran 3, tekan tamper 15 kg, seduh 9 bar selama 25 detik, tuang susu 150 ml suhu 65°..."
  </div>
  <div class="card pop">
    <div class="box-h">☕ High level</div>
    <span style="font-size: 1.3rem; font-weight: 700">"Mas, es kopi susu satu, gulanya dikit ya."</span>
  </div>
</div>

<!--
⏱️ 00:13 · 1,5 menit

"Hasilnya sama-sama kopi. Bedanya: siapa yang mikirin detailnya. Di bahasa high level, detail ribetnya diurus oleh bahasanya."
-->

---

<div class="eyebrow">// Bab 2</div>

## Sama-sama bilang "Halo"

<div class="grid grid-cols-2 gap-x-6 gap-y-1 code-sm">
<div>
<div class="box-h">Bahasa mesin (ilustrasi)</div>

```text
10110000 01100001 11001101 00100001 ...
```

<div class="box-h mt-3">Assembly</div>

```text
mov edx, len
mov ecx, msg
mov ebx, 1
mov eax, 4
int 0x80
```

</div>
<div>
<div class="box-h">Java</div>

```java
public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, Kopi Senja!");
    }
}
```

<div class="box-h mt-3">Python</div>
<div class="code-lg code-yl">

```python
print("Halo, Kopi Senja!")
```

</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Java juga high level, tapi lihat bedanya. Python satu baris. Itu yang dimaksud simple syntax."
-->

---

<div class="eyebrow">// Bab 2</div>

## Dirancang untuk mudah <span class="hl">dibaca</span>

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2 items-start">
<div>

```python
menu_tersedia = ["kopi susu", "americano", "latte"]
pesanan = "latte"

if pesanan in menu_tersedia:
    print("Siap, pesanan dibuat!")
else:
    print("Maaf, menu habis.")
```

</div>
<div class="stack">
  <div class="card pop-yl">
    <div class="box-h">Coba tebak</div>
    Kalian <b>belum belajar</b> Python sama sekali. Program ini ngapain?
  </div>
  <div v-click class="card tk">
    <div class="box-h">Readability counts</div>
    Bisa nebak, kan? Python memang didesain supaya kodenya gampang dibaca <b>manusia</b>.
  </div>
</div>
</div>

<!--
⏱️ 1,5 menit

- Tunggu 2–3 jawaban, baru klik.
- `if` sengaja dipakai sebagai teaser (dipelajari pertemuan berikutnya). Jangan jelaskan sintaksnya.
- "Readability counts" adalah salah satu baris Zen of Python (`import this`).
-->

---

<div class="eyebrow">// Bab 2 <span class="tag paham">paham</span></div>

## Interpreted vs Compiled

<table>
  <thead><tr><th></th><th>Interpreted · Python</th><th>Compiled · C, C++, Java, C#</th></tr></thead>
  <tbody>
    <tr><td><b>Cara kerja</b></td><td>Dibaca & dijalankan <b>baris per baris</b></td><td>Seluruh kode <b>dibungkus</b> jadi bahasa mesin dulu, baru jalan</td></tr>
    <tr><td><b>Analogi</b></td><td>☕ Barista meracik sambil baca resep</td><td>🥫 Pabrik kopi kaleng: produksi dulu, baru diminum</td></tr>
    <tr><td><b>Error ketahuan</b></td><td>Saat baris itu dijalankan. Baris sebelumnya <b>sudah jalan</b></td><td>Saat compile, <b>sebelum</b> program jalan sama sekali</td></tr>
    <tr><td><b>Kelebihan</b></td><td>Cepat dicoba, cocok eksplorasi data</td><td>Eksekusi lebih cepat</td></tr>
    <tr><td><b>Kekurangan</b></td><td>Eksekusi relatif lebih lambat</td><td>Tiap ubah kode harus compile ulang</td></tr>
  </tbody>
</table>

<!--
⏱️ 2 menit

"Barista baca resep langkah demi langkah. Kalau di langkah ke-3 susunya habis, langkah 1 & 2 udah terjadi. Pabrik kopi kaleng: resep diproses semua dulu. Kalau salah, ketahuan sebelum produksi, tapi tiap ganti resep harus produksi ulang."

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

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2 items-start">
<Predict :options="['0 baris', '2 baris', '4 baris']" :answer="1" note="baris 1–2 jalan, baris 3 error, baris 4 nggak pernah dijalankan">

```python
print("1. Download data Jakarta... beres")
print("2. Download data Bandung... beres")
prnt("3. Download data Surabaya...")
print("4. Kirim laporan ke Bu Sari")
```

</Predict>
<div class="stack">
  <div class="card soft"><div class="box-h">Pertanyaan</div>Ada typo di baris 3. <b>Berapa baris</b> yang tercetak?</div>
  <Goto to="colab" where="Materi · Bab 3 · Halo Kopi Senja" />
  <div v-click="2" class="code-sm code-err">

```text
1. Download data Jakarta... beres
2. Download data Bandung... beres
NameError: name 'prnt' is not defined
```

  </div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 3 · Halo Kopi Senja" (peserta nonton saja)

- Tanya tebakan dulu, klik untuk reveal, lalu jalankan di Colab.
- Jangan bahas cara baca error dulu: itu di slide 23 saat peserta mengalaminya sendiri.
-->

---

<div class="eyebrow">// Bab 2 <span class="tag kenalan">kenalan</span></div>

## General purpose: satu bahasa, banyak dapur

<div class="grid grid-cols-5 gap-4 mt-4">
  <div class="card pop"><div style="font-size:2rem">📊</div><h3 class="mt-2">Data</h3><span class="small">pandas · numpy · matplotlib</span></div>
  <div class="card"><div style="font-size:2rem">🤖</div><h3 class="mt-2">AI / ML</h3><span class="small">scikit-learn · PyTorch</span></div>
  <div class="card"><div style="font-size:2rem">🌐</div><h3 class="mt-2">Web</h3><span class="small">Django · Flask · FastAPI</span></div>
  <div class="card"><div style="font-size:2rem">🎮</div><h3 class="mt-2">Game</h3><span class="small">pygame</span></div>
  <div class="card pop-yl"><div style="font-size:2rem">⚙️</div><h3 class="mt-2">Otomasi</h3><span class="small">openpyxl (Excel!) · requests</span></div>
</div>

<div class="story mt-10">
<b>Library</b> = bahan setengah jadi. Kopi Senja nggak bikin sirup gula aren dari tebu, tinggal beli yang udah jadi. Raka nanti pakai <code>pandas</code> buat baca file kasir (pertemuan berikutnya).
</div>

<!--
⏱️ 1 menit

"Mau baca Excel nggak perlu bikin dari nol, tinggal pakai library."
-->

---

<div class="eyebrow">// Bab 2</div>

## Gratis, komunitasnya besar, jagoan di data

<div class="grid grid-cols-3 gap-6 mt-2">
  <div class="card pop"><div style="font-size:2rem">🆓</div><h3 class="mt-2">Free & open source</h3>Gratis, kodenya terbuka untuk semua.</div>
  <div class="card pop"><div style="font-size:2rem">👥</div><h3 class="mt-2">Komunitas besar</h3><b>PythonID</b> (Telegram/FB) & <b>PyCon ID</b> tiap tahun.</div>
  <div class="card pop"><div style="font-size:2rem">🏆</div><h3 class="mt-2">Nomor 1 di data</h3>Konsisten di peringkat atas bahasa terpopuler dunia.</div>
</div>

<blockquote class="mt-6">
<b>Python</b> = bahasa high-level, mudah dibaca, interpreted, serbaguna, gratis, dan jagoan di dunia data.
</blockquote>

<div class="mt-3"><StampCard :done="2" :stamping="2" compact /></div>

<!--
⏱️ 1 menit · 🎟️ STEMPEL 2

"Komunitas besar artinya kalau kalian error, 99% kemungkinan sudah ada orang lain yang pernah kena dan nanya duluan di internet."

Kalau mau sebut angka peringkat, cek data terbaru (TIOBE / IEEE Spectrum / Stack Overflow Survey).

➡️ "Bahasanya udah kepilih. Sekarang, Raka ngodingnya DI MANA?"
-->

---
section: Bab 3 · Nyiapin Meja Kerja
bab: 3
---

<div class="ghostnum">03</div>
<div class="eyebrow">// Bab 3 · Nyiapin meja kerja <span class="tag paham">paham</span></div>

## Development environment = dapur

<div class="lead mt-2" style="max-width: 760px">Tempat kita <b>menulis</b>, <b>menjalankan</b>, dan <b>mengembangkan</b> aplikasi. Dapurnya tergantung mau masak apa.</div>

<div class="grid grid-cols-2 gap-8 mt-8">
  <div class="card">
    <div class="box-h">🌐 Bikin web</div>
    <div class="huge" style="font-size: 1.7rem">VSCode · Cursor · PhpStorm</div>
  </div>
  <div class="card pop">
    <div class="box-h">📊 Ngolah data</div>
    <div class="huge" style="font-size: 1.7rem">VSCode · Cursor · <span class="hl">Notebook</span></div>
  </div>
</div>

<!--
⏱️ 00:23 · 1,5 menit

"Barista butuh dapur. Programmer butuh dev environment."
-->

---

<div class="eyebrow">// Bab 3</div>

## Isi dapur Python

<table>
  <thead><tr><th>Komponen</th><th>Fungsinya</th><th>Analogi dapur</th><th>Level</th></tr></thead>
  <tbody>
    <tr><td><b>Python interpreter</b></td><td>Yang benar-benar menjalankan kode</td><td>☕ Barista / mesin kopi</td><td><span class="tag paham">paham</span></td></tr>
    <tr><td><b>Code editor</b></td><td>Tempat menulis kode</td><td>📒 Meja racik + buku resep</td><td><span class="tag paham">paham</span></td></tr>
    <tr><td><b>Package manager</b> <code>pip</code> <code>uv</code></td><td>Download & install library</td><td>🚚 Supplier bahan</td><td><span class="tag kenalan">kenalan</span></td></tr>
    <tr><td><b>Virtual environment</b></td><td>Ruang terpisah per proyek, biar versi library nggak bentrok</td><td>🍳 Dapur terpisah per menu</td><td><span class="tag kenalan">kenalan</span></td></tr>
  </tbody>
</table>

<div class="mt-6 lead">Hari ini cukup ingat dua yang pertama. Kabar baiknya: di <b>Google Colab</b> semuanya udah disiapin. 🎉</div>

<!--
⏱️ 2 menit

Package manager & virtual env akan kepakai nanti waktu mulai pakai library.
-->

---

<div class="eyebrow">// Bab 3</div>

## 3 gaya meja kerja

<table>
  <thead><tr><th>Gaya</th><th>Contoh</th><th>Analogi</th><th>Cocok untuk</th></tr></thead>
  <tbody>
    <tr><td><b>Text editor + terminal</b></td><td>Notepad++ + terminal</td><td>Dapur minimalis</td><td>Script kecil, server</td></tr>
    <tr><td><b>IDE</b></td><td>VSCode, PyCharm</td><td>Dapur produksi lengkap</td><td>Aplikasi & script yang dipakai rutin</td></tr>
    <tr><td><b>Notebook</b></td><td>Jupyter, <b>Google Colab</b>, Marimo</td><td><span class="hl">Test kitchen</span>: coba satu-satu, langsung cicip</td><td>Belajar, eksplorasi & analisis data</td></tr>
  </tbody>
</table>

<div class="card pop-yl mt-8">
<div class="box-h">Notebook</div>
Kode dipotong-potong per <b>cell</b>. Tiap cell bisa dijalankan sendiri dan hasilnya langsung kelihatan di bawahnya.
</div>

<!--
⏱️ 2 menit

"Notebook itu kayak dapur uji coba: cocok banget buat belajar dan eksplorasi data."
-->

---

<div class="eyebrow">// Bab 3</div>

## Hari ini pakai yang mana?

<div class="grid grid-cols-2 gap-8 mt-4">
  <div class="card pop" style="padding: 22px">
    <div style="font-size: 3rem">🧪</div>
    <div class="huge mt-2" style="font-size: 2.2rem">Google Colab</div>
    <p class="lead mt-2">Tempat <b>belajar & coba-coba</b>. Nggak perlu install apa pun.</p>
    <span class="sticker tk">dipakai sepanjang kelas</span>
  </div>
  <div class="card" style="padding: 22px">
    <div style="font-size: 3rem">💻</div>
    <div class="huge mt-2" style="font-size: 2.2rem">VSCode</div>
    <p class="lead mt-2">Tempat script <b>"beneran"</b> yang dijalankan rutin tiap pagi.</p>
    <span class="sticker r">tujuan akhir Raka</span>
  </div>
</div>

<div class="mt-8 flex items-center gap-6">
  <span class="lead">Saatnya pegang kode!</span>
  <Goto to="hands-on" where="Hands-on 1 · Halo, Kopi Senja!" />
</div>

<!--
⏱️ 1,5 menit

"Sepanjang kelas kita pakai Colab. Di akhir kelas, kita pindahin hasilnya ke VSCode, karena itulah yang nanti dijalankan Raka tiap pagi."

Kenapa semua pakai Colab: nol instalasi = nol waktu terbuang buat troubleshooting setup; beban kognitif fokus ke Python, bukan tools.
-->

---
mode: hands-on
where: Latihan · Bab 3
---

<div class="eyebrow">// Hands-on 1 · Halo, Kopi Senja!</div>

## Meja kerja pertamamu

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-2">
<div>
<ol>
  <li>Buka notebook latihan (link di kanan / di chat)</li>
  <li><b>File → Save a copy in Drive</b></li>
  <li>Ganti nama: <code>KopiSenja_NamaKamu</code></li>
  <li>Scroll ke section <b>Bab 3 · Halo Kopi Senja</b></li>
  <li>Ketik di code cell, lalu tekan <span class="kbd">Shift</span> + <span class="kbd">Enter</span></li>
  <li>Ganti tulisannya jadi namamu, jalankan lagi</li>
  <li><b>+ Text</b> → tulis: <i>Catatan kelas Python pertamaku ☕</i></li>
  <li>Kasih sinyal 🟢 berhasil · 🔴 stuck</li>
</ol>
</div>
<div class="stack">
  <Goto to="hands-on" where="Buka 02_latihan_peserta di Colab" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
  <div class="code-lg">

```python
print("Halo, Kopi Senja!")
```

  </div>
  <div class="card soft small">
    <b>Cell</b> = kotak kode. Angka <code>[1]</code> di kiri = urutan cell dijalankan. Run pertama agak lama karena Colab lagi nyiapin "dapur" (runtime).
  </div>
</div>
</div>

<!--
⏱️ 00:30 · 6 menit · 🎯 HANDS-ON (share screen Colab, kerjakan bareng langkah demi langkah)

- Lupa tanda kutip → NameError; kurung tidak ditutup → SyntaxError. Bagus! Pakai sebagai bahan slide 23.
- Bonus buat yang cepat: `import this`.
-->

---
mode: hands-on
where: Latihan · Bab 3
---

<div class="eyebrow">// Hands-on 1</div>

## Error pertamamu (dan cara bacanya)

<div class="grid grid-cols-[1.1fr_1fr] gap-8 mt-2">
<div>
<p>Jalankan cell <b>"Tebak dulu, baru jalankan"</b> di notebook latihan. Tebak dulu berapa baris yang tercetak!</p>
<div class="code-sm code-err">

```text
NameError          Traceback (most recent call last)
Cell In[2], line 3
      1 print("1. Download data Jakarta... beres")
      2 print("2. Download data Bandung... beres")
----> 3 prnt("3. Download data Surabaya...")

NameError: name 'prnt' is not defined
```

</div>
</div>
<div class="stack">
  <div class="card pop"><span class="num" style="font-size:1.6rem">1</span> 👇 <b>Baca baris paling bawah dulu</b>: jenis error + pesannya</div>
  <div class="card pop"><span class="num" style="font-size:1.6rem">2</span> 🔍 <b>Cari nomor baris / panah</b> <code>----></code></div>
  <div class="card pop"><span class="num" style="font-size:1.6rem">3</span> 🤔 <b>Bandingkan dengan maksudmu</b>: typo? kutip? kurung?</div>
  <div class="card yl small"><b>📕 Kamus Error #1 · NameError</b> = "Aku nggak kenal nama ini."</div>
</div>
</div>

<!--
⏱️ 2,5 menit

"Pesan error itu bukan marah-marah, tapi PETUNJUK. Python sering bahkan kasih saran, misalnya 'Did you mean: print?'."

Mulai papan "Kamus Error": NameError = typo, lupa kutip, atau cell yang membuat variabelnya belum dijalankan.
-->

---
mode: vscode
where: kopi-senja/laporan.py
---

<div class="eyebrow">// Hands-on 1 · Demo</div>

## Dapur produksi: VSCode

<div class="grid grid-cols-[1fr_1fr] gap-8 mt-2">
<div>
<ol>
  <li><b>File → Open Folder</b> → <code>kopi-senja</code></li>
  <li>File baru: <code>laporan.py</code></li>
  <li>Ketik kodenya → <b>simpan</b> <span class="kbd">Cmd/Ctrl</span> + <span class="kbd">S</span></li>
  <li>Klik ▶ <b>Run Python File</b>, atau lewat terminal:</li>
</ol>

```bash
python3 laporan.py    # Mac/Linux
python laporan.py     # Windows
```

</div>
<div class="stack">
  <Goto to="vscode" where="demo trainer, peserta yang sudah install boleh ikut" />
  <div class="card pop-yl">
    <div class="box-h">Bedanya sama Colab</div>
    Ini <b>file</b> <code>.py</code>: resep yang tersimpan rapi. Bisa dijalankan kapan saja tanpa browser, bahkan dijadwalkan tiap jam 7 pagi.
  </div>
  <div class="sticker tk" style="align-self: flex-start">kita balik ke sini di akhir kelas</div>
</div>
</div>

<!--
⏱️ 2,5 menit · 💻 PINDAH KE VSCODE

- Tombol ▶ tidak muncul → cek extension Python & interpreter terpilih (pojok kanan bawah).
- Peserta yang belum install: kirim panduan setup untuk dikerjakan di rumah.
-->

---

<div class="eyebrow">// Hands-on 1</div>

## Colab vs VSCode

<table>
  <thead><tr><th></th><th>🧪 Colab (notebook)</th><th>💻 VSCode (file .py)</th></tr></thead>
  <tbody>
    <tr><td><b>Analogi</b></td><td>Test kitchen</td><td>Dapur produksi</td></tr>
    <tr><td><b>Cara jalan</b></td><td>Per cell, <span class="kbd">Shift</span>+<span class="kbd">Enter</span></td><td>Seluruh file sekaligus</td></tr>
    <tr><td><b>Dipakai untuk</b></td><td>Belajar, eksplorasi, analisis</td><td>Script rutin, aplikasi</td></tr>
  </tbody>
</table>

<div class="card pop-yl mt-5">
<div class="box-h">💡 Tips penting notebook</div>
Variabel "nggak dikenal" padahal sudah ditulis? Biasanya <b>cell-nya belum di-run</b>. Solusi pamungkas: <b>Runtime → Run all</b>.
</div>

<div class="mt-4"><StampCard :done="3" :stamping="3" compact /></div>

<!--
⏱️ 1 menit · 🎟️ STEMPEL 3

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

## Langkah pertama Raka: catatan

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-4 items-start">
<div>

```python
# Laporan harian Kopi Senja
# Dibuat oleh: Raka
print("Laporan dimulai")  # komentar di ujung baris
# print("baris ini nggak dijalankan")
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Komentar <code>#</code></div>Catatan untuk <b>manusia</b>. Dilewati Python.</div>
  <div class="card"><div class="box-h">Dipakai untuk</div><ol><li>Menjelaskan <b>kenapa</b> kode ditulis begitu</li><li>"Mematikan" kode sementara</li></ol></div>
  <div class="card soft small">Shortcut: <span class="kbd">Cmd</span> + <span class="kbd">/</span> (Mac) · <span class="kbd">Ctrl</span> + <span class="kbd">/</span> (Windows)</div>
</div>
</div>

<!--
⏱️ 00:42 · 1,5 menit · 🧪 COLAB → materi, section "Bab 4 · Toples Berlabel"

Ketik live, jangan paste.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## <code>print()</code> dan konsep function

<div class="flowrow mt-2" style="gap: 14px">
  <div class="node"><div class="t">"Halo"</div><div class="s">bahan = argumen</div></div>
  <div class="arw">➜</div>
  <div class="node tk" style="padding: 14px 22px"><div class="t" style="font-size:1.3rem">☕ print( )</div><div class="s">mesin = function</div></div>
  <div class="arw">➜</div>
  <div class="node"><div class="t">Halo</div><div class="s">hasil tampil di layar</div></div>
  <div class="card soft small" style="margin-left: 12px; flex: 1"><b>Built-in function</b> = mesin bawaan Python: <code>print</code>, <code>type</code>, <code>len</code>, <code>max</code>, <code>round</code>, <code>input</code>...</div>
</div>

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-start">
<div>

```python
print("Laporan Kopi Senja")
print(3)
print("Jumlah cabang:", 3)  # dipisah koma
print()                     # baris kosong
print(Kopi)                 # ❌ lupa kutip
```

</div>
<div class="stack">
  <div class="card pop-yl">Baris terakhir bakal jalan nggak? 🤔</div>
  <div v-click class="card yl"><b>NameError</b>: teks wajib pakai kutip. Tanpa kutip, Python mengira <code>Kopi</code> itu nama sesuatu.</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Teks pakai tanda kutip, angka tidak. Tanpa kutip, Python mengira Kopi itu nama sesuatu, dan dia nggak kenal → NameError, teman lama kita."
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
  <div class="card pop mt-5 flowrow" style="gap: 14px">
    <code style="font-size:1.1rem">nama = nilai</code>
    <span><b><span class="hl">=</span> artinya MASUKKAN KE</b>, bukan "sama dengan". Baca dari <b>kanan ke kiri</b>.</span>
  </div>
</div>
<Predict :options="['10', '12', 'Error']" :answer="1" note="ambil isi, kurangi 3, tambah 5, masukkan lagi">

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

Ketik di Colab: nama_toko, jumlah_cabang, omzet_jakarta, lalu print.

"Di matematika x = x + 1 itu mustahil. Di Python normal: ambil isi toples, tambah 1, masukin lagi."

Miskonsepsi `=` sebagai "sama dengan" sangat umum. Tekankan sekarang karena di Bab 5 muncul `==`.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Isi toples bisa diganti

<div class="grid grid-cols-2 gap-8 mt-2">
<div>
<div class="box-h">☕ Java: tipe ditulis & dikunci</div>

```java
int omzetJakarta = 4250000;
omzetJakarta = "empat juta"; // ❌ error
```

<div class="box-h mt-4">🐍 Python: tipe "ditebak" dari isinya</div>

```python
omzet_jakarta = 4250000
print(type(omzet_jakarta))  # <class 'int'>

omzet_jakarta = "empat juta"  # ✅ boleh, tapi
print(type(omzet_jakarta))  # <class 'str'>
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Nama sama = ditimpa</div>Isi toples diganti, <b>isi lama hilang</b>.</div>
  <div class="card pop"><div class="box-h">Dynamic typing</div>Python menebak tipe dari isinya. Fleksibel, tapi <b>jangan ganti-ganti tipe</b> di satu variabel.</div>
  <div class="card soft"><div class="box-h"><code>type()</code></div>Built-in function buat ngecek isi toples itu jenisnya apa.</div>
</div>
</div>

<!--
⏱️ 1,5 menit
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Aturan wajib kasih label

<table class="dense">
  <thead><tr><th>Aturan</th><th>❌ Salah</th><th>✅ Benar</th><th>Error-nya</th></tr></thead>
  <tbody>
    <tr><td>Tidak boleh diawali angka</td><td><code>2cabang = 3</code></td><td><code>cabang2 = 3</code></td><td>SyntaxError: invalid decimal literal</td></tr>
    <tr><td>Tidak boleh pakai spasi</td><td><code>omzet bandung = 875000</code></td><td><code>omzet_bandung</code></td><td>SyntaxError: invalid syntax</td></tr>
    <tr><td>Hanya huruf, angka, <code>_</code></td><td><code>omzet-surabaya = 3520000</code></td><td><code>omzet_surabaya</code></td><td>SyntaxError: cannot assign to expression here</td></tr>
    <tr><td>Bukan <i>keyword</i> Python</td><td><code>class = "A"</code></td><td><code>kelas = "A"</code></td><td>SyntaxError: invalid syntax</td></tr>
    <tr><td><i>Case sensitive</i></td><td><code>Total</code> ≠ <code>total</code></td><td>konsisten</td><td>NameError kalau salah huruf</td></tr>
  </tbody>
</table>

<div class="grid grid-cols-[1fr_1fr] gap-6 mt-5 items-center">
<div class="code-sm">

```python
import keyword
print(keyword.kwlist)  # kata yang "dipesan"
```

</div>
<div class="card yl small"><b>📕 Kamus Error #2 · SyntaxError</b> = "Tata bahasanya salah." Python menolak menjalankan cell sama sekali.</div>
</div>

<!--
⏱️ 1,5 menit

"Kenapa omzet-surabaya salah? Tanda - dibaca Python sebagai PENGURANGAN: 'omzet dikurangi surabaya'."
Keyword = kata yang udah dipesan Python: if, for, class, True, dll.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Jebakan: boleh, tapi bikin celaka

<div class="story">Raka pernah bikin variabel <code>max</code> buat nyimpen omzet tertinggi. 10 menit kemudian...</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
max = 4250000        # omzet tertinggi
print(max)           # 4250000 (normal)

print(max(3, 7, 5))  # ❌ TypeError: 'int'
                     #  object is not callable
```

</div>
<div>

```python
del max              # hapus variabel kita
print(max(3, 7, 5))  # ✅ 7, mesin asli kembali
```

<div class="card pop-yl mt-4 small">
Hindari nama <code>max</code> <code>min</code> <code>sum</code> <code>list</code> <code>str</code> <code>print</code> <code>type</code> <code>input</code>. Kalau nama variabelmu <b>berubah warna</b> di editor → ganti namanya.
</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Nama function bawaan BUKAN keyword, jadi Python mengizinkan. Tapi mesin max aslinya ketimpa angka. Toples dikasih label 'mesin kopi', mesinnya jadi hilang."
"del dipakai menghapus variabel. Setelah dihapus, kalau dipanggil lagi → NameError."
-->

---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Konvensi: biar rapi & dimengerti orang lain

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-2 items-start">
<table>
  <thead><tr><th>Jenis</th><th>Gaya (PEP 8)</th><th>Contoh</th></tr></thead>
  <tbody>
    <tr><td>Variabel</td><td><code>snake_case</code></td><td><code>omzet_jakarta</code></td></tr>
    <tr><td>Konstanta</td><td><code>UPPER_CASE</code></td><td><code>TARGET_HARIAN = 10_000_000</code></td></tr>
    <tr><td>Class (nanti)</td><td><code>PascalCase</code></td><td><code>LaporanHarian</code></td></tr>
  </tbody>
</table>
<div class="stack">
  <div class="card err"><div class="box-h" style="color: var(--err)">Nama jelek</div><code>x</code> <code>a1</code> <code>data2</code> <code>tmp</code></div>
  <div class="card pop"><div class="box-h">Nama bagus</div><code>omzet_jakarta</code> <code>trx_bandung</code></div>
</div>
</div>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="card soft"><b>Aturan</b> (slide sebelumnya) = <b>wajib</b>. Dilanggar → error.</div>
  <div class="card soft"><b>Konvensi</b> = <b>kesepakatan</b>. Nggak error, tapi kode lebih sering <b>dibaca</b> daripada ditulis.</div>
</div>

<!--
⏱️ 1 menit

"Konvensi bikin kode gampang dibaca orang lain, termasuk diri kalian sendiri 3 bulan lagi."
-->

---
mode: hands-on
where: Latihan · Bab 4
---

<div class="eyebrow">// Bab 4 · Latihan</div>

## 🎯 Latihan Bab 4

<div class="grid grid-cols-[1.15fr_1fr] gap-8">
<div>
<ol class="small">
  <li>Buat variabel: nama toko, namamu, jumlah cabang</li>
  <li>Buat variabel omzet & transaksi tiap cabang:<br>
    <span class="mono tiny">JKT 4250000 / 170 · BDG 2875000 / 125 · SBY 3520000 / 160</span></li>
  <li>Buat <b>konstanta</b> target harian: <code>10000000</code></li>
  <li>Print semuanya, cek tipenya pakai <code>type()</code></li>
</ol>
</div>
<div>
<div class="box-h">🕵️ Pojok Error: tebak, error atau tidak?</div>
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
<div v-click class="answer small mt-1">❌ baris 2 & 3 SyntaxError · baris 6 NameError</div>
</div>
</div>

<div class="mt-4"><StampCard :done="4" :stamping="4" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 4 · Toples Berlabel" · 🎟️ STEMPEL 4

- Di notebook latihan, Pojok Error sudah dipisah satu cell per baris: tebak dulu, baru jalankan satu per satu.
- Variabel dari latihan ini dipakai lagi di Bab 5 (data kit juga tersedia di section Bab 5).

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
  <thead><tr><th>Kategori</th><th>Tipe</th><th>Contoh di Kopi Senja</th><th>Analogi bahan</th><th>Dibahas</th></tr></thead>
  <tbody>
    <tr><td>Numeric</td><td><code>int</code></td><td><code>170</code> transaksi</td><td>biji kopi, dihitung per butir</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td></td><td><code>float</code></td><td><code>23395.6</code> rata-rata</td><td>susu, ditakar</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td></td><td><code>complex</code></td><td><code>3+4j</code></td><td>–</td><td>Bab 5 <span class="tag kenalan">kenalan</span></td></tr>
    <tr><td>Boolean</td><td><code>bool</code></td><td><code>True</code> target tercapai</td><td>lampu BUKA/TUTUP</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Text</td><td><code>str</code></td><td><code>"Es Kopi Susu"</code></td><td>label menu</td><td>Bab 6 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Sequence</td><td><code>list</code> <code>tuple</code></td><td>daftar omzet, jam buka</td><td>antrean, jam di pintu</td><td>Bab 7 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Set</td><td><code>set</code> <code>frozenset</code></td><td>menu unik</td><td>jenis menu terjual</td><td>Bab 7 <span class="tag paham">paham</span></td></tr>
    <tr><td>Mapping</td><td><code>dict</code></td><td>harga per menu</td><td>papan menu</td><td>Bab 7 <span class="tag wajib">wajib</span></td></tr>
  </tbody>
</table>

<!--
⏱️ 00:57 · 1 menit (advance organizer)

"Ini peta semua jenis 'bahan' di Python. Kita kunjungi satu-satu."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Angka: <code>int</code>, <code>float</code>, <code>complex</code>

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-2 items-start">
<div>

```python
trx_jakarta = 170          # int  : bilangan bulat
rata_rata = 23395.6        # float: desimal (TITIK)
omzet_jakarta = 4_250_000  # underscore boleh

print(type(trx_jakarta), type(rata_rata))
# <class 'int'> <class 'float'>

z = 3 + 4j                 # complex: kenalan aja
print(type(z))             # <class 'complex'>
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Desimal = titik</div><code>23.5</code> ✅ &nbsp; <code>23,5</code> ❌</div>
  <div class="card pop"><div class="box-h">Underscore</div><code>4_250_000</code> sama persis dengan <code>4250000</code></div>
  <div class="card soft small"><b>Tips:</b> uang Rupiah simpan sebagai <code>int</code>. (Kenapa? Coba <code>0.1 + 0.2</code> 😉)</div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 5 · Ngitung Omzet" (jalankan data kit dulu)

0.1 + 0.2 = 0.30000000000000004 → lihat FAQ trainer.
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Operator: kalkulator Raka

<div class="grid grid-cols-[1.45fr_1fr] gap-8 items-start">
<table class="dense">
  <thead><tr><th>Op</th><th>Arti</th><th>Contoh Kopi Senja</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td><code>+</code></td><td>tambah</td><td><code>omzet_jakarta + omzet_bandung</code></td><td><code>7125000</code></td></tr>
    <tr><td><code>-</code></td><td>kurang</td><td><code>omzet_jakarta - omzet_bandung</code></td><td><code>1375000</code></td></tr>
    <tr><td><code>*</code></td><td>kali</td><td><code>25000 * 170</code> harga × cup</td><td><code>4250000</code></td></tr>
    <tr><td><code>/</code></td><td>bagi, <b>selalu float</b></td><td><code>4250000 / 170</code></td><td><code>25000.0</code></td></tr>
    <tr><td><code>//</code></td><td>bagi, bulat ke bawah</td><td><code>455 // 50</code> kardus penuh</td><td><code>9</code></td></tr>
    <tr><td><code>%</code></td><td>sisa bagi</td><td><code>455 % 50</code> sisa cup</td><td><code>5</code></td></tr>
    <tr><td><code>**</code></td><td>pangkat</td><td><code>1.1 ** 3</code></td><td><code>1.331...</code></td></tr>
  </tbody>
</table>
<div class="stack">
  <Predict :options="['5', '5.0']" :answer="1" note="/ selalu menghasilkan float">

```python
print(10 / 2)
```

  </Predict>
  <div class="card pop small"><b>Urutan:</b> <code>**</code> → <code>* / // %</code> → <code>+ -</code>. Ragu? Pakai <b>kurung</b>.</div>
</div>
</div>

<!--
⏱️ 3 menit · ketik di Colab, tanya hasil sebelum run

- total_omzet = omzet_jakarta + omzet_bandung + omzet_surabaya → 10645000
- "// dan % itu pasangan: // dapat berapa kardus penuh, % sisanya berapa."
- Pertumbuhan: omzet_jakarta * 1.1 ** 3 → 5656750.000000002 (lalu round)
- % tidak ada di outline asli, tapi sangat sering dipakai dan berpasangan dengan //.
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Built-in function untuk angka

<div class="code-sm">

```python
print(abs(omzet_bandung - omzet_jakarta))                 # 1375000 (selisih tanpa minus)
print(round(23395.6043))                                  # 23396
print(round(23395.6043, 1))                               # 23395.6
print(max(omzet_jakarta, omzet_bandung, omzet_surabaya))  # 4250000
print(min(omzet_jakarta, omzet_bandung, omzet_surabaya))  # 2875000
print(int(3.99))                                          # 3 ← dipotong, BUKAN dibulatkan!
print(float(170))                                         # 170.0
```

</div>

<div class="grid grid-cols-[1fr_1.2fr] gap-6 mt-4 items-stretch">
  <div class="card pop-yl"><div class="box-h">🎣 Cara mancing sendiri</div>
    <code>round?</code> di Colab / Jupyter · <code>help(round)</code> di mana saja
  </div>
  <div class="card tk"><b>Nggak perlu hafal</b> semua function. Yang penting tahu cara <b>nyari</b>: <code>?</code>, <code>help()</code>, Google, AI.</div>
</div>

<!--
⏱️ 2 menit

Sebelum int(3.99): "3 atau 4?"
"Programmer profesional pun buka dokumentasi tiap hari."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Boolean: lampu <span class="hl-tk">BUKA</span> / <span class="hl">TUTUP</span>

<div class="grid grid-cols-[1fr_1.3fr] gap-8 mt-2 items-start">
<div class="stack">
  <div class="card pop"><div class="box-h">Cuma 2 nilai</div><span class="huge" style="font-size:2rem">True · False</span><div class="small muted mt-1">huruf depan <b>kapital</b>!</div></div>
  <table class="dense">
    <thead><tr><th>Perbandingan</th><th>Arti</th></tr></thead>
    <tbody>
      <tr><td><code>==</code> &nbsp; <code>!=</code></td><td>sama / tidak sama</td></tr>
      <tr><td><code>&gt;</code> &nbsp; <code>&lt;</code></td><td>lebih besar / kecil</td></tr>
      <tr><td><code>&gt;=</code> &nbsp; <code>&lt;=</code></td><td>... atau sama dengan</td></tr>
    </tbody>
  </table>
</div>
<div>

```python
print(omzet_jakarta > omzet_surabaya)  # True
print(total_omzet >= TARGET_HARIAN)    # True ← tercapai!
print(trx_bandung != 125)              # False
print(type(True))                      # <class 'bool'>

print(true)                            # ❌ NameError
```

<div class="card yl mt-4"><b><code>=</code> memasukkan ke toples. <code>==</code> bertanya "apakah sama?"</b> Sumber error nomor satu pemula.</div>
</div>
</div>

<!--
⏱️ 2,5 menit

"true huruf kecil → NameError. Python cuma kenal True dan False."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag paham">paham</span></div>

## Gabungin kondisi: <code>and</code>, <code>or</code>, <code>not</code>

<div class="grid grid-cols-[1fr_1.6fr] gap-8 mt-2 items-start">
<table>
  <thead><tr><th>Operator</th><th>True kalau...</th></tr></thead>
  <tbody>
    <tr><td><code>and</code></td><td><b>dua-duanya</b> True</td></tr>
    <tr><td><code>or</code></td><td><b>salah satu</b> True</td></tr>
    <tr><td><code>not</code></td><td>membalik True ↔ False</td></tr>
  </tbody>
</table>
<div>

```python
# Target tercapai DAN Bandung di atas 3 juta?  → False
print(total_omzet >= TARGET_HARIAN and omzet_bandung > 3_000_000)

# Target tercapai ATAU Bandung di atas 3 juta?  → True
print(total_omzet >= TARGET_HARIAN or omzet_bandung > 3_000_000)

print(not True)  # False
```

</div>
</div>

<div class="story mt-8">Sekarang boolean cuma jawab benar/salah. Pertemuan berikutnya, boolean jadi <b>otak</b> program: <i>"kalau target nggak tercapai, kirim peringatan ke Bu Sari"</i> pakai <code>if</code>.</div>

<!--
⏱️ 1 menit

Teaser: `if` = kode yang tadi kalian tebak di slide 13.
-->

---
mode: hands-on
where: Latihan · Bab 5
---

<div class="eyebrow">// Bab 5 · Latihan</div>

## 🎯 Latihan Bab 5

<div class="grid grid-cols-[1.25fr_1fr] gap-8">
<div>
<p class="small muted">Jalankan cell data kit dulu, lalu kerjakan satu cell per soal.</p>
<ol class="small">
  <li>Total omzet 3 cabang</li>
  <li>Total transaksi 3 cabang</li>
  <li>Rata-rata omzet per transaksi, dibulatkan</li>
  <li>Selisih omzet tertinggi & terendah (<code>max</code>, <code>min</code>)</li>
  <li>Target harian tercapai? (<code>True</code>/<code>False</code>)</li>
  <li><span class="tag paham">bonus</span> Berapa persen capaian target?</li>
  <li><span class="tag wajib">tantangan</span> Kardus isi 50 cup: butuh berapa kardus penuh, sisa berapa?</li>
</ol>
</div>
<div class="stack">
  <Predict :options="['3.5 0', '3 1', '3 0.5']" :answer="1">

```python
print(7 // 2, 7 % 2)
```

  </Predict>
  <div v-click="2" class="card soft small mono">Kunci: 10645000 · 455 · 23396 · 1375000 · True · 106.45 · 9 kardus sisa 5</div>
</div>
</div>

<div class="mt-3"><StampCard :done="5" :stamping="5" compact /></div>

<!--
⏱️ 4 menit · 🎯 HANDS-ON → latihan, section "Bab 5 · Ngitung Omzet" · 🎟️ STEMPEL 5

Setelah latihan: tebak output 7 // 2, 7 % 2 (angkat 1/2/3 jari).

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
    <div class="box-h">🧩 Teka-teki sambil istirahat</div>

```python
print("10" + "5")
print(10 + 5)
```

  <div class="card pop-yl">Kenapa hasilnya <b>beda</b>? Jawabannya setelah istirahat. 😉</div>
  </div>
</div>

<!--
⏱️ 01:12 – 01:22 · ISTIRAHAT

- Klik timer untuk mulai. Dobel klik = reset.
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

## Tiga kasir, tiga gaya nulis

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2 items-start">
<div class="stack">
  <div class="card"><div class="box-h">Kasir Jakarta</div><code>"  es kopi SUSU gula aren "</code></div>
  <div class="card"><div class="box-h">Kasir Bandung</div><code>"ES KOPI SUSU GULA AREN"</code></div>
  <div class="card"><div class="box-h">Kasir Surabaya</div><code>"Es Kopi susu Gula Aren   "</code></div>
</div>
<div class="stack">
  <div class="card pop-yl">Buat manusia: menu yang <b>sama</b>.<br>Buat komputer: <b>tiga menu berbeda</b>.</div>

```python
print(menu_kasir_jkt == menu_kasir_bdg)
# False 😱
```

  <div v-click class="card tk small">Jawaban teka-teki: <code>"10" + "5"</code> = teks digabung → <code>"105"</code>. Di akhir bab ini, <code>False</code> tadi jadi <code>True</code>.</div>
</div>
</div>

<!--
⏱️ 01:22 · 1,5 menit · 🧪 COLAB → materi, section "Bab 6 · Beresin Nama Menu" (jalankan data kit teks)
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## String: untaian karakter

<div class="grid grid-cols-[1.4fr_1fr] gap-8 mt-2 items-start">
<div>

```python
nama_toko = "Kopi Senja"         # kutip dua
slogan = 'Seduh rasa, pulang'    # kutip satu, sama saja
alamat = """Jl. Senja No. 7
Jakarta Selatan"""               # kutip tiga: banyak baris

print("Kopi" + " " + "Senja")    # gabung → Kopi Senja
print("=" * 30)                  # ulang 30 kali
print(len(nama_toko))            # 10 (spasi dihitung)
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h"><code>+</code> gabung</div><code>"Kopi" + "Senja"</code> → <code>"KopiSenja"</code></div>
  <div class="card pop"><div class="box-h"><code>*</code> ulang</div><code>"=" * 30</code> → garis pemisah laporan!</div>
  <div class="card soft small">Kutip satu atau dua <b>sama saja</b>, yang penting konsisten.</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"'=' * 30 ini nanti kita pakai buat garis di laporan Bu Sari."
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 2
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Indexing: setiap karakter punya nomor

<div class="mt-2"><IndexStrip text="TRX-20261005-JKT-0170" :sels="['[0]', '[-1]']" /></div>

<div class="grid grid-cols-[1fr_1fr] gap-8 mt-5 items-start">
<div class="code-sm">

```python
kode_trx = "TRX-20261005-JKT-0170"
print(kode_trx[0])    # T ← mulai dari 0!
print(kode_trx[-1])   # 0 ← minus = dari belakang
print(len(kode_trx))  # 21
print(kode_trx[21])   # ❌ IndexError
```

</div>
<div class="stack">
  <div class="card soft small">Struktur: <code>TRX</code> - <code>tanggal</code> - <code>kode cabang</code> - <code>nomor urut</code></div>
  <div class="card pop small">Kenapa mulai dari 0? Anggap index = <b>jarak dari awal</b>.</div>
  <div class="card yl small"><b>📕 Kamus Error · IndexError</b> = "Nomor urutnya kelewatan."</div>
</div>
</div>

<!--
⏱️ 2 menit

- Klik → sorot kode_trx[0], klik lagi → kode_trx[-1].
- Sebelum kode_trx[21]: "Panjangnya 21, index terakhir berapa?" (20, bukan 21).
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 5
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Slicing: motong teks <code>[start:stop]</code>

<div class="mt-1"><IndexStrip text="TRX-20261005-JKT-0170" :sels="['[0:3]', '[4:12]', '[4:8]', '[13:16]', '[-4:]']" /></div>

<div class="grid grid-cols-3 gap-5 mt-6">
  <div class="card pop"><div class="box-h">Aturan</div>Ambil dari <b>start</b>, sampai <b>sebelum</b> stop.</div>
  <div class="card pop"><div class="box-h">🔪 Mental model</div>Pisau memotong <b>di antara</b> karakter. Angka = posisi pisau.</div>
  <div class="card pop-yl"><div class="box-h">Kosong</div><code>[:3]</code> dari awal · <code>[-4:]</code> sampai akhir</div>
</div>

<!--
⏱️ 2,5 menit

- Tiap klik menyorot satu slice: [0:3] TRX, [4:12] tanggal, [4:8] tahun, [13:16] JKT, [-4:] 0170.
- Sebelum klik ke-3: "Ambilkan tahunnya saja, index berapa sampai berapa?"
- "Kenapa stop nggak ikut? Biar gampang ngitung: [4:12] panjangnya pasti 12 - 4 = 8 karakter."
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 3
---

<div class="eyebrow">// Bab 6 <span class="tag paham">paham</span></div>

## Slicing dengan langkah <code>[start:stop:step]</code>

<div class="mt-2"><IndexStrip text="0123456789" name="angka" :neg="false" :sels="['[::2]', '[1::2]', '[::-1]']" /></div>

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-6 items-start">
<div>

```python
angka = "0123456789"
print(angka[::2])      # 02468 → loncat 2 (genap)
print(angka[1::2])     # 13579 → mulai index 1, loncat 2
print(kode_trx[::-1])  # 0710-TKJ-50016202-XRT → dibalik!
```

</div>
<div class="card soft"><code>[::-1]</code> = trik terkenal buat membalik teks. Step jarang dipakai sehari-hari, cukup tahu cara bacanya.</div>
</div>

<!--
⏱️ 1 menit
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## String itu <span class="hl">immutable</span>

<div class="lead mt-2">Tidak bisa diubah sebagian. Kayak tulisan yang dicetak di gelas: mau ganti, <b>cetak gelas baru</b>.</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
kode_trx[0] = "X"
# ❌ TypeError: 'str' object does not
#    support item assignment
```

</div>
<div>

```python
kode_baru = kode_trx.replace("JKT", "BDG")
print(kode_baru)  # TRX-20261005-BDG-0170 (BARU)
print(kode_trx)   # TRX-20261005-JKT-0170 (tetap)
```

</div>
</div>

<div class="card yl mt-6 small"><b>📕 Kamus Error · TypeError</b> = "Tipe datanya nggak cocok untuk operasi ini."</div>

<!--
⏱️ 1,5 menit
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## String method: alat beres-beres teks

<div class="grid grid-cols-[1fr_1.15fr] gap-6 items-start">
<table class="dense">
  <thead><tr><th>Method</th><th>Contoh → hasil</th></tr></thead>
  <tbody>
    <tr><td><code>.strip()</code></td><td><code>"  latte  "</code> → <code>"latte"</code></td></tr>
    <tr><td><code>.upper()</code> <code>.lower()</code></td><td><code>"Latte"</code> → <code>"LATTE"</code></td></tr>
    <tr><td><code>.title()</code></td><td><code>"es kopi"</code> → <code>"Es Kopi"</code></td></tr>
    <tr><td><code>.replace(a, b)</code></td><td><code>"JKT"</code> → <code>"BKT"</code></td></tr>
    <tr><td><code>.split("-")</code></td><td>→ <code>['TRX', '20261005', ...]</code></td></tr>
  </tbody>
</table>
<div>
<div class="code-sm">

```python
bersih_jkt = menu_kasir_jkt.strip().title()
bersih_bdg = menu_kasir_bdg.strip().title()
print(bersih_jkt)  # Es Kopi Susu Gula Aren
print(bersih_jkt == bersih_bdg)  # True 🎉
```

</div>
<div class="small muted mt-2">Lainnya: <code>.count()</code> <code>.startswith()</code> <code>.center()</code> · ketik <code>menu.</code> lalu <span class="kbd">Tab</span></div>
</div>
</div>

<div class="mt-3">
<Predict :options="['[LATTE]', '[  LATTE  ]', '[  latte  ]']" :answer="2" note="method mengembalikan string BARU, aslinya tetap">

```python
menu = "  latte  "; menu.upper(); print("[" + menu + "]")
```

</Predict>
</div>

<!--
⏱️ 3 menit · momen "aha" bab ini

- Tunjukkan bersih_jkt == bersih_bdg → True.
- Jebakan: "Ingat, string immutable. Method TIDAK mengubah aslinya. Kalau mau disimpan: menu = menu.upper()."
- .split() menghasilkan LIST → jembatan ke Bab 7: "Kurung siku ini namanya list."
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Casting: ganti jenis bahan

<div class="grid grid-cols-[1.4fr_1fr] gap-8 mt-2 items-start">
<div>

```python
nomor = kode_trx[-4:]
print(nomor, type(nomor))  # 0170 <class 'str'>

nomor_int = int(nomor)     # nol di depan hilang
print(nomor_int, type(nomor_int))  # 170 <class 'int'>

print(str(170) + " transaksi")  # angka → teks
print(float("23.5"))            # 23.5
print(int("17O"))               # ❌ ValueError (huruf O!)
```

</div>
<div class="stack">
  <div class="card pop">Data dari file atau input sering datang sebagai <b>teks</b>, walaupun isinya angka.</div>
  <div class="card soft small">Kasir kadang ngetik huruf <b>O</b>, bukan angka <b>0</b>.</div>
  <div class="card yl small"><b>📕 Kamus Error · ValueError</b> = "Tipenya benar, nilainya nggak masuk akal."</div>
</div>
</div>

<!--
⏱️ 1,5 menit
-->

---
mode: hands-on
where: Latihan · Bab 6
---

<div class="eyebrow">// Bab 6 · Latihan</div>

## 🎯 Latihan Bab 6

<div class="grid grid-cols-[1fr_1fr] gap-6">
<div>
<p class="small muted">Jalankan data kit teks dulu, <b>jangan diketik ulang</b> biar spasinya tetap berantakan.</p>
<ol class="small">
  <li>Bersihkan ketiga nama menu → <code>"Es Kopi Susu Gula Aren"</code></li>
  <li>Buktikan ketiganya sama (pakai <code>==</code> dan <code>and</code>)</li>
  <li>Dari <code>kode_trx</code>: tanggal, kode cabang, nomor</li>
  <li>Ubah nomor transaksi jadi angka <code>170</code></li>
  <li><span class="tag paham">bonus</span> Tanggal jadi <code>"05-10-2026"</code> (slicing + <code>+</code>)</li>
  <li><span class="tag wajib">tantangan</span> Ada berapa huruf "a" di nama menu bersih?</li>
</ol>
</div>
<div v-click class="code-xs">
<div class="box-h">Kunci</div>

```python
bersih_jkt = menu_kasir_jkt.strip().title()
bersih_bdg = menu_kasir_bdg.strip().title()
bersih_sby = menu_kasir_sby.strip().title()
print(bersih_jkt == bersih_bdg
      and bersih_bdg == bersih_sby)     # True
print(kode_trx[4:12], kode_trx[13:16])  # 20261005 JKT
print(int(kode_trx[-4:]))               # 170
print(kode_trx[10:12] + "-" + kode_trx[8:10]
      + "-" + kode_trx[4:8])            # 05-10-2026
print(bersih_jkt.lower().count("a"))    # 2
```

</div>
</div>

<div class="mt-3"><StampCard :done="6" :stamping="6" compact /></div>

<!--
⏱️ 5,5 menit · 🎯 HANDS-ON → latihan, section "Bab 6 · Beresin Nama Menu" · 🎟️ STEMPEL 6

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

## "Kalau cabangnya 30?" → <code>list</code>

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-1 items-start">
<div class="code-sm">

```python
cabang = ["Jakarta", "Bandung", "Surabaya"]
omzet  = [4_250_000, 2_875_000, 3_520_000]

print(omzet[0])     # 4250000 ← SAMA kayak string!
print(omzet[-1])    # 3520000
print(cabang[0:2])  # ['Jakarta', 'Bandung']

print(len(omzet), sum(omzet))       # 3 10645000
print(max(omzet), min(omzet))       # 4250000 2875000
print(sorted(omzet, reverse=True))  # terbesar dulu

omzet[1] = 2_900_000         # koreksi: list BISA diubah
cabang.append("Yogyakarta")  # buka cabang baru
```

</div>
<div class="stack">
  <div class="story small">30 cabang = 30 variabel omzet + 30 variabel transaksi? 😵</div>
  <div class="card pop"><div class="box-h">List = antrean pesanan</div>Urut, bisa ditambah, bisa diubah.</div>
  <div class="card pop-yl small">Ilmu indexing string <b>dipakai lagi</b>. Bedanya: string <b>immutable</b>, list <b>mutable</b>.</div>
</div>
</div>

<!--
⏱️ 01:42 · 3,5 menit · 🧪 COLAB → materi, section "Bab 7 · Wadah Banyak Barang"

- Sebelum omzet[0]: "Kalian udah tahu caranya dari Bab 6. Tebak?"
- "sum() di list ini andalan Raka: 30 cabang pun tetap satu baris."
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag paham">paham</span></div>

## <code>tuple</code>: data yang dikunci

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-4 items-start">
<div>

```python
JAM_OPERASIONAL = (7, 22)   # buka 7, tutup 22
LOKASI_JKT = (-6.2, 106.8)  # koordinat

print(JAM_OPERASIONAL[0])   # 7
JAM_OPERASIONAL[0] = 8      # ❌ TypeError: 'tuple'
                            #    object does not support
                            #    item assignment
```

</div>
<div class="stack">
  <div class="card pop"><div style="font-size: 2.2rem">🔒</div>Kayak list yang <b>dikunci</b>. Pakai kurung biasa <code>( )</code>.</div>
  <div class="card soft">Cocok buat data yang memang <b>nggak boleh berubah</b>: jam buka di pintu, koordinat.</div>
</div>
</div>

<!--
⏱️ 1 menit
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag paham">paham</span></div>

## <code>set</code>: hanya yang unik

<div class="grid grid-cols-[1.45fr_1fr] gap-8 mt-4 items-start">
<div>

```python
menu_terjual = ["kopi susu", "latte", "kopi susu",
                "americano", "latte"]
menu_unik = set(menu_terjual)
print(menu_unik)       # {'latte', 'kopi susu', 'americano'}
print(len(menu_unik))  # 3 jenis menu terjual

menu_tetap = frozenset(["kopi susu", "latte"])  # dikunci
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Set</div>Otomatis <b>buang duplikat</b>, <b>tanpa urutan</b> (nggak bisa pakai index).</div>
  <div class="card soft small"><span class="tag kenalan">kenalan</span> <b>frozenset</b> = set yang nggak bisa diubah. Cukup tahu.</div>
</div>
</div>

<!--
⏱️ 1,5 menit

Urutan print set bisa beda-beda tiap dijalankan, itu normal.
-->

---
mode: colab-demo
where: Materi · Bab 7
---

<div class="eyebrow">// Bab 7 <span class="tag wajib">wajib</span></div>

## <code>dict</code>: papan menu

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-1 items-start">
<div class="code-sm">

```python
harga = {
    "kopi susu": 25000,
    "latte": 28000,
    "americano": 22000,
}
print(harga["latte"])           # 28000 ← akses pakai KUNCI
harga["matcha latte"] = 30000   # tambah menu baru

print(harga["teh tarik"])       # ❌ KeyError: 'teh tarik'

omzet_cabang = {"Jakarta": 4_250_000, "Bandung": 2_875_000,
                "Surabaya": 3_520_000}
print(sum(omzet_cabang.values()))   # 10645000
```

</div>
<div class="stack">
  <div class="card pop-yl">
    <div class="box-h">📋 Papan menu</div>
    <div class="mono small">kopi susu ........ 25.000<br>latte ............ 28.000<br>americano ........ 22.000</div>
  </div>
  <div class="card pop small">List: cari pakai <b>nomor urut</b>. Dict: cari pakai <b>nama</b>. Kita nggak bilang "menu nomor 2", tapi "latte berapa?"</div>
  <div class="card yl small"><b>📕 Kamus Error · KeyError</b> = "Kunci ini nggak ada di dict."</div>
</div>
</div>

<!--
⏱️ 2 menit
-->

---

<div class="eyebrow">// Bab 7</div>

## Pilih wadah yang tepat

<table class="dense">
  <thead><tr><th>Wadah</th><th>Tanda</th><th>Urut?</th><th>Bisa diubah?</th><th>Duplikat?</th><th>Analogi</th></tr></thead>
  <tbody>
    <tr><td><code>list</code></td><td><code>[ ]</code></td><td>✅</td><td>✅</td><td>✅</td><td>Antrean pesanan</td></tr>
    <tr><td><code>tuple</code></td><td><code>( )</code></td><td>✅</td><td>❌</td><td>✅</td><td>Jam buka di pintu</td></tr>
    <tr><td><code>set</code></td><td><code>{ }</code></td><td>❌</td><td>✅</td><td>❌</td><td>Jenis menu terjual</td></tr>
    <tr><td><code>dict</code></td><td><code>{k: v}</code></td><td>✅</td><td>✅</td><td>kunci ❌</td><td>Papan menu</td></tr>
  </tbody>
</table>

<div class="grid grid-cols-4 gap-4 mt-4 small">
  <div class="card flex justify-between items-center gap-2">Transaksi hari ini, urut waktu<span v-click class="answer">list</span></div>
  <div class="card flex justify-between items-center gap-2">Koordinat cabang<span v-click class="answer">tuple</span></div>
  <div class="card flex justify-between items-center gap-2">Pelanggan unik<span v-click class="answer">set</span></div>
  <div class="card flex justify-between items-center gap-2">Stok per nama bahan<span v-click class="answer">dict</span></div>
</div>

<div class="mt-4"><StampCard :done="7" :stamping="7" compact /></div>

<!--
⏱️ 2 menit · kuis cepat, jawab serentak / di chat · 🎟️ STEMPEL 7

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

## <code>print()</code> lebih jauh & escape character

<div class="grid grid-cols-[1fr_1.5fr] gap-8 mt-2 items-start">
<table>
  <thead><tr><th>Escape</th><th>Arti</th></tr></thead>
  <tbody>
    <tr><td><code>\n</code></td><td>baris baru</td></tr>
    <tr><td><code>\t</code></td><td>tab (rata kolom)</td></tr>
    <tr><td><code>\"</code> <code>\'</code></td><td>kutip di dalam teks</td></tr>
    <tr><td><code>\\</code></td><td>garis miring terbalik</td></tr>
  </tbody>
</table>
<div>

```python
print("Jakarta", "Bandung", "Surabaya", sep=" | ")
print("Laporan \"Kopi Senja\"\nTanggal:\t05-10-2026")
```

<div class="code-yl">

```text
Jakarta | Bandung | Surabaya
Laporan "Kopi Senja"
Tanggal:	05-10-2026
```

</div>
</div>
</div>

<!--
⏱️ 01:52 · 2 menit · 🧪 COLAB → materi, section "Bab 8 · Laporan buat Bu Sari"

Jebakan klasik (ceritakan saja): print("C:\data\new") → \n jadi baris baru. Solusi: "C:\\data\\new" atau raw string r"C:\data\new".
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8</div>

## Raka mencoba bikin laporan...

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-center">
<div class="code-lg code-err">

```python
total_omzet = 10645000
print("Total omzet: " + total_omzet)
```

</div>
<div class="card err">
<div class="box-h" style="color: var(--err)">TypeError</div>
<code>can only concatenate str (not "int") to str</code>
</div>
</div>

<div class="story mt-10">Teks + angka = nggak bisa. Kayak nyampur gula sama tulisan "gula". Ternyata Python punya beberapa solusi dari zaman ke zaman...</div>

<!--
⏱️ 1 menit
-->

---

<div class="eyebrow">// Bab 8 <span class="tag wajib">f-string wajib</span> <span class="tag kenalan">% & .format kenalan</span></div>

## Evolusi string formatting

```python
print("Total omzet: " + str(total_omzet))      # 1. casting manual  → ribet
print("Total omzet: %d" % total_omzet)         # 2. gaya %  (jadul)
print("Total omzet: {}".format(total_omzet))   # 3. .format()
print(f"Total omzet: {total_omzet}")           # 4. f-string ⭐ pakai ini!
```

<div class="grid grid-cols-[1fr_1.3fr] gap-8 mt-6 items-center">
  <div class="card soft">Semua hasilnya sama: <code>Total omzet: 10645000</code></div>
  <div class="card pop-yl">Kenali cara 2 & 3 karena masih sering muncul di kode orang. Tapi kalau nulis sendiri: <b>f-string</b>. Huruf <code>f</code> di depan kutip, variabel di dalam <code>{ }</code>.</div>
</div>

<!--
⏱️ 2 menit
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8 <span class="tag wajib">wajib</span></div>

## Kekuatan super f-string

<div class="grid grid-cols-[1fr_1.35fr] gap-6 mt-1 items-start">
<table class="dense">
  <thead><tr><th>Format</th><th>Contoh</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td>Variabel</td><td><code>f"{nama_toko}"</code></td><td>Kopi Senja</td></tr>
    <tr><td>Hitungan</td><td><code>f"{total_omzet / 455}"</code></td><td>23395.60...</td></tr>
    <tr><td>Ribuan</td><td><code>f"{total_omzet:,}"</code></td><td>10,645,000</td></tr>
    <tr><td>2 desimal</td><td><code>f"{106.4512:.2f}"</code></td><td>106.45</td></tr>
    <tr><td>Method</td><td><code>f"{nama_toko.upper()}"</code></td><td>KOPI SENJA</td></tr>
  </tbody>
</table>
<div class="code-sm">

```python
persen_target = total_omzet / TARGET_HARIAN * 100

print(f"Total omzet : Rp{total_omzet:,}")
# Rp10,645,000  (gaya Inggris)
print(f"Total omzet : Rp{total_omzet:,}".replace(",", "."))
# Rp10.645.000  (gaya Indonesia!)
print(f"Capaian     : {persen_target:.2f}%")    # 106.45%
print(f"Tercapai?   : {total_omzet >= TARGET_HARIAN}")
```

</div>
</div>

<div class="card pop-yl mt-4">Trik <code>.replace(",", ".")</code> itu <b>string method dari Bab 6</b>. Semua mulai nyambung! 🧩</div>

<!--
⏱️ 3 menit
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8 <span class="tag wajib">wajib</span></div>

## <code>input()</code>: biar laporannya bisa diisi

<div class="grid grid-cols-[1fr_1.15fr] gap-8 mt-1 items-start">
<div class="stack">

```python
nama_analis = input("Nama analis: ")
print(f"Laporan disusun oleh {nama_analis}")
```

<div class="card soft small">Di Colab muncul kotak isian, cell "berputar" sampai kamu tekan <span class="kbd">Enter</span>. Bukan hang!</div>
<div v-click="2">
<div class="box-h">Perbaikan: casting dari Bab 6</div>

```python
trx = int(input("Jumlah transaksi: "))
print(trx * 2)    # 20
```

</div>
</div>
<Predict :options="['20', '1010', 'Error']" :answer="1" note="input() SELALU menghasilkan string">

```python
trx = input("Jumlah transaksi: ")   # ketik: 10
print(trx * 2)
```

</Predict>
</div>

<!--
⏱️ 2,5 menit · momen paling berkesan, JANGAN dilewati

"input() selalu menghasilkan string, apa pun yang diketik. '10' * 2 = teks diulang 2 kali. Sama kayak teka-teki sebelum istirahat."
-->

---
mode: hands-on
where: Latihan · Bab 8
---

<div class="eyebrow">// Bab 8 · Latihan</div>

## 🎯 Latihan Bab 8

<div class="grid grid-cols-[1.1fr_1fr] gap-8">
<div>
<ol class="small">
  <li>Minta nama analis lewat <code>input()</code>, rapikan pakai <code>.strip().title()</code></li>
  <li>Cetak header seperti di kanan</li>
  <li>Cetak total omzet format Rupiah: <code>Rp10.645.000</code></li>
  <li><span class="tag paham">bonus</span> Minta target lewat <code>input()</code>, hitung persen capaian</li>
</ol>
</div>
<div class="stack">
<div class="code-yl">

```text
========================================
LAPORAN HARIAN KOPI SENJA
Analis : Raka Pratama
========================================
Total omzet : Rp10.645.000
```

</div>
<div class="sticker tk" style="align-self: flex-start">8/8 stempel → saatnya tukar kopi gratis!</div>
</div>
</div>

<div class="mt-4"><StampCard :done="8" :stamping="8" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 8 · Laporan buat Bu Sari" · 🎟️ STEMPEL 8

Kunci ada di 03_kunci_jawaban.ipynb.

➡️ "8 stempel penuh. Saatnya tukar dengan kopi gratis: LAPORAN OTOMATIS RAKA."
-->

---
section: Final · Satu Klik, Laporan Jadi
bab: 9
---

<div class="eyebrow">// Final · Satu klik, laporan jadi</div>

## Misi: Laporan Harian Kopi Senja v1.0

<div class="grid grid-cols-[1.15fr_1fr] gap-8 items-start">
<div class="code-xs">

```text
============================================
         LAPORAN HARIAN KOPI SENJA
============================================
Tanggal          : 05-10-2026
Analis           : Raka Pratama
--------------------------------------------
Omzet per cabang
  Jakarta    : Rp4.250.000 (170 trx)
  Bandung    : Rp2.875.000 (125 trx)
  Surabaya   : Rp3.520.000 (160 trx)
--------------------------------------------
Total omzet      : Rp10.645.000
Total transaksi  : 455
Rata-rata/trx    : Rp23.396
Menu terlaris    : Es Kopi Susu Gula Aren
...
Capaian          : 106.45%
Target tercapai? : True
============================================
```

</div>
<div class="stack">
  <div class="card tk"><div class="box-h">🟢 Wajib</div>Isi semua <code>___</code> di template sampai laporan tampil.</div>
  <div class="card yl"><div class="box-h">🟡 Bonus</div>Tambah baris "Cabang terbaik: Jakarta"<br><span class="small">hint: <code>cabang[omzet.index(max(omzet))]</code></span></div>
  <div class="card"><div class="box-h">🔴 Tantangan</div>Omzet tiap cabang juga diminta lewat <code>input()</code>.</div>
</div>
</div>

<!--
⏱️ 02:07 · 2 menit

"Perhatikan: tiap baris laporan ini pakai sesuatu yang kalian pelajari hari ini. Coba tebak, baris 'Menu terlaris' pakai ilmu dari bab berapa?" (Bab 6)
-->

---
mode: hands-on
where: Latihan · Final
---

<div class="eyebrow">// Final</div>

## 🎯 Kerjakan!

<div class="grid grid-cols-[1fr_1.1fr] gap-8 mt-2">
<div class="stack">
  <Goto to="hands-on" where="Latihan · section Final · Laporan Harian v1.0" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
  <div class="card soft small">Masih ada <code>___</code>? Python bakal protes <code>NameError: name '___' is not defined</code>, artinya masih ada yang belum diisi.</div>
  <div><Countdown :minutes="10" small /></div>
</div>
<div>
<div class="box-h">🪜 Tangga petunjuk kalau stuck</div>
<div class="stack" style="gap: 10px">
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">1</span> Cek komentar <code>[Bab X]</code> di template</div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">2</span> Scroll ke latihan bab itu di notebook-mu</div>
  <div class="card pop flowrow"><span class="num" style="font-size:1.6rem">3</span> Tanya teman sebelah (boleh pair programming)</div>
  <div class="card pop-yl flowrow"><span class="num" style="font-size:1.6rem">4</span> Angkat sinyal 🔴, trainer datang</div>
</div>
</div>
</div>

<!--
⏱️ 10 menit · 🎯 HANDS-ON → latihan, section "Final · Laporan Harian v1.0"

- Keliling / buka breakout room. Prioritaskan peserta 🔴.
- Yang selesai cepat → 🟡/🔴, atau jadi "asisten" teman sebelah.
- Menit ke-8: "2 menit lagi".
-->

---
mode: vscode
where: kopi-senja/laporan.py
---

<div class="eyebrow">// Final · Momen "aha"</div>

## Dari notebook ke script

<div class="grid grid-cols-[1fr_1.1fr] gap-10 mt-4 items-center">
<div>

```bash
cd kopi-senja
python3 laporan.py
```

<div class="mt-6"><Goto to="vscode" where="buka kopi-senja/laporan.py, jalankan" /></div>
</div>
<div class="stack">
  <div class="flowrow" style="gap: 16px">
    <div class="huge" style="font-size: 3.4rem; text-decoration: line-through; text-decoration-thickness: 6px; text-decoration-color: var(--err)">65 mnt</div>
    <div class="arw" style="font-size: 2.6rem">➜</div>
    <div class="huge" style="font-size: 3.4rem"><span class="hl-tk">1 dtk</span></div>
  </div>
  <div class="card pop-yl lead" style="color: var(--fg)">Nggak ada lagi salah ketik nol. Laporan sama rapinya setiap hari. Dan yang nulis kodenya... <b>kalian</b>.</div>
</div>
</div>

<!--
⏱️ 3 menit · 💻 PINDAH KE VSCODE → kopi-senja/laporan.py (sudah disiapkan)

- Jalankan, isi nama & tanggal → laporan muncul.
- "Ini yang sekarang dijalankan Raka tiap pagi. Satu perintah."
- Show & tell: 1–2 peserta share screen hasil mereka (terutama yang mengerjakan bonus). Beri apresiasi.
-->

---
section: Epilog · Bersambung...
bab: 10
---

<div class="eyebrow">// Epilog · Isi kotak perkakas Raka</div>

## Yang kalian kuasai hari ini

<table class="dense">
  <thead><tr><th>Masalah Raka</th><th>Alat yang dipakai</th><th>Bab</th></tr></thead>
  <tbody>
    <tr><td>Angka berserakan</td><td>Variabel & konstanta</td><td>4</td></tr>
    <tr><td>Hitung total, rata-rata, selisih</td><td>Operator, <code>sum</code> <code>max</code> <code>min</code> <code>round</code></td><td>5 · 7</td></tr>
    <tr><td>Cek target</td><td>Boolean & perbandingan</td><td>5</td></tr>
    <tr><td>Nama menu berantakan</td><td><code>.strip()</code> <code>.title()</code></td><td>6</td></tr>
    <tr><td>Ambil info dari kode transaksi</td><td>Indexing, slicing, <code>int()</code></td><td>6</td></tr>
    <tr><td>Data banyak cabang</td><td><code>list</code>, <code>dict</code></td><td>7</td></tr>
    <tr><td>Laporan rapi & bisa diisi</td><td>f-string, <code>\t</code>, <code>"=" * 44</code>, <code>input()</code></td><td>8</td></tr>
    <tr><td>Error</td><td>Baca dari baris <b>paling bawah</b></td><td>semua</td></tr>
  </tbody>
</table>

<div class="mt-5 lead">Dari semua ini, mana yang paling bikin kalian <b class="hl">"ooh!"</b>?</div>

<!--
⏱️ 02:22 · 2 menit · tanya 1–2 jawaban
-->

---

<div class="eyebrow">// 📖 Tapi...</div>

## Raka masih punya masalah

<div class="grid grid-cols-2 gap-5 mt-2">
  <div class="card pop"><div class="box-h">😐 "Data omzetnya masih diketik manual di kode."</div><b>→ Baca file Excel/CSV</b> pakai pandas</div>
  <div class="card pop-yl"><div class="box-h">🚨 "Kalau target nggak tercapai, kasih peringatan!"</div><b>→ <code>if</code> / <code>else</code></b>: boolean tadi jadi otaknya</div>
  <div class="card pop"><div class="box-h">🔁 "30 cabang = 30 baris print?"</div><b>→ Loop</b> <code>for</code></div>
  <div class="card pop-yl"><div class="box-h">♻️ "Pengen bikin mesin sendiri kayak print()."</div><b>→ Function</b> buatan sendiri</div>
</div>

<div class="mt-8 flex items-center gap-6">
  <div class="huge" style="font-size: 3rem">Bersambung...</div>
  <span class="sticker">☕ pertemuan berikutnya</span>
</div>

<!--
⏱️ 2 menit

"Kalian sendiri ngerasain kan waktu nulis 3 baris print per cabang di final project? Bayangin 30."
Sesuaikan kartu dengan silabus pertemuan berikutnya.
-->

---

<div class="eyebrow">// Epilog</div>

## Latihan mandiri: mulai dari mana?

<div class="grid grid-cols-[1.45fr_1fr] gap-6 items-start">
<table class="dense">
  <thead><tr><th>#</th><th>Platform</th><th>Kenapa</th></tr></thead>
  <tbody>
    <tr><td>1</td><td><a href="https://codesaya.com/python" target="_blank">Codesaya</a></td><td>Bahasa Indonesia, interaktif, ramah pemula</td></tr>
    <tr><td>2</td><td><a href="https://www.kaggle.com/learn/python" target="_blank">Kaggle Learn: Python</a></td><td>Gratis, berbasis notebook, orientasi data</td></tr>
    <tr><td>3</td><td><a href="https://www.hackerrank.com/domains/python" target="_blank">HackerRank</a></td><td>Introduction, Basic Data Types, Strings</td></tr>
    <tr><td>4</td><td><a href="https://leetcode.com" target="_blank">LeetCode</a></td><td><b>Nanti dulu</b>, setelah paham <code>if</code>, loop, function</td></tr>
  </tbody>
</table>
<div class="card pop-yl small">
<div class="box-h">📝 PR (disarankan)</div>
<ol>
  <li>Baris "Cabang terbaik" & "Cabang terlemah"</li>
  <li>% kontribusi Jakarta ke total (2 desimal)</li>
  <li>Tambah cabang ke-4: Yogyakarta, Rp1.980.000, 88 trx. <b>Rasakan</b> berapa baris yang harus diubah. 😉</li>
</ol>
</div>
</div>

<!--
⏱️ 2 menit

PR nomor 3 sengaja bikin peserta MERASAKAN sakitnya tanpa loop → motivasi alami materi berikutnya.
-->

---

<div class="eyebrow">// Epilog</div>

## Exit ticket 3-2-1

<div class="grid grid-cols-3 gap-6 mt-8">
  <div class="card pop" style="text-align:center; padding: 26px"><div class="huge">3</div><p class="lead mt-3">hal yang aku <b>pelajari</b> hari ini</p></div>
  <div class="card pop-yl" style="text-align:center; padding: 26px"><div class="huge">2</div><p class="lead mt-3">hal yang masih bikin <b>bingung</b></p></div>
  <div class="card pop" style="text-align:center; padding: 26px"><div class="huge">1</div><p class="lead mt-3">pertanyaan yang masih ingin <b>ditanyakan</b></p></div>
</div>

<div class="mt-8 center-x muted">Isi lewat form yang dibagikan di chat ✍️</div>

<!--
⏱️ 1 menit

Baca jawaban "2 hal bingung" sebelum pertemuan berikutnya → buka dengan review 5 menit soal topik yang paling sering muncul.
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
    <a href="https://github.com/thosangs/python_lecture" target="_blank">📦 Repo: notebook, script, slide</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/01_materi_kopi_senja.ipynb" target="_blank">📓 Materi lengkap (Colab)</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/03_kunci_jawaban.ipynb" target="_blank">🔑 Kunci jawaban (Colab)</a>
    <span>👥 Komunitas: PythonID · PyCon ID</span>
  </div>
</div>

<div class="lead mt-6">Error akan terus datang. Itu tanda kalian <b>sedang belajar</b>, bukan tanda kalian nggak bisa.</div>

<!--
⏱️ 1 menit · Q&A
-->
