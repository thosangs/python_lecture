# Slides: Ijazah Raka

Deck [Slidev](https://sli.dev) untuk kelas Python pemula (2,5 jam). Tema neo-brutalist, dark mode default (toggle `d` untuk light), warna kedua toska, aksen kuning.

```bash
npm install
npm run dev        # http://localhost:3030 · presenter: /presenter
npm run build      # → dist/ (di CI: --base /<nama-repo>/)
```

- `slides.md`: 69 slide, nomornya sama dengan [panduan trainer](../python_dbb_alur_slide.md). Catatan trainer ada di komentar `<!-- -->` tiap slide (tampil di mode presenter).
- Frontmatter per slide yang dipakai navigasi:
  - `section` + `bab`: dipasang di slide pertama tiap bab
  - `mode`: `colab-demo` · `hands-on` · `vscode` · `break`
  - `where`: section notebook yang dibuka, misalnya `Materi · Bab 4`
  - `footer: false`: sembunyikan footer
- Komponen: `<Transkrip :done="3" :stamping="3" compact />`, `<Goto to="hands-on" where="..." href="..." />`, `<Predict :options="[...]" :answer="1">kode</Predict>`, `<IndexStrip text="..." :sels="['[0:3]']" />` (butuh `clicks: N` di frontmatter), `<Folder label value type />`, `<Countdown :minutes="10" />`.
- `vite.config.ts`: mematikan CSS minify. Ini workaround bug Slidev v53 + Vite 8, yang membuat build gagal di lightningcss.
