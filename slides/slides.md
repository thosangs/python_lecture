---
theme: default
title: Ijazah Raka — Python Fundamentals & Logic
info: |
  Kelas Python untuk pemula (2,5 jam), satu cerita: membantu Raka, fresh graduate,
  mengotomasi urusan lamaran kerja. Neo-brutalist × toska × kuning.
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
section: Prolog · Malam-malam Cari Kerja
bab: 0
footer: false
---

<div class="cover-frame"></div>

<div class="eyebrow">// Python Fundamentals &amp; Logic · Pertemuan 1</div>

# Ijazah <span class="hl">Raka</span>

<div class="lead" style="max-width: 640px">Dari copy-paste lamaran ke kartu lamaran otomatis. <b>Satu cerita, 2,5 jam</b>, dan kamu yang nulis kodenya.</div>

<div class="row mt-8" style="max-width: 760px">
  <div class="card pop"><div class="box-h">Durasi</div><b>2,5 jam</b></div>
  <div class="card pop"><div class="box-h">Level</div><b>Pemula total</b></div>
  <div class="card pop"><div class="box-h">Mode</div><b>Cerita + live coding</b></div>
</div>

<div class="sticker" style="position:absolute; right: 70px; top: 90px; font-size: 1rem">🎓 Edisi Fresh Graduate</div>

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
    <p class="mt-3">Siapa yang pernah ngisi <b>form yang itu-itu lagi</b> berulang-ulang? Misalnya form lamaran kerja.</p>
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
    <div style="font-size: 6rem; line-height: 1">🧑‍🎓</div>
    <div class="huge" style="font-size: 3rem; margin-top: 12px">RAKA</div>
    <div class="muted mono small">Fresh graduate · wisuda Sept 2026</div>
  </div>
  <div class="stack">
    <div class="card">
      <div class="box-h">Ijazahnya</div>
      <b>S1 Statistika</b>, Universitas Kenanga Raya <span class="muted small">(fiktif)</span>
      <div class="mt-3 flex gap-2">
        <span class="tag wajib">144 SKS</span>
        <span class="tag wajib">IPK 3.45</span>
        <span class="tag wajib">lulus 4 tahun</span>
      </div>
    </div>
    <div class="card">
      <div class="box-h">Misinya</div>
      Dapat kerja pertama sebagai <b>Data Analyst</b>.
    </div>
    <div class="card soft">
      <div class="box-h">Orangnya</div>
      Rajin, jago Excel... tapi tiap malam habis buat ngurus lamaran.
    </div>
  </div>
</div>

<!--
⏱️ 1 menit

"Raka ini mirip banyak dari kita: baru lulus, semangat, jago Excel. Tapi ngurus lamaran ternyata makan waktu banget."
Semua nama kampus, perusahaan, dan nomor ijazah di kelas ini fiktif.
-->

---

<div class="eyebrow">// 📖 Cerita</div>

## Malam-malam Raka

<div class="grid grid-cols-[1.25fr_1fr] gap-8 mt-2">

<div class="stack" style="gap: 8px">
  <div class="flowrow"><span class="tag paham">21.00</span> Buka 5 portal lowongan</div>
  <div class="flowrow"><span class="tag paham">21.15</span> Salin lowongan baru ke Excel</div>
  <div class="flowrow"><span class="tag paham">21.35</span> Cek syarat satu-satu: IPK minimal, jurusan</div>
  <div class="flowrow"><span class="tag paham">21.55</span> Ketik ulang data diri di form tiap perusahaan</div>
  <div class="flowrow"><span class="tag paham">22.15</span> Edit surat lamaran: ganti nama perusahaan</div>
  <div class="flowrow"><span class="tag wajib">22.30</span> <b>Kirim... besok ulang lagi. 😮‍💨</b></div>
</div>

<div>
<div class="box-h">// Nama Raka di 3 dokumen</div>

```text
"  raka PRATAMA putra "  | form online
"RAKA PRATAMA PUTRA"     | KTP
"Raka Pratama Putra   "  | CV
```

<div class="mt-6 lead">±<b class="hl">90 menit</b> setiap malam.</div>
</div>

</div>

<!--
⏱️ 1 menit

"Ini terjadi setiap malam selama Raka cari kerja."
Tunjuk data nama yang berantakan: orangnya sama, tulisannya beda-beda. Ini akan jadi masalah di Bab 6.
-->

---

<div class="eyebrow">// 📖 Sampai suatu hari...</div>

## Lupa ganti satu nama

<div class="chat mt-8" style="max-width: 760px; margin-left: auto; margin-right: auto">
  <div class="bubble me"><small>RAKA → PT DATA MAJU · 22.27</small>Yth. HRD <b>PT Awan Biru</b>, dengan ini saya melamar posisi Data Analyst... 📎</div>
  <div class="bubble them"><small>HRD PT DATA MAJU · 09.10</small>Terima kasih, Mas Raka. Tapi... lamarannya buat kami atau buat PT Awan Biru? 😅</div>
  <div v-click class="bubble me"><small>RAKA · 09.12</small>Mohon maaf, salah copy-paste surat 🙇</div>
</div>

<!--
⏱️ 30 detik

"Copy-paste surat lamaran, lupa ganti nama perusahaan. Capek, ngantuk, manusiawi. Tapi kesan pertama ke HRD jadi jelek."
-->

---
mode: colab-demo
where: 00 · Demo Final
---

<div class="eyebrow">// Misi hari ini</div>

# Gimana kalau semuanya selesai dalam <span class="hl">1 detik</span>?

<div class="grid grid-cols-[1fr_1.1fr] gap-10 mt-6 items-center">
  <div>
    <p class="lead">Di akhir kelas, <b>kalian sendiri</b> yang bikin script kartu lamaran otomatis buat Raka.</p>
    <p class="muted">Semua materi hari ini = potongan puzzle untuk script itu.</p>
    <div class="mt-6"><Goto to="colab" where="Materi · section 00 · Demo Final" /></div>
  </div>

<div class="code-xs">

```text
==============================================
       KARTU LAMARAN RAKA PRATAMA PUTRA
==============================================
Perusahaan       : PT DATA MAJU
Posisi           : Data Analyst
----------------------------------------------
Nama             : Raka Pratama Putra (22 th)
Tanggal lulus    : 15-09-2026 (lulusan ke-457)
IPK              : 3.45
Memenuhi syarat? : True
==============================================
Yth. HRD PT DATA MAJU,
saya Raka Pratama Putra, lulusan Statistika ...
```

</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 PINDAH KE COLAB → notebook 01_materi_ijazah_raka, section "00 · Demo Final"

1. Jalankan cell, isi nama perusahaan, posisi, dan IPK minimal saat diminta input.
2. Biarkan output kartu tampil penuh. Scroll cepat: kodenya "cuma" ±50 baris.
3. "Ini yang KALIAN sendiri bakal bikin di akhir kelas. Nama perusahaan nggak mungkin ketuker lagi."
4. Jangan jelaskan kodenya sekarang. Tujuannya bikin penasaran.

➡️ Balik ke slide 7.
-->

---

<div class="eyebrow">// Peta perjalanan</div>

## 8 bab, 8 nilai A, lalu lulus 🎓

<div class="grid grid-cols-[1.55fr_1fr] gap-8 mt-2">
  <Transkrip :done="0" />
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

<div class="mt-6 lead">Hari ini kalian akan <b>kenalan sama Python</b>, <b>nulis & jalanin kode sendiri</b>, dan <b>bikin kartu lamaran otomatis</b> buat Raka.</div>

<!--
⏱️ 1 menit

- Bacakan tujuan versi ramah peserta (teks di bawah).
- "Setiap selesai satu bab, kalian dapat nilai A di transkrip. 8 nilai A = lulus: kartu lamaran otomatis."
- Lihat footer: kotak kecil di tengah = progres transkrip, label kanan = kita lagi di mana (Colab/VSCode/Hands-on).
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
    <div class="node"><div class="t">💼 LinkedIn</div><div class="s">format A</div></div>
    <div class="node"><div class="t">📋 Jobstreet</div><div class="s">format B</div></div>
    <div class="node"><div class="t">🚀 Glints</div><div class="s">format C</div></div>
    <div class="node"><div class="t">🏢 Web karier</div><div class="s">beda-beda lagi</div></div>
  </div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="node yl" style="flex: 0.8; text-align:center; padding: 24px 14px">
    <div style="font-size: 3rem">🧑‍🎓</div>
    <div class="t" style="font-size: 1.2rem">Raka</div>
    <div class="s">sendirian, tiap malam</div>
  </div>
  <div class="card pop" style="flex: 1.4">
    <div class="huge" style="font-size: 2.3rem">Di dunia data, datanya bukan cuma 1 file Excel.</div>
    <p class="muted mt-3">Datang dari banyak tempat, tiap hari, dengan format beda-beda.</p>
  </div>
</div>

<!--
⏱️ 00:07 · 2 menit

"Excel itu alat yang bagus. Masalahnya, data di dunia nyata datang dari banyak tempat, tiap hari, dengan format beda-beda. Lowongan kerja juga begitu: 5 portal, 5 format."

Tanya: "Di kerjaan/kampus kalian, data datang dari mana aja?" (1–2 jawaban saja)
-->

---

<div class="eyebrow">// Bab 1</div>

## 3 musuh kerja manual

<div class="grid grid-cols-3 gap-6 mt-4">
  <div class="card pop"><div style="font-size:2.2rem">🔁</div><h3 class="mt-2">Repetitif</h3>Form yang sama, tiap lamaran.</div>
  <div class="card pop"><div style="font-size:2.2rem">😴</div><h3 class="mt-2">Membosankan</h3>Bikin kita lengah.</div>
  <div class="card err"><div style="font-size:2.2rem">⚠️</div><h3 class="mt-2" style="color: var(--err)">Rawan salah</h3>Salah nama perusahaan, nomor ijazah ketuker, IPK <code>3.45</code> jadi <code>34.5</code>.</div>
</div>

<div class="card mt-8 flowrow" style="gap: 20px">
  <div class="box-h" style="margin:0">Hitung bareng</div>
  <div class="mono"><b>90</b> menit × <b>30</b> malam =</div>
  <div v-click class="huge" style="font-size: 2.4rem"><span class="hl">±45 jam/bulan</span></div>
  <div v-after class="muted">= hampir 6 hari kerja, cuma buat copy-paste lamaran.</div>
</div>

<!--
⏱️ 2,5 menit

- Minta peserta hitung dulu sebelum klik reveal: 90 × 30 = 2.700 menit = 45 jam ≈ 6 hari kerja.
- "Yang paling bahaya bukan capeknya, tapi SALAHNYA. Satu digit nomor ijazah ketuker, HRD bisa langsung menganggap datanya tidak valid."
-->

---

<div class="eyebrow">// Bab 1</div>

## Kode itu <span class="hl">template</span>

<div class="grid grid-cols-[1fr_auto_1fr] gap-6 mt-4 items-center">
  <div class="card"><div class="box-h">Manual</div><div class="huge" style="font-size:3rem">90 menit</div><p class="muted">hasil bisa salah-salah</p></div>
  <div class="arw" style="font-size: 3rem">➜</div>
  <div class="card tk"><div class="box-h">Script</div><div class="huge" style="font-size:3rem">1 detik</div><p>hasil selalu konsisten</p></div>
</div>

<div class="mt-6 lead">Ditulis <b>sekali</b>, dipakai <b>berkali-kali</b>, hasilnya <b>selalu sama</b>. Bonusnya: hampir semua lowongan Data Analyst yang Raka lihat <b class="hl">minta Python</b>. 😉</div>

<div class="mt-4"><Transkrip :done="1" :stamping="1" compact /></div>

<!--
⏱️ 1,5 menit · 🎓 NILAI A UNTUK BAB 1

"Kode itu kayak template surat. Ditulis sekali, tinggal isi datanya, hasilnya selalu rapi. Dan sekalian, Python itu skill yang dicari di lowongan yang Raka incar."

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
    <div class="box-h">🖨️ Low level</div>
    "Ambil kertas A4 80 gram, buka tutup mesin, taruh ijazah menghadap kaca pojok kiri atas, kontras level 3, tekan tombol hijau 5 kali..."
  </div>
  <div class="card pop">
    <div class="box-h">🖨️ High level</div>
    <span style="font-size: 1.3rem; font-weight: 700">"Mas, fotokopi ijazah 5 lembar, sekalian legalisir ya."</span>
  </div>
</div>

<!--
⏱️ 00:13 · 1,5 menit

"Hasilnya sama-sama fotokopian. Bedanya: siapa yang mikirin detailnya. Di bahasa high level, detail ribetnya diurus oleh bahasanya."
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
        System.out.println("Halo, dunia kerja!");
    }
}
```

<div class="box-h mt-3">Python</div>
<div class="code-lg code-yl">

```python
print("Halo, dunia kerja!")
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
syarat_jurusan = ["statistika", "matematika"]
jurusan_raka = "statistika"

if jurusan_raka in syarat_jurusan:
    print("Siap, kirim lamaran!")
else:
    print("Cari lowongan lain.")
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
    <tr><td><b>Analogi</b></td><td>🎙️ Penerjemah simultan saat wawancara: kalimat demi kalimat</td><td>📜 Penerjemah tersumpah: seluruh ijazah diterjemahkan & dicetak dulu</td></tr>
    <tr><td><b>Error ketahuan</b></td><td>Saat baris itu dijalankan. Baris sebelumnya <b>sudah jalan</b></td><td>Saat compile, <b>sebelum</b> program jalan sama sekali</td></tr>
    <tr><td><b>Kelebihan</b></td><td>Cepat dicoba, cocok eksplorasi data</td><td>Eksekusi lebih cepat</td></tr>
    <tr><td><b>Kekurangan</b></td><td>Eksekusi relatif lebih lambat</td><td>Tiap ubah kode harus compile ulang</td></tr>
  </tbody>
</table>

<!--
⏱️ 2 menit

"Penerjemah simultan menerjemahkan kalimat demi kalimat. Kalau di kalimat ke-3 dia salah, kalimat 1 & 2 sudah terlanjur diucapkan. Penerjemah tersumpah beda: seluruh ijazah diterjemahkan dulu, dicek, baru dicetak. Kalau ada salah, ketahuan sebelum dipakai, tapi tiap ada perubahan harus terjemah & cetak ulang."

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

## Penerjemah kalimat demi kalimat

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2 items-start">
<Predict :options="['0 baris', '2 baris', '4 baris']" :answer="1" note="baris 1–2 jalan, baris 3 error, baris 4 nggak pernah dijalankan">

```python
print("1. Buka portal lowongan... beres")
print("2. Salin data lowongan... beres")
prnt("3. Cek syarat IPK...")
print("4. Kirim lamaran")
```

</Predict>
<div class="stack">
  <div class="card soft"><div class="box-h">Pertanyaan</div>Ada typo di baris 3. <b>Berapa baris</b> yang tercetak?</div>
  <Goto to="colab" where="Materi · Bab 3 · Halo Python" />
  <div v-click="2" class="code-sm code-err">

```text
1. Buka portal lowongan... beres
2. Salin data lowongan... beres
NameError: name 'prnt' is not defined
```

  </div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 3 · Halo Python" (peserta nonton saja)

- Tanya tebakan dulu, klik untuk reveal, lalu jalankan di Colab.
- Jangan bahas cara baca error dulu: itu di slide 23 saat peserta mengalaminya sendiri.
-->

---

<div class="eyebrow">// Bab 2 <span class="tag kenalan">kenalan</span></div>

## General purpose: satu bahasa, banyak kegunaan

<div class="grid grid-cols-5 gap-4 mt-4">
  <div class="card pop"><div style="font-size:2rem">📊</div><h3 class="mt-2">Data</h3><span class="small">pandas · numpy · matplotlib</span></div>
  <div class="card"><div style="font-size:2rem">🤖</div><h3 class="mt-2">AI / ML</h3><span class="small">scikit-learn · PyTorch</span></div>
  <div class="card"><div style="font-size:2rem">🌐</div><h3 class="mt-2">Web</h3><span class="small">Django · Flask · FastAPI</span></div>
  <div class="card"><div style="font-size:2rem">🎮</div><h3 class="mt-2">Game</h3><span class="small">pygame</span></div>
  <div class="card pop-yl"><div style="font-size:2rem">⚙️</div><h3 class="mt-2">Otomasi</h3><span class="small">openpyxl (Excel!) · requests</span></div>
</div>

<div class="story mt-10">
<b>Library</b> = template CV siap pakai. Raka nggak desain CV dari nol, tinggal pakai template yang sudah jadi. Raka nanti pakai <code>pandas</code> buat baca data lowongan (pertemuan berikutnya).
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

<div class="mt-3"><Transkrip :done="2" :stamping="2" compact /></div>

<!--
⏱️ 1 menit · 🎓 NILAI A UNTUK BAB 2

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

## Development environment = meja kerja

<div class="lead mt-2" style="max-width: 760px">Tempat kita <b>menulis</b>, <b>menjalankan</b>, dan <b>mengembangkan</b> aplikasi. Mejanya tergantung mau ngerjain apa.</div>

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

"Mahasiswa butuh meja belajar. Programmer butuh dev environment."
-->

---

<div class="eyebrow">// Bab 3</div>

## Isi meja kerja Python

<table>
  <thead><tr><th>Komponen</th><th>Fungsinya</th><th>Analogi</th><th>Level</th></tr></thead>
  <tbody>
    <tr><td><b>Python interpreter</b></td><td>Yang benar-benar menjalankan kode</td><td>🏢 Petugas loket yang memproses berkas kita</td><td><span class="tag paham">paham</span></td></tr>
    <tr><td><b>Code editor</b></td><td>Tempat menulis kode</td><td>📝 Meja & kertas buat nulis</td><td><span class="tag paham">paham</span></td></tr>
    <tr><td><b>Package manager</b> <code>pip</code> <code>uv</code></td><td>Download & install library</td><td>🛒 Koperasi kampus: beli perlengkapan</td><td><span class="tag kenalan">kenalan</span></td></tr>
    <tr><td><b>Virtual environment</b></td><td>Ruang terpisah per proyek, biar versi library nggak bentrok</td><td>🗂️ Map terpisah per lamaran</td><td><span class="tag kenalan">kenalan</span></td></tr>
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
    <tr><td><b>Text editor + terminal</b></td><td>Notepad++ + terminal</td><td>Meja lipat minimalis</td><td>Script kecil, server</td></tr>
    <tr><td><b>IDE</b></td><td>VSCode, PyCharm</td><td>Meja kerja lengkap</td><td>Aplikasi & script yang dipakai rutin</td></tr>
    <tr><td><b>Notebook</b></td><td>Jupyter, <b>Google Colab</b>, Marimo</td><td><span class="hl">Kertas coretan</span>: hitung per bagian, langsung lihat hasil</td><td>Belajar, eksplorasi & analisis data</td></tr>
  </tbody>
</table>

<div class="card pop-yl mt-8">
<div class="box-h">Notebook</div>
Kode dipotong-potong per <b>cell</b>. Tiap cell bisa dijalankan sendiri dan hasilnya langsung kelihatan di bawahnya.
</div>

<!--
⏱️ 2 menit

"Notebook itu kayak kertas coretan waktu ujian: hitung per bagian, langsung lihat hasilnya. Cocok buat belajar dan eksplorasi data."
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
    <p class="lead mt-2">Tempat script <b>"beneran"</b> yang dijalankan tiap ada lowongan baru.</p>
    <span class="sticker r">tujuan akhir Raka</span>
  </div>
</div>

<div class="mt-8 flex items-center gap-6">
  <span class="lead">Saatnya pegang kode!</span>
  <Goto to="hands-on" where="Hands-on 1 · Halo, dunia kerja!" />
</div>

<!--
⏱️ 1,5 menit

"Sepanjang kelas kita pakai Colab. Di akhir kelas, kita pindahin hasilnya ke VSCode, karena itulah yang nanti dijalankan Raka tiap ada lowongan baru."

Kenapa semua pakai Colab: nol instalasi = nol waktu terbuang buat troubleshooting setup; beban kognitif fokus ke Python, bukan tools.
-->

---
mode: hands-on
where: Latihan · Bab 3
---

<div class="eyebrow">// Hands-on 1 · Halo, dunia kerja!</div>

## Meja kerja pertamamu

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-2">
<div>
<ol>
  <li>Buka notebook latihan (link di kanan / di chat)</li>
  <li><b>File → Save a copy in Drive</b></li>
  <li>Ganti nama: <code>IjazahRaka_NamaKamu</code></li>
  <li>Scroll ke section <b>Bab 3 · Halo Python</b></li>
  <li>Ketik di code cell, lalu tekan <span class="kbd">Shift</span> + <span class="kbd">Enter</span></li>
  <li>Ganti tulisannya jadi namamu, jalankan lagi</li>
  <li><b>+ Text</b> → tulis: <i>Catatan kelas Python pertamaku 🎓</i></li>
  <li>Kasih sinyal 🟢 berhasil · 🔴 stuck</li>
</ol>
</div>
<div class="stack">
  <Goto to="hands-on" where="Buka 02_latihan_peserta di Colab" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
  <div class="code-lg">

```python
print("Halo, dunia kerja!")
```

  </div>
  <div class="card soft small">
    <b>Cell</b> = kotak kode. Angka <code>[1]</code> di kiri = urutan cell dijalankan. Run pertama agak lama karena Colab lagi nyiapin "meja kerja" (runtime).
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
      1 print("1. Buka portal lowongan... beres")
      2 print("2. Salin data lowongan... beres")
----> 3 prnt("3. Cek syarat IPK...")

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
where: lamaran-raka/kartu_lamaran.py
---

<div class="eyebrow">// Hands-on 1 · Demo</div>

## Meja kerja lengkap: VSCode

<div class="grid grid-cols-[1fr_1fr] gap-8 mt-2">
<div>
<ol>
  <li><b>File → Open Folder</b> → <code>lamaran-raka</code></li>
  <li>File baru: <code>kartu_lamaran.py</code></li>
  <li>Ketik kodenya → <b>simpan</b> <span class="kbd">Cmd/Ctrl</span> + <span class="kbd">S</span></li>
  <li>Klik ▶ <b>Run Python File</b>, atau lewat terminal:</li>
</ol>

```bash
python3 kartu_lamaran.py   # Mac/Linux
python kartu_lamaran.py    # Windows
```

</div>
<div class="stack">
  <Goto to="vscode" where="demo trainer, peserta yang sudah install boleh ikut" />
  <div class="card pop-yl">
    <div class="box-h">Bedanya sama Colab</div>
    Ini <b>file</b> <code>.py</code>: dokumen yang tersimpan rapi. Bisa dijalankan kapan saja tanpa browser, tiap kali ada lowongan baru.
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
    <tr><td><b>Analogi</b></td><td>Kertas coretan</td><td>Meja kerja lengkap</td></tr>
    <tr><td><b>Cara jalan</b></td><td>Per cell, <span class="kbd">Shift</span>+<span class="kbd">Enter</span></td><td>Seluruh file sekaligus</td></tr>
    <tr><td><b>Dipakai untuk</b></td><td>Belajar, eksplorasi, analisis</td><td>Script rutin, aplikasi</td></tr>
  </tbody>
</table>

<div class="card pop-yl mt-5">
<div class="box-h">💡 Tips penting notebook</div>
Variabel "nggak dikenal" padahal sudah ditulis? Biasanya <b>cell-nya belum di-run</b>. Solusi pamungkas: <b>Runtime → Run all</b>.
</div>

<div class="mt-4"><Transkrip :done="3" :stamping="3" compact /></div>

<!--
⏱️ 1 menit · 🎓 NILAI A UNTUK BAB 3

➡️ "Meja kerja siap. Sekarang Raka mulai menyusun data lamarannya. Mulai sekarang kita di COLAB terus."
-->

---
section: Bab 4 · Map Berlabel
bab: 4
mode: colab-demo
where: Materi · Bab 4
---

<div class="ghostnum">04</div>
<div class="eyebrow">// Bab 4 · Map berlabel <span class="tag wajib">wajib</span></div>

## Langkah pertama Raka: catatan

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-4 items-start">
<div>

```python
# Kartu lamaran Raka
# Dibuat oleh: Raka
print("Mulai menyusun lamaran")  # komentar di ujung
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
⏱️ 00:42 · 1,5 menit · 🧪 COLAB → materi, section "Bab 4 · Map Berlabel"

Ketik live, jangan paste.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## <code>print()</code> dan konsep function

<div class="flowrow mt-2" style="gap: 14px">
  <div class="node"><div class="t">"Halo"</div><div class="s">dokumen = argumen</div></div>
  <div class="arw">➜</div>
  <div class="node tk" style="padding: 14px 22px"><div class="t" style="font-size:1.3rem">🖨️ print( )</div><div class="s">mesin = function</div></div>
  <div class="arw">➜</div>
  <div class="node"><div class="t">Halo</div><div class="s">hasil tampil di layar</div></div>
  <div class="card soft small" style="margin-left: 12px; flex: 1"><b>Built-in function</b> = mesin bawaan Python: <code>print</code>, <code>type</code>, <code>len</code>, <code>max</code>, <code>round</code>, <code>input</code>...</div>
</div>

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-start">
<div>

```python
print("Lamaran Data Analyst")
print(144)
print("Total SKS:", 144)  # dipisah koma
print()                   # baris kosong
print(Raka)               # ❌ lupa kutip
```

</div>
<div class="stack">
  <div class="card pop-yl">Baris terakhir bakal jalan nggak? 🤔</div>
  <div v-click class="card yl"><b>NameError</b>: teks wajib pakai kutip. Tanpa kutip, Python mengira <code>Raka</code> itu nama sesuatu.</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Function itu kayak mesin fotokopi: dokumen masuk, hasil keluar. print() mencetak ke layar."
"Teks pakai tanda kutip, angka tidak. Tanpa kutip, Python mengira Raka itu nama sesuatu, dan dia nggak kenal → NameError, teman lama kita."
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Variabel = map berlabel

<div class="grid grid-cols-[1.25fr_1fr] gap-8 items-start">
<div>
  <div class="flex gap-4 mt-1">
    <Folder label="nama_lengkap" value='"Raka Pratama Putra"' type="str" />
    <Folder label="total_sks" value="144" type="int" accent="yl" />
    <Folder label="ipk" value="3.45" type="float" />
  </div>
  <div class="card pop mt-5 flowrow" style="gap: 14px">
    <code style="font-size:1.1rem">nama = nilai</code>
    <span><b><span class="hl">=</span> artinya MASUKKAN KE</b>, bukan "sama dengan". Baca dari <b>kanan ke kiri</b>.</span>
  </div>
</div>
<Predict :options="['10', '12', 'Error']" :answer="1" note="ambil isi, kurangi 3, tambah 5, masukkan lagi">

```python
lamaran_aktif = 10
lamaran_aktif = lamaran_aktif - 3
lamaran_aktif = lamaran_aktif + 5
print(lamaran_aktif)
```

</Predict>
</div>

<!--
⏱️ 2 menit

"Di Excel, Raka nyimpen IPK di sel B2. Masalahnya, B2 itu apa? Di Python, kita kasih NAMA yang bermakna, kayak label di map dokumen."

Ketik di Colab: nama_lengkap, total_sks, ipk, lalu print.

Tebak output: "Raka punya 10 lamaran aktif, 3 ditolak, lalu kirim 5 lagi."
"Di matematika x = x + 1 itu mustahil. Di Python normal: ambil isi map, tambah 1, masukin lagi."

Miskonsepsi `=` sebagai "sama dengan" sangat umum. Tekankan sekarang karena di Bab 5 muncul `==`.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Isi map bisa diganti

<div class="grid grid-cols-2 gap-8 mt-2">
<div>
<div class="box-h">☕ Java: tipe ditulis & dikunci</div>

```java
double ipk = 3.45;
ipk = "tiga koma empat lima"; // ❌ error
```

<div class="box-h mt-4">🐍 Python: tipe "ditebak" dari isinya</div>

```python
ipk = 3.45
print(type(ipk))  # <class 'float'>

ipk = "tiga koma empat lima"  # ✅ boleh, tapi
print(type(ipk))  # <class 'str'>
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Nama sama = ditimpa</div>Isi map diganti, <b>isi lama hilang</b>.</div>
  <div class="card pop"><div class="box-h">Dynamic typing</div>Python menebak tipe dari isinya. Fleksibel, tapi <b>jangan ganti-ganti tipe</b> di satu variabel.</div>
  <div class="card soft"><div class="box-h"><code>type()</code></div>Built-in function buat ngecek isi map itu jenisnya apa.</div>
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
    <tr><td>Tidak boleh diawali angka</td><td><code>1nama = "Raka"</code></td><td><code>nama1 = "Raka"</code></td><td>SyntaxError: invalid decimal literal</td></tr>
    <tr><td>Tidak boleh pakai spasi</td><td><code>nama lengkap = ...</code></td><td><code>nama_lengkap</code></td><td>SyntaxError: invalid syntax</td></tr>
    <tr><td>Hanya huruf, angka, <code>_</code></td><td><code>total-sks = 144</code></td><td><code>total_sks</code></td><td>SyntaxError: cannot assign to expression here</td></tr>
    <tr><td>Bukan <i>keyword</i> Python</td><td><code>class = "Statistika"</code></td><td><code>kelas = ...</code></td><td>SyntaxError: invalid syntax</td></tr>
    <tr><td><i>Case sensitive</i></td><td><code>Ipk</code> ≠ <code>ipk</code></td><td>konsisten</td><td>NameError kalau salah huruf</td></tr>
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

"Kenapa total-sks salah? Tanda - dibaca Python sebagai PENGURANGAN: 'total dikurangi sks'."
Keyword = kata yang udah dipesan Python: if, for, class, True, dll.

Fun fact kalau ada yang iseng: `1jurusan = ...` malah muncul "invalid imaginary literal", karena `1j` dibaca sebagai bilangan kompleks. Tetap sama-sama SyntaxError.
-->

---
mode: colab-demo
where: Materi · Bab 4
---

<div class="eyebrow">// Bab 4 <span class="tag paham">paham</span></div>

## Jebakan: boleh, tapi bikin celaka

<div class="story">Raka pernah bikin variabel <code>max</code> buat nyimpen IPS tertinggi. 10 menit kemudian...</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
max = 3.65        # IPS tertinggi
print(max)        # 3.65 (normal)

print(max(3.20, 3.65, 3.41))
# ❌ TypeError: 'float' object
#    is not callable
```

</div>
<div>

```python
del max           # hapus variabel kita
print(max(3.20, 3.65, 3.41))  # ✅ 3.65
```

<div class="card pop-yl mt-4 small">
Hindari nama <code>max</code> <code>min</code> <code>sum</code> <code>list</code> <code>str</code> <code>print</code> <code>type</code> <code>input</code>. Kalau nama variabelmu <b>berubah warna</b> di editor → ganti namanya.
</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Nama function bawaan BUKAN keyword, jadi Python mengizinkan. Tapi mesin max aslinya ketimpa angka. Kayak map dikasih label 'mesin fotokopi', mesinnya jadi hilang."
"del dipakai menghapus variabel. Setelah dihapus, kalau dipanggil lagi → NameError."
-->

---

<div class="eyebrow">// Bab 4 <span class="tag wajib">wajib</span></div>

## Konvensi: biar rapi & dimengerti orang lain

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-2 items-start">
<table>
  <thead><tr><th>Jenis</th><th>Gaya (PEP 8)</th><th>Contoh</th></tr></thead>
  <tbody>
    <tr><td>Variabel</td><td><code>snake_case</code></td><td><code>nama_lengkap</code></td></tr>
    <tr><td>Konstanta</td><td><code>UPPER_CASE</code></td><td><code>IPK_MINIMAL = 3.00</code></td></tr>
    <tr><td>Class (nanti)</td><td><code>PascalCase</code></td><td><code>KartuLamaran</code></td></tr>
  </tbody>
</table>
<div class="stack">
  <div class="card err"><div class="box-h" style="color: var(--err)">Nama jelek</div><code>x</code> <code>a1</code> <code>data2</code> <code>tmp</code></div>
  <div class="card pop"><div class="box-h">Nama bagus</div><code>total_sks</code> <code>tahun_lulus</code></div>
</div>
</div>

<div class="grid grid-cols-2 gap-6 mt-8">
  <div class="card soft"><b>Aturan</b> (slide sebelumnya) = <b>wajib</b>. Dilanggar → error.</div>
  <div class="card soft"><b>Konvensi</b> = <b>kesepakatan</b>. Nggak error, tapi kode lebih sering <b>dibaca</b> daripada ditulis.</div>
</div>

<!--
⏱️ 1 menit

"Konvensi bikin kode gampang dibaca orang lain, termasuk diri kalian sendiri 3 bulan lagi. Rekan kerja di kantor pertama kalian akan berterima kasih."
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
  <li>Buat variabel data diri Raka: nama lengkap, jurusan, tahun masuk, tahun lulus</li>
  <li>Buat variabel transkrip:<br>
    <span class="mono tiny">total SKS 144 · total mutu 497</span></li>
  <li>Buat <b>konstanta</b> IPK minimal lowongan: <code>3.00</code></li>
  <li>Print semuanya, cek tipenya pakai <code>type()</code></li>
</ol>
</div>
<div>
<div class="box-h">🕵️ Pojok Error: tebak, error atau tidak?</div>
<div class="code-sm">

```python
jurusan_1 = "Statistika"
1prodi = "Matematika"
tahun lulus = 2026
_catatan = "rahasia"
Ipk = 3.45
print(ipk)
```

</div>
<div v-click class="answer small mt-1">❌ baris 2 & 3 SyntaxError · baris 6 NameError</div>
</div>
</div>

<div class="mt-4"><Transkrip :done="4" :stamping="4" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 4 · Map Berlabel" · 🎓 NILAI A UNTUK BAB 4

- Di notebook latihan, Pojok Error sudah dipisah satu cell per baris: tebak dulu, baru jalankan satu per satu.
- Variabel dari latihan ini dipakai lagi di Bab 5 (data kit juga tersedia di section Bab 5).

➡️ "Data diri udah masuk map. Sekarang saatnya NGITUNG IPK."
-->

---
section: Bab 5 · Ngitung IPK
bab: 5
---

<div class="ghostnum">05</div>
<div class="eyebrow">// Bab 5 · Ngitung IPK</div>

## Peta tipe data

<table class="dense">
  <thead><tr><th>Kategori</th><th>Tipe</th><th>Contoh di cerita Raka</th><th>Gampangnya</th><th>Dibahas</th></tr></thead>
  <tbody>
    <tr><td>Numeric</td><td><code>int</code></td><td><code>144</code> total SKS</td><td>dihitung bulat</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td></td><td><code>float</code></td><td><code>3.45</code> IPK</td><td>ada komanya</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td></td><td><code>complex</code></td><td><code>3+4j</code></td><td>–</td><td>Bab 5 <span class="tag kenalan">kenalan</span></td></tr>
    <tr><td>Boolean</td><td><code>bool</code></td><td><code>True</code> memenuhi syarat</td><td>kotak centang ✅ / ❌</td><td>Bab 5 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Text</td><td><code>str</code></td><td><code>"Raka Pratama Putra"</code></td><td>tulisan di ijazah</td><td>Bab 6 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Sequence</td><td><code>list</code> <code>tuple</code></td><td>IPS per semester, tanggal lahir</td><td>daftar urut</td><td>Bab 7 <span class="tag wajib">wajib</span></td></tr>
    <tr><td>Set</td><td><code>set</code> <code>frozenset</code></td><td>skill tanpa dobel</td><td>daftar unik</td><td>Bab 7 <span class="tag paham">paham</span></td></tr>
    <tr><td>Mapping</td><td><code>dict</code></td><td>transkrip</td><td>mata kuliah → nilai</td><td>Bab 7 <span class="tag wajib">wajib</span></td></tr>
  </tbody>
</table>

<!--
⏱️ 00:57 · 1 menit (advance organizer)

"Ini peta semua jenis data di Python. Kita kunjungi satu-satu."
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
total_sks = 144            # int  : bilangan bulat
ipk = 3.45                 # float: desimal (TITIK)
GAJI_HARAPAN = 6_500_000   # underscore boleh

print(type(total_sks), type(ipk))
# <class 'int'> <class 'float'>

z = 3 + 4j                 # complex: kenalan aja
print(type(z))             # <class 'complex'>
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h">Desimal = titik</div><code>3.45</code> ✅ &nbsp; <code>3,45</code> ❌</div>
  <div class="card pop"><div class="box-h">Underscore</div><code>6_500_000</code> sama persis dengan <code>6500000</code></div>
  <div class="card soft small"><b>Tips:</b> uang Rupiah simpan sebagai <code>int</code>. (Kenapa? Coba <code>0.1 + 0.2</code> 😉)</div>
</div>
</div>

<!--
⏱️ 1,5 menit · 🧪 COLAB → materi, section "Bab 5 · Ngitung IPK" (jalankan data kit dulu)

"IPK di ijazah ditulis 3,45 pakai koma. Di Python wajib pakai titik: 3.45."
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
  <thead><tr><th>Op</th><th>Arti</th><th>Contoh cerita Raka</th><th>Hasil</th></tr></thead>
  <tbody>
    <tr><td><code>+</code></td><td>tambah</td><td><code>tahun_masuk + 4</code></td><td><code>2026</code></td></tr>
    <tr><td><code>-</code></td><td>kurang</td><td><code>tahun_lulus - tahun_masuk</code></td><td><code>4</code></td></tr>
    <tr><td><code>*</code></td><td>kali</td><td><code>18 * 8</code> SKS × semester</td><td><code>144</code></td></tr>
    <tr><td><code>/</code></td><td>bagi, <b>selalu float</b></td><td><code>total_mutu / total_sks</code> IPK</td><td><code>3.4513...</code></td></tr>
    <tr><td><code>//</code></td><td>bagi, bulat ke bawah</td><td><code>100_000 // 7_500</code> lembar legalisir</td><td><code>13</code></td></tr>
    <tr><td><code>%</code></td><td>sisa bagi</td><td><code>100_000 % 7_500</code> sisa uang</td><td><code>2500</code></td></tr>
    <tr><td><code>**</code></td><td>pangkat</td><td><code>1.1 ** 3</code></td><td><code>1.331...</code></td></tr>
  </tbody>
</table>
<div class="stack">
  <Predict :options="['18', '18.0']" :answer="1" note="/ selalu menghasilkan float">

```python
print(144 / 8)
```

  </Predict>
  <div class="card pop small"><b>Urutan:</b> <code>**</code> → <code>* / // %</code> → <code>+ -</code>. Ragu? Pakai <b>kurung</b>.</div>
</div>
</div>

<!--
⏱️ 3 menit · ketik di Colab, tanya hasil sebelum run

- ipk = total_mutu / total_sks → 3.451388888888889 (IPK = jumlah bobot nilai × SKS dibagi total SKS)
- lama_studi = tahun_lulus - tahun_masuk → 4; × 2 → 8 semester
- "// dan % itu pasangan. Legalisir ijazah Rp7.500 per lembar, uang Raka Rp100.000: // = dapat berapa lembar, % = sisa uangnya."
- Gaji pertama naik 10%/tahun: GAJI_HARAPAN * 1.1 ** 3 → 8651500.000000002 (lalu round)
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
print(abs(tahun_masuk - tahun_lulus))  # 4 (selisih tanpa minus)
print(round(ipk, 2))                   # 3.45 (dibulatkan 2 desimal)
print(round(ipk))                      # 3
print(max(3.20, 3.65, 3.41))           # 3.65 (IPS tertinggi)
print(min(3.20, 3.65, 3.41))           # 3.2
print(int(3.99))                       # 3 ← dipotong, BUKAN dibulatkan!
print(float(144))                      # 144.0
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

Sebelum int(3.99): "IPK 3.99 kalau di-int jadi 3 atau 4?" (3, dipotong!)
"Programmer profesional pun buka dokumentasi tiap hari."
-->

---
mode: colab-demo
where: Materi · Bab 5
---

<div class="eyebrow">// Bab 5 <span class="tag wajib">wajib</span></div>

## Boolean: centang <span class="hl-tk">YA</span> / <span class="hl">TIDAK</span>

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
ipk = round(total_mutu / total_sks, 2)
print(ipk >= IPK_MINIMAL)       # True ← memenuhi!
print(ipk >= 3.50)              # False (PT Awan Biru)
print(jurusan == "Statistika")  # True
print(type(True))               # <class 'bool'>

print(true)                     # ❌ NameError
```

<div class="card yl mt-4"><b><code>=</code> memasukkan ke map. <code>==</code> bertanya "apakah sama?"</b> Sumber error nomor satu pemula.</div>
</div>
</div>

<!--
⏱️ 2,5 menit

"Lowongan PT Data Maju minta IPK minimal 3.00: Raka memenuhi. PT Awan Biru minta 3.50: belum."
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
# Cum laude: IPK di atas 3.50 DAN lulus maks 4 tahun?
print(ipk > 3.50 and lama_studi <= 4)   # False

# Lowongan B: IPK min 3.50 ATAU lulus maks 4 tahun?
print(ipk >= 3.50 or lama_studi <= 4)   # True

print(not True)                         # False
```

</div>
</div>

<div class="story mt-8">Sekarang boolean cuma jawab benar/salah. Pertemuan berikutnya, boolean jadi <b>otak</b> program: <i>"kalau IPK nggak memenuhi syarat, jangan kirim lamaran"</i> pakai <code>if</code>.</div>

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
<ol class="small">
  <li>Hitung IPK Raka (total mutu / total SKS)</li>
  <li>Bulatkan IPK jadi 2 desimal</li>
  <li>Berapa tahun Raka kuliah? Berapa semester?</li>
  <li>IPK memenuhi <code>IPK_MINIMAL</code>? (<code>True</code>/<code>False</code>)</li>
  <li>Memenuhi lowongan lain yang minta <code>3.50</code>?</li>
  <li><span class="tag paham">bonus</span> Cum laude? (IPK &gt; 3.50 <b>dan</b> lulus maks 4 tahun)</li>
  <li><span class="tag wajib">tantangan</span> Legalisir Rp7.500/lembar, uang Rp100.000: berapa lembar & sisa?</li>
</ol>
</div>
<div class="stack">
  <Predict :options="['3.5 0', '3 1', '3 0.5']" :answer="1">

```python
print(7 // 2, 7 % 2)
```

  </Predict>
  <div v-click="2" class="card soft small mono">Kunci: 3.4513… · 3.45 · 4 / 8 · True · False · False · 13 sisa 2500</div>
</div>
</div>

<div class="mt-2"><Transkrip :done="5" :stamping="5" compact /></div>

<!--
⏱️ 4 menit · 🎯 HANDS-ON → latihan, section "Bab 5 · Ngitung IPK" · 🎓 NILAI A UNTUK BAB 5

Ingatkan: jalankan cell data kit dulu, lalu kerjakan satu cell per soal.

Setelah latihan: tebak output 7 // 2, 7 % 2 (angkat 1/2/3 jari).

➡️ "IPK beres! Tapi Raka masih punya masalah besar: data dirinya ditulis beda-beda di tiap dokumen. Kita rehat dulu."
-->

---
mode: break
footer: true
---

<div class="eyebrow">// Istirahat · 10 menit</div>

## ⏸️ Rehat dulu

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
section: Bab 6 · Beresin Data Diri
bab: 6
mode: colab-demo
where: Materi · Bab 6
---

<div class="ghostnum">06</div>
<div class="eyebrow">// Bab 6 · Beresin data diri</div>

## Satu nama, tiga versi

<div class="grid grid-cols-[1.2fr_1fr] gap-8 mt-2 items-start">
<div class="stack">
  <div class="card"><div class="box-h">Form online (diketik buru-buru)</div><code>"  raka PRATAMA putra "</code></div>
  <div class="card"><div class="box-h">KTP</div><code>"RAKA PRATAMA PUTRA"</code></div>
  <div class="card"><div class="box-h">CV</div><code>"Raka Pratama Putra   "</code></div>
</div>
<div class="stack">
  <div class="card pop-yl">Buat manusia: orang yang <b>sama</b>.<br>Buat sistem HRD: <b>tiga nama berbeda</b>.</div>

```python
print(nama_form == nama_ktp)
# False 😱
```

  <div v-click class="card tk small">Jawaban teka-teki: <code>"10" + "5"</code> = teks digabung → <code>"105"</code>. Di akhir bab ini, <code>False</code> tadi jadi <code>True</code>.</div>
</div>
</div>

<!--
⏱️ 01:22 · 1,5 menit · 🧪 COLAB → materi, section "Bab 6 · Beresin Data Diri" (jalankan data kit teks)

"Sistem HRD sering mencocokkan data form dengan dokumen. Kalau beda, lamaran bisa dianggap tidak valid."
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
nama_kampus = "Universitas Kenanga Raya"  # kutip dua
motto = 'Lulus, lalu kerja'               # kutip satu
alamat = """Jl. Kenanga No. 12
Bandung"""                                # kutip tiga

print("Raka" + " " + "Pratama")  # gabung
print("=" * 30)                  # ulang 30 kali
print(len(nama_ktp))             # 18 (spasi dihitung)
```

</div>
<div class="stack">
  <div class="card pop"><div class="box-h"><code>+</code> gabung</div><code>"Raka" + "Putra"</code> → <code>"RakaPutra"</code></div>
  <div class="card pop"><div class="box-h"><code>*</code> ulang</div><code>"=" * 30</code> → garis pemisah kartu lamaran!</div>
  <div class="card soft small">Kutip satu atau dua <b>sama saja</b>, yang penting konsisten.</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"'=' * 30 ini nanti kita pakai buat garis di kartu lamaran Raka."
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 2
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Indexing: setiap karakter punya nomor

<div class="mt-2"><IndexStrip text="IJZ-20260915-STA-0457" name="nomor_ijazah" :sels="['[0]', '[-1]']" /></div>

<div class="grid grid-cols-[1.1fr_1fr] gap-6 mt-5 items-start">
<div class="code-sm">

```python
print(nomor_ijazah[0])    # I ← mulai dari 0!
print(nomor_ijazah[-1])   # 7 ← dari belakang
print(len(nomor_ijazah))  # 21
print(nomor_ijazah[21])   # ❌ IndexError
```

</div>
<div class="stack">
  <div class="card soft small">Struktur: <code>IJZ</code> - <code>tanggal lulus</code> - <code>kode prodi</code> - <code>nomor urut</code></div>
  <div class="card pop small">Kenapa mulai dari 0? Anggap index = <b>jarak dari awal</b>.</div>
  <div class="card yl small"><b>📕 Kamus Error · IndexError</b> = "Nomor urutnya kelewatan."</div>
</div>
</div>

<!--
⏱️ 2 menit

- Klik → sorot nomor_ijazah[0], klik lagi → nomor_ijazah[-1].
- Sebelum nomor_ijazah[21]: "Panjangnya 21, index terakhir berapa?" (20, bukan 21).
- Nomor ijazah ini fiktif, formatnya dibuat supaya gampang dibongkar.
-->

---
mode: colab-demo
where: Materi · Bab 6
clicks: 5
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Slicing: motong teks <code>[start:stop]</code>

<div class="mt-1"><IndexStrip text="IJZ-20260915-STA-0457" name="nomor_ijazah" :sels="['[0:3]', '[4:12]', '[4:8]', '[13:16]', '[-4:]']" /></div>

<div class="grid grid-cols-3 gap-5 mt-6">
  <div class="card pop"><div class="box-h">Aturan</div>Ambil dari <b>start</b>, sampai <b>sebelum</b> stop.</div>
  <div class="card pop"><div class="box-h">✂️ Mental model</div>Gunting memotong <b>di antara</b> karakter. Angka = posisi gunting.</div>
  <div class="card pop-yl"><div class="box-h">Kosong</div><code>[:3]</code> dari awal · <code>[-4:]</code> sampai akhir</div>
</div>

<!--
⏱️ 2,5 menit

- Tiap klik menyorot satu slice: [0:3] IJZ, [4:12] tanggal lulus, [4:8] tahun, [13:16] kode prodi STA, [-4:] nomor urut 0457.
- Sebelum klik ke-3: "Ambilkan tahun lulusnya saja, index berapa sampai berapa?"
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
print(angka[::2])    # 02468 → loncat 2 (genap)
print(angka[1::2])   # 13579 → mulai index 1
print(nomor_ijazah[::-1])
# 7540-ATS-51906202-ZJI → dibalik!
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

<div class="lead mt-2">Tidak bisa diubah sebagian. Kayak <b>ijazah yang sudah dicetak</b>: salah ketik nggak bisa dicoret, harus <b>cetak ulang</b>.</div>

<div class="grid grid-cols-2 gap-8 mt-6">
<div class="code-err">

```python
nomor_ijazah[0] = "X"
# ❌ TypeError: 'str' object does not
#    support item assignment
```

</div>
<div>

```python
baru = nomor_ijazah.replace("STA", "INF")
print(baru)          # ...-INF-0457 (BARU)
print(nomor_ijazah)  # ...-STA-0457 (tetap)
```

</div>
</div>

<div class="card yl mt-6 small"><b>📕 Kamus Error · TypeError</b> = "Tipe datanya nggak cocok untuk operasi ini."</div>

<!--
⏱️ 1,5 menit

Analogi ini paling nempel di cerita: ijazah salah cetak nggak bisa dicoret pakai tipe-x, harus dicetak ulang. String juga begitu: yang bisa kita lakukan adalah bikin string BARU.
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
    <tr><td><code>.strip()</code></td><td><code>"  raka  "</code> → <code>"raka"</code></td></tr>
    <tr><td><code>.upper()</code> <code>.lower()</code></td><td><code>"Raka"</code> → <code>"RAKA"</code></td></tr>
    <tr><td><code>.title()</code></td><td><code>"data analyst"</code> → <code>"Data Analyst"</code></td></tr>
    <tr><td><code>.replace(a, b)</code></td><td><code>"STA"</code> → <code>"INF"</code></td></tr>
    <tr><td><code>.split("-")</code></td><td>→ <code>['IJZ', '20260915', ...]</code></td></tr>
  </tbody>
</table>
<div>
<div class="code-sm">

```python
bersih_form = nama_form.strip().title()
bersih_ktp = nama_ktp.strip().title()
print(bersih_form)  # Raka Pratama Putra
print(bersih_form == bersih_ktp)  # True 🎉
```

</div>
<div class="small muted mt-2">Lainnya: <code>.count()</code> <code>.startswith()</code> <code>.center()</code> · ketik <code>nama.</code> lalu <span class="kbd">Tab</span></div>
</div>
</div>

<div class="mt-3">
<Predict :options="['[RAKA]', '[  RAKA  ]', '[  raka  ]']" :answer="2" note="method mengembalikan string BARU, aslinya tetap">

```python
nama = "  raka  "; nama.upper(); print("[" + nama + "]")
```

</Predict>
</div>

<!--
⏱️ 3 menit · momen "aha" bab ini

- Tunjukkan bersih_form == bersih_ktp → True. Nama Raka akhirnya cocok di semua dokumen.
- Jebakan: "Ingat, string immutable. Method TIDAK mengubah aslinya. Kalau mau disimpan: nama = nama.upper()."
- Fun fact: "pt data maju".title() → "Pt Data Maju" (t-nya kecil). Makanya di final project nama perusahaan pakai .upper().
- .split() menghasilkan LIST → jembatan ke Bab 7: "Kurung siku ini namanya list."
-->

---
mode: colab-demo
where: Materi · Bab 6
---

<div class="eyebrow">// Bab 6 <span class="tag wajib">wajib</span></div>

## Casting: ganti jenis data

<div class="grid grid-cols-[1.4fr_1fr] gap-8 mt-2 items-start">
<div>

```python
nomor = nomor_ijazah[-4:]
print(nomor, type(nomor))   # 0457 <class 'str'>

lulusan_ke = int(nomor)     # nol di depan hilang
print(lulusan_ke)           # 457

print("Lulusan ke-" + str(457))  # angka → teks
print(float("3.45"))             # 3.45
print(float("3,45"))             # ❌ ValueError
```

</div>
<div class="stack">
  <div class="card pop">Data dari form online sering datang sebagai <b>teks</b>, walaupun isinya angka.</div>
  <div class="card soft small">Kebiasaan Indonesia: desimal pakai <b>koma</b>. Python pakai <b>titik</b>.</div>
  <div class="card yl small"><b>📕 Kamus Error · ValueError</b> = "Tipenya benar, nilainya nggak masuk akal."</div>
</div>
</div>

<!--
⏱️ 1,5 menit

"Raka ngetik IPK 3,45 pakai koma, kebiasaan dari ijazah. Python protes: teksnya ada, tapi nggak bisa jadi angka."
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
  <li>Rapikan ketiga versi nama → <code>"Raka Pratama Putra"</code></li>
  <li>Buktikan ketiganya sama (pakai <code>==</code> dan <code>and</code>)</li>
  <li>Dari <code>nomor_ijazah</code>: tanggal, kode prodi, nomor urut</li>
  <li>Ubah nomor urut jadi angka <code>457</code></li>
  <li><span class="tag paham">bonus</span> Tanggal lulus jadi <code>"15-09-2026"</code></li>
  <li><span class="tag wajib">tantangan</span> Ada berapa huruf "a" di nama rapi?</li>
</ol>
</div>
<div v-click class="code-xs">
<div class="box-h">Kunci</div>

```python
bersih_form = nama_form.strip().title()
bersih_ktp = nama_ktp.strip().title()
bersih_cv = nama_cv.strip().title()
print(bersih_form == bersih_ktp
      and bersih_ktp == bersih_cv)       # True
print(nomor_ijazah[4:12], nomor_ijazah[13:16])
print(int(nomor_ijazah[-4:]))            # 457
print(nomor_ijazah[10:12] + "-" + nomor_ijazah[8:10]
      + "-" + nomor_ijazah[4:8])         # 15-09-2026
print(bersih_form.lower().count("a"))    # 6
```

</div>
</div>

<div class="mt-3"><Transkrip :done="6" :stamping="6" compact /></div>

<!--
⏱️ 5,5 menit · 🎯 HANDS-ON → latihan, section "Bab 6 · Beresin Data Diri" · 🎓 NILAI A UNTUK BAB 6

Klik untuk membuka kunci setelah waktu habis.

➡️ "Data diri udah rapi. Tapi Raka punya 8 semester nilai, dan lowongannya makin banyak..."
-->

---
section: Bab 7 · Wadah Banyak Barang
bab: 7
mode: colab-demo
where: Materi · Bab 7
---

<div class="ghostnum">07</div>
<div class="eyebrow">// Bab 7 · Wadah banyak barang <span class="tag wajib">wajib</span></div>

## "8 semester = 8 variabel?" → <code>list</code>

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-1 items-start">
<div class="code-sm">

```python
ips = [3.20, 3.35, 3.50, 3.41,
       3.60, 3.52, 3.38, 3.65]   # semester 1-8

print(ips[0])      # 3.2 ← SAMA kayak string!
print(ips[-1])     # 3.65
print(ips[0:2])    # [3.2, 3.35]

print(len(ips), sum(ips) / len(ips))  # 8 3.45125
print(max(ips), min(ips))             # 3.65 3.2
print(sorted(ips, reverse=True))      # terbesar dulu

ips[3] = 3.45              # nilai direvisi: BISA diubah
lowongan = ["PT Data Maju", "PT Awan Biru"]
lowongan.append("CV Tiga Kode")  # nemu lowongan baru
```

</div>
<div class="stack">
  <div class="story small"><code>ips_semester_1</code> sampai <code>ips_semester_8</code>? Belum lagi daftar lowongan. 😵</div>
  <div class="card pop"><div class="box-h">List = daftar berurutan</div>Urut, bisa ditambah, bisa diubah.</div>
  <div class="card pop-yl small">Ilmu indexing string <b>dipakai lagi</b>. Bedanya: string <b>immutable</b>, list <b>mutable</b>.</div>
</div>
</div>

<!--
⏱️ 01:42 · 3,5 menit · 🧪 COLAB → materi, section "Bab 7 · Wadah Banyak Barang"

- Sebelum ips[0]: "Kalian udah tahu caranya dari Bab 6. Tebak?"
- Catatan: Raka ambil 18 SKS tiap semester, jadi rata-rata IPS = IPK (3.45).
- "sum() dan len() di list ini andalan Raka: 30 lowongan pun tetap satu baris."
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
TANGGAL_LAHIR = (12, 3, 2004)   # tgl, bln, thn

print(TANGGAL_LAHIR[2])          # 2004
print(2026 - TANGGAL_LAHIR[2])   # 22 (usia Raka)
TANGGAL_LAHIR[2] = 2005          # ❌ TypeError: 'tuple'
                                 #    object does not
                                 #    support item
                                 #    assignment
```

</div>
<div class="stack">
  <div class="card pop"><div style="font-size: 2.2rem">🔒</div>Kayak list yang <b>dikunci</b>. Pakai kurung biasa <code>( )</code>.</div>
  <div class="card soft">Cocok buat data yang memang <b>nggak boleh berubah</b>: tanggal lahir. Nggak bisa muda-in umur. 😄</div>
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
# skill dari CV, LinkedIn, portofolio (ada yang dobel)
semua_skill = ["Python", "Excel", "SQL",
               "Python", "Excel", "Tableau"]
skill_unik = set(semua_skill)
print(skill_unik)
# {'Python', 'Excel', 'SQL', 'Tableau'}
print(len(skill_unik))   # 4

skill_wajib = frozenset(["Python", "SQL"])  # dikunci
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

## <code>dict</code>: transkrip nilai

<div class="grid grid-cols-[1.35fr_1fr] gap-8 mt-1 items-start">
<div class="code-sm">

```python
transkrip = {
    "Statistika Dasar": "A",
    "Basis Data": "A-",
    "Pemrograman Python": "B+",
}
print(transkrip["Basis Data"])       # A- ← pakai KUNCI
transkrip["Machine Learning"] = "A"  # tambah matkul

print(transkrip["Kalkulus 3"])       # ❌ KeyError

biodata = {"nama": "Raka Pratama Putra", "ipk": 3.45}
print(biodata["ipk"])                # 3.45
```

</div>
<div class="stack">
  <div class="card pop-yl">
    <div class="box-h">📜 Transkrip</div>
    <div class="mono small">Statistika Dasar ..... A<br>Basis Data ........... A-<br>Pemrograman Python ... B+</div>
  </div>
  <div class="card pop small">List: cari pakai <b>nomor urut</b>. Dict: cari pakai <b>nama</b>. HRD nggak nanya "nilai mata kuliah nomor 2", tapi "nilai Basis Data berapa?"</div>
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
  <thead><tr><th>Wadah</th><th>Tanda</th><th>Urut?</th><th>Bisa diubah?</th><th>Duplikat?</th><th>Contoh Raka</th></tr></thead>
  <tbody>
    <tr><td><code>list</code></td><td><code>[ ]</code></td><td>✅</td><td>✅</td><td>✅</td><td>IPS per semester</td></tr>
    <tr><td><code>tuple</code></td><td><code>( )</code></td><td>✅</td><td>❌</td><td>✅</td><td>Tanggal lahir</td></tr>
    <tr><td><code>set</code></td><td><code>{ }</code></td><td>❌</td><td>✅</td><td>❌</td><td>Skill tanpa dobel</td></tr>
    <tr><td><code>dict</code></td><td><code>{k: v}</code></td><td>✅</td><td>✅</td><td>kunci ❌</td><td>Transkrip</td></tr>
  </tbody>
</table>

<div class="grid grid-cols-4 gap-4 mt-4 small">
  <div class="card flex justify-between items-center gap-2">Lowongan dilamar, urut tanggal<span v-click class="answer">list</span></div>
  <div class="card flex justify-between items-center gap-2">Koordinat kantor<span v-click class="answer">tuple</span></div>
  <div class="card flex justify-between items-center gap-2">Perusahaan unik yang dilamar<span v-click class="answer">set</span></div>
  <div class="card flex justify-between items-center gap-2">Gaji per posisi<span v-click class="answer">dict</span></div>
</div>

<div class="mt-4"><Transkrip :done="7" :stamping="7" compact /></div>

<!--
⏱️ 2 menit · kuis cepat, jawab serentak / di chat · 🎓 NILAI A UNTUK BAB 7

dict menyimpan urutan dimasukkan (Python 3.7+).

➡️ "Semua data udah rapi di wadahnya. Tinggal satu: MENYAJIKAN lamarannya ke HRD."
-->

---
section: Bab 8 · Surat Lamaran Rapi
bab: 8
mode: colab-demo
where: Materi · Bab 8
---

<div class="ghostnum">08</div>
<div class="eyebrow">// Bab 8 · Surat lamaran rapi <span class="tag paham">paham</span></div>

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
print("Lampiran:", "Ijazah", "Transkrip", sep=" | ")
print("Hal:\tLamaran \"Data Analyst\"\nLampiran:\t3 berkas")
```

<div class="code-yl">

```text
Lampiran: | Ijazah | Transkrip
Hal:	Lamaran "Data Analyst"
Lampiran:	3 berkas
```

</div>
</div>
</div>

<!--
⏱️ 01:52 · 2 menit · 🧪 COLAB → materi, section "Bab 8 · Surat Lamaran Rapi"

Jebakan klasik (ceritakan saja): print("C:\data\new") → \n jadi baris baru. Solusi: "C:\\data\\new" atau raw string r"C:\data\new".
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8</div>

## Raka mencoba bikin surat...

<div class="grid grid-cols-[1.3fr_1fr] gap-8 mt-6 items-center">
<div class="code-lg code-err">

```python
ipk = 3.45
print("IPK saya: " + ipk)
```

</div>
<div class="card err">
<div class="box-h" style="color: var(--err)">TypeError</div>
<code>can only concatenate str (not "float") to str</code>
</div>
</div>

<div class="story mt-10">Teks + angka = nggak bisa digabung langsung. Ternyata Python punya beberapa solusi dari zaman ke zaman...</div>

<!--
⏱️ 1 menit
-->

---

<div class="eyebrow">// Bab 8 <span class="tag wajib">f-string wajib</span> <span class="tag kenalan">% & .format kenalan</span></div>

## Evolusi string formatting

```python
print("IPK saya: " + str(ipk))     # 1. casting manual → ribet
print("IPK saya: %.2f" % ipk)      # 2. gaya %  (jadul)
print("IPK saya: {}".format(ipk))  # 3. .format()
print(f"IPK saya: {ipk}")          # 4. f-string ⭐ pakai ini!
```

<div class="grid grid-cols-[1fr_1.3fr] gap-8 mt-6 items-center">
  <div class="card soft">Semua hasilnya sama: <code>IPK saya: 3.45</code></div>
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
    <tr><td>Variabel</td><td><code>f"{perusahaan}"</code></td><td>PT Data Maju</td></tr>
    <tr><td>Hitungan</td><td><code>f"{total_mutu / total_sks}"</code></td><td>3.4513...</td></tr>
    <tr><td>Ribuan</td><td><code>f"{GAJI_HARAPAN:,}"</code></td><td>6,500,000</td></tr>
    <tr><td>2 desimal</td><td><code>f"{3.451388:.2f}"</code></td><td>3.45</td></tr>
    <tr><td>Method</td><td><code>f"{posisi.upper()}"</code></td><td>DATA ANALYST</td></tr>
  </tbody>
</table>
<div class="code-sm">

```python
perusahaan = "PT Data Maju"
print(f"Yth. HRD {perusahaan},")  # nggak ketuker lagi!

print(f"Gaji: Rp{GAJI_HARAPAN:,}")
# Rp6,500,000  (gaya Inggris)
print(f"Gaji: Rp{GAJI_HARAPAN:,}".replace(",", "."))
# Rp6.500.000  (gaya Indonesia!)
print(f"IPK : {total_mutu / total_sks:.2f}")  # 3.45
```

</div>
</div>

<div class="card pop-yl mt-4">Ingat insiden <i>"Yth. HRD PT Awan Biru"</i>? Sekarang nama perusahaan diambil dari <b>variabel</b>. Dan trik <code>.replace(",", ".")</code> itu string method dari Bab 6. 🧩</div>

<!--
⏱️ 3 menit

"Template surat dengan f-string: ganti satu variabel perusahaan, semua surat ikut benar. Insiden PT Awan Biru nggak akan terulang."
-->

---
mode: colab-demo
where: Materi · Bab 8
---

<div class="eyebrow">// Bab 8 <span class="tag wajib">wajib</span></div>

## <code>input()</code>: biar kartunya bisa diisi

<div class="grid grid-cols-[1fr_1.15fr] gap-8 mt-1 items-start">
<div class="stack">

```python
perusahaan = input("Nama perusahaan: ")
print(f"Yth. HRD {perusahaan},")
```

<div class="card soft small">Di Colab muncul kotak isian, cell "berputar" sampai kamu tekan <span class="kbd">Enter</span>. Bukan hang!</div>
<div v-click="2">
<div class="box-h">Perbaikan: casting dari Bab 6</div>

```python
jumlah = int(input("Sudah melamar? "))
print(jumlah * 2)    # 20
```

</div>
</div>
<Predict :options="['20', '1010', 'Error']" :answer="1" note="input() SELALU menghasilkan string">

```python
jumlah = input("Sudah melamar? ")  # ketik: 10
print(jumlah * 2)  # target 2x lipat
```

</Predict>
</div>

<!--
⏱️ 2,5 menit · momen paling berkesan, JANGAN dilewati

"Raka sudah melamar 10 lowongan, targetnya bulan depan 2x lipat."
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
  <li>Minta nama perusahaan & posisi lewat <code>input()</code>, rapikan posisi pakai <code>.strip().title()</code></li>
  <li>Cetak header seperti di kanan</li>
  <li>Cetak ekspektasi gaji format Rupiah: <code>Rp6.500.000</code></li>
  <li><span class="tag paham">bonus</span> Cetak pembuka surat: <code>Yth. HRD ...</code></li>
</ol>
</div>
<div class="stack">
<div class="code-yl">

```text
==============================================
KARTU LAMARAN RAKA
Perusahaan : PT Data Maju
Posisi     : Data Analyst
==============================================
Ekspektasi gaji : Rp6.500.000
```

</div>
<div class="sticker tk" style="align-self: flex-start">8/8 nilai A → saatnya wisuda!</div>
</div>
</div>

<div class="mt-4"><Transkrip :done="8" :stamping="8" compact /></div>

<!--
⏱️ 4,5 menit · 🎯 HANDS-ON → latihan, section "Bab 8 · Surat Lamaran Rapi" · 🎓 NILAI A UNTUK BAB 8

Kunci ada di 03_kunci_jawaban.ipynb.

➡️ "8 nilai A. Saatnya ujian akhir: KARTU LAMARAN OTOMATIS RAKA."
-->

---
section: Final · Satu Klik, Lamaran Jadi
bab: 9
---

<div class="eyebrow">// Final · Satu klik, lamaran jadi</div>

## Misi: Kartu Lamaran Raka v1.0

<div class="grid grid-cols-[1.15fr_1fr] gap-8 items-start">
<div class="code-xs">

```text
==============================================
       KARTU LAMARAN RAKA PRATAMA PUTRA
==============================================
Perusahaan       : PT DATA MAJU
Posisi           : Data Analyst
----------------------------------------------
Nama             : Raka Pratama Putra (22 th)
Jurusan          : Statistika
Nomor ijazah     : IJZ-20260915-STA-0457
Tanggal lulus    : 15-09-2026 (lulusan ke-457)
----------------------------------------------
IPK              : 3.45
Ekspektasi gaji  : Rp6.500.000
Memenuhi syarat? : True
==============================================
Yth. HRD PT DATA MAJU,
saya Raka Pratama Putra, lulusan Statistika
Universitas Kenanga Raya dengan IPK 3.45,
ingin melamar posisi Data Analyst.
```

</div>
<div class="stack">
  <div class="card tk"><div class="box-h">🟢 Wajib</div>Isi semua <code>___</code> di template sampai kartu tampil.</div>
  <div class="card yl"><div class="box-h">🟡 Bonus</div>Tambah baris "Cum laude?"<br><span class="small">hint: IPK &gt; 3.50 <b>and</b> lama studi &lt;= 4</span></div>
  <div class="card"><div class="box-h">🔴 Tantangan</div>Rata-rata IPS 4 semester terakhir.<br><span class="small">hint: <code>ips[-4:]</code>, <code>sum</code>, <code>len</code></span></div>
</div>
</div>

<!--
⏱️ 02:07 · 2 menit

"Perhatikan: tiap baris kartu ini pakai sesuatu yang kalian pelajari hari ini. Coba tebak, baris 'Tanggal lulus' pakai ilmu dari bab berapa?" (Bab 6: slicing nomor ijazah)
-->

---
mode: hands-on
where: Latihan · Final
---

<div class="eyebrow">// Final</div>

## 🎯 Kerjakan!

<div class="grid grid-cols-[1fr_1.1fr] gap-8 mt-2">
<div class="stack">
  <Goto to="hands-on" where="Latihan · section Final · Kartu Lamaran v1.0" href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/02_latihan_peserta.ipynb" />
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
⏱️ 10 menit · 🎯 HANDS-ON → latihan, section "Final · Kartu Lamaran v1.0"

- Keliling / buka breakout room. Prioritaskan peserta 🔴.
- Yang selesai cepat → 🟡/🔴, atau jadi "asisten" teman sebelah.
- Menit ke-8: "2 menit lagi".
-->

---
mode: vscode
where: lamaran-raka/kartu_lamaran.py
---

<div class="eyebrow">// Final · Momen "aha"</div>

## Dari notebook ke script

<div class="grid grid-cols-[1fr_1.1fr] gap-10 mt-4 items-center">
<div>

```bash
cd lamaran-raka
python3 kartu_lamaran.py
```

<div class="mt-6"><Goto to="vscode" where="buka lamaran-raka/kartu_lamaran.py, jalankan" /></div>
</div>
<div class="stack">
  <div class="flowrow" style="gap: 16px">
    <div class="huge" style="font-size: 3.4rem; text-decoration: line-through; text-decoration-thickness: 6px; text-decoration-color: var(--err)">90 mnt</div>
    <div class="arw" style="font-size: 2.6rem">➜</div>
    <div class="huge" style="font-size: 3.4rem"><span class="hl-tk">1 dtk</span></div>
  </div>
  <div class="card pop-yl lead" style="color: var(--fg)">Nggak ada lagi <i>"Yth. HRD PT Awan Biru"</i>. Satu script untuk lowongan mana pun. Dan yang nulis kodenya... <b>kalian</b>.</div>
</div>
</div>

<!--
⏱️ 3 menit · 💻 PINDAH KE VSCODE → lamaran-raka/kartu_lamaran.py (sudah disiapkan)

- Jalankan 2x dengan lowongan berbeda: PT Data Maju (IPK min 3.00 → True) lalu PT Awan Biru (IPK min 3.50 → False).
- "Ini yang sekarang dijalankan Raka tiap ada lowongan baru. Satu perintah."
- Show & tell: 1–2 peserta share screen hasil mereka (terutama yang mengerjakan bonus). Beri apresiasi.
-->

---
section: Epilog · Bersambung...
bab: 10
---

<div class="eyebrow">// Epilog · Isi tas Raka</div>

## Yang kalian kuasai hari ini

<table class="dense">
  <thead><tr><th>Masalah Raka</th><th>Alat yang dipakai</th><th>Bab</th></tr></thead>
  <tbody>
    <tr><td>Data diri berserakan</td><td>Variabel & konstanta</td><td>4</td></tr>
    <tr><td>Hitung IPK, lama studi</td><td>Operator, <code>round</code> <code>max</code> <code>min</code></td><td>5</td></tr>
    <tr><td>Cek syarat lowongan</td><td>Boolean & perbandingan</td><td>5</td></tr>
    <tr><td>Nama beda-beda di tiap dokumen</td><td><code>.strip()</code> <code>.title()</code></td><td>6</td></tr>
    <tr><td>Ambil info dari nomor ijazah</td><td>Indexing, slicing, <code>int()</code></td><td>6</td></tr>
    <tr><td>Nilai per semester, transkrip</td><td><code>list</code>, <code>dict</code>, <code>sum</code>, <code>len</code></td><td>7</td></tr>
    <tr><td>Surat & kartu lamaran rapi</td><td>f-string, <code>\t</code>, <code>"=" * 46</code>, <code>input()</code></td><td>8</td></tr>
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
  <div class="card pop"><div class="box-h">😐 "Data lowongan masih diketik manual."</div><b>→ Baca file CSV/Excel</b> pakai pandas</div>
  <div class="card pop-yl"><div class="box-h">🏅 "Predikatku apa: cum laude, sangat memuaskan?"</div><b>→ <code>if</code> / <code>elif</code> / <code>else</code></b>: boolean jadi otaknya</div>
  <div class="card pop"><div class="box-h">🔁 "30 lowongan = jalanin script 30 kali?"</div><b>→ Loop</b> <code>for</code></div>
  <div class="card pop-yl"><div class="box-h">♻️ "Pengen bikin mesin cek_syarat() sendiri."</div><b>→ Function</b> buatan sendiri</div>
</div>

<div class="mt-8 flex items-center gap-6">
  <div class="huge" style="font-size: 3rem">Bersambung...</div>
  <span class="sticker">🎓 pertemuan berikutnya</span>
</div>

<!--
⏱️ 2 menit

"Kalian sendiri ngerasain kan: tiap lowongan baru, script harus dijalankan ulang dan diisi ulang. Bayangin 30 lowongan."
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
  <li>Baris "Cum laude?" di kartu lamaran</li>
  <li>Rata-rata IPS 4 semester terakhir (2 desimal)</li>
  <li>Bikin kartu untuk PT Awan Biru (IPK min 3.50) dan CV Tiga Kode (2.75). <b>Rasakan</b> berapa kali harus jalanin ulang. 😉</li>
</ol>
</div>
</div>

<!--
⏱️ 2 menit

PR nomor 3 sengaja bikin peserta MERASAKAN repotnya tanpa loop → motivasi alami materi berikutnya.
Bonus cerita: "Portofolio GitHub berisi script seperti ini juga nilai plus waktu melamar kerja."
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

<div class="eyebrow">// Terima kasih 🎓</div>

# Selamat, kalian <span class="hl">lulus</span>.

<div class="grid grid-cols-[1.5fr_1fr] gap-8 mt-6 items-start" style="max-width: 980px">
  <Transkrip :done="8" />
  <div class="stack small">
    <a href="https://github.com/thosangs/python_lecture" target="_blank">📦 Repo: notebook, script, slide</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/01_materi_ijazah_raka.ipynb" target="_blank">📓 Materi lengkap (Colab)</a>
    <a href="https://colab.research.google.com/github/thosangs/python_lecture/blob/main/notebooks/03_kunci_jawaban.ipynb" target="_blank">🔑 Kunci jawaban (Colab)</a>
    <span>👥 Komunitas: PythonID · PyCon ID</span>
  </div>
</div>

<div class="lead mt-6">Error akan terus datang. Itu tanda kalian <b>sedang belajar</b>, bukan tanda kalian nggak bisa.</div>

<!--
⏱️ 1 menit · Q&A
-->
