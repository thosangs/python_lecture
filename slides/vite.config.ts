import { defineConfig } from 'vite'

export default defineConfig({
  build: {
    // Slidev v53 + Vite 8: minifier lightningcss menolak CSS bawaan Slidev
    // (`--uno: ... dark-text-gray-600` jadi rule bersarang), dan Vite 8 tidak
    // lagi membawa esbuild. CSS dibiarkan tanpa minify (ukurannya tetap kecil).
    cssMinify: false,
  },
})
