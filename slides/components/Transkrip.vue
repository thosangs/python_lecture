<script setup>
// Transkrip kelas: 8 bab = 8 mata kuliah, tiap bab selesai dapat nilai "A".
// Semua lulus → LULUS 🎓 = kartu lamaran otomatis.
defineProps({
  done: { type: Number, default: 0 },      // jumlah bab yang sudah lulus
  stamping: { type: Number, default: 0 },  // bab yang baru dinilai di slide ini (animasi)
  compact: { type: Boolean, default: false },
})
const babs = [
  'Kenapa Ngoding', 'Kenalan Python', 'Meja Kerja', 'Map Berlabel',
  'Ngitung IPK', 'Data Diri', 'Wadah Barang', 'Surat Lamaran',
]
</script>

<template>
  <div class="transkrip" :class="{ compact }">
    <div class="tr-head">
      <span>🎓 Transkrip Kelas Python</span>
      <span class="tr-count">{{ done }}/8 lulus</span>
    </div>
    <div class="tr-grid">
      <div
        v-for="(name, i) in babs"
        :key="i"
        class="tr-cell"
        :class="{ done: i + 1 <= done, now: i + 1 === stamping }"
      >
        <div class="tr-no">PY-{{ String(i + 1).padStart(2, '0') }}</div>
        <div class="tr-name">{{ name }}</div>
        <div v-if="i + 1 <= done" class="tr-grade">A</div>
      </div>
      <div class="tr-cell reward" :class="{ done: done >= 8 }">
        <div class="tr-no">🎓</div>
        <div class="tr-name">{{ done >= 8 ? 'LULUS!' : compact ? 'Lulus' : 'Lulus = kartu lamaran otomatis' }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.transkrip {
  border: 3px solid var(--border);
  border-radius: 12px;
  background: var(--surface);
  box-shadow: 6px 6px 0 var(--yl);
  padding: 12px 14px 14px;
}
.tr-head {
  display: flex;
  justify-content: space-between;
  font-family: var(--f-mono);
  font-weight: 800;
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.tr-count { color: var(--tk-strong); }
.tr-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 11px; padding-top: 4px; }
.tr-cell {
  position: relative;
  border: 2.5px dashed var(--line);
  border-radius: 9px;
  padding: 7px 8px;
  min-height: 62px;
}
.tr-no { font-family: var(--f-mono); font-weight: 800; font-size: 0.72rem; line-height: 1; color: var(--muted); }
.tr-name { font-size: 0.7rem; font-weight: 600; line-height: 1.2; margin-top: 5px; }
.tr-cell.done { border: 2.5px solid var(--border); background: var(--tk-soft); }
.tr-cell.done .tr-no { color: var(--tk-strong); }
.tr-grade {
  position: absolute;
  right: -8px;
  top: -9px;
  width: 28px;
  height: 28px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 3px solid var(--border);
  background: var(--tk);
  color: var(--on-accent);
  font-family: var(--f-display);
  font-size: 0.95rem;
  transform: rotate(-12deg);
}
.tr-cell.now .tr-grade { animation: grade-in 0.55s cubic-bezier(.2, 1.6, .4, 1) 0.25s both; }
.tr-cell.now { border-color: var(--yl); box-shadow: 0 0 0 3px var(--yl); }
.reward { border-style: solid; border-color: var(--yl); }
.reward .tr-no { font-size: 1.1rem; color: inherit; }
.reward.done { background: var(--yl); color: var(--on-accent); }
.reward.done .tr-name { font-family: var(--f-display); font-size: 0.95rem; }
.compact .tr-grid { grid-template-columns: repeat(9, 1fr); gap: 6px; }
.compact .tr-cell { min-height: 46px; padding: 5px 6px; }
.compact .tr-name { font-size: 0.6rem; }
.compact .tr-grade { width: 21px; height: 21px; font-size: 0.66rem; right: -6px; top: -8px; border-width: 2.5px; }
@keyframes grade-in {
  from { transform: scale(2.6) rotate(-35deg); opacity: 0; }
  to { transform: scale(1) rotate(-12deg); opacity: 1; }
}
</style>
