<script setup>
// Kartu Stempel Kopi Senja: 8 bab = 8 stempel, stempel ke-9 = kopi gratis (laporan otomatis)
defineProps({
  done: { type: Number, default: 0 },      // jumlah bab yang sudah dicap
  stamping: { type: Number, default: 0 },  // bab yang baru dicap di slide ini (animasi)
  compact: { type: Boolean, default: false },
})
const babs = [
  'Kenapa Ngoding', 'Kenalan Python', 'Meja Kerja', 'Toples Berlabel',
  'Ngitung Omzet', 'Beresin Menu', 'Wadah Barang', 'Laporan Bu Sari',
]
</script>

<template>
  <div class="stampcard" :class="{ compact }">
    <div class="sc-head">
      <span>☕ Kartu Stempel Kopi Senja</span>
      <span class="sc-count">{{ done }}/8</span>
    </div>
    <div class="sc-grid">
      <div
        v-for="(name, i) in babs"
        :key="i"
        class="sc-cell"
        :class="{ done: i + 1 <= done, now: i + 1 === stamping }"
      >
        <div class="sc-no">{{ String(i + 1).padStart(2, '0') }}</div>
        <div class="sc-name">{{ name }}</div>
        <div v-if="i + 1 <= done" class="sc-stamp">✓</div>
      </div>
      <div class="sc-cell reward" :class="{ done: done >= 8 }">
        <div class="sc-no">☕</div>
        <div class="sc-name">Gratis: laporan otomatis</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.stampcard {
  border: 3px solid var(--border);
  border-radius: 12px;
  background: var(--surface);
  box-shadow: 6px 6px 0 var(--yl);
  padding: 12px 14px 14px;
}
.sc-head {
  display: flex;
  justify-content: space-between;
  font-family: var(--f-mono);
  font-weight: 800;
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 10px;
}
.sc-count { color: var(--tk-strong); }
.sc-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 9px; }
.sc-cell {
  position: relative;
  border: 2.5px dashed var(--line);
  border-radius: 9px;
  padding: 7px 8px;
  min-height: 62px;
}
.sc-no { font-family: var(--f-display); font-size: 1.15rem; line-height: 1; color: var(--muted); }
.sc-name { font-size: 0.7rem; font-weight: 600; line-height: 1.2; margin-top: 4px; }
.sc-cell.done { border: 2.5px solid var(--border); background: var(--tk-soft); }
.sc-cell.done .sc-no { color: var(--tk-strong); }
.sc-stamp {
  position: absolute;
  right: 6px;
  bottom: 4px;
  width: 30px;
  height: 30px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  border: 3px solid var(--border);
  background: var(--tk);
  color: var(--on-accent);
  font-weight: 800;
  transform: rotate(-12deg);
}
.sc-cell.now .sc-stamp { animation: stamp-in 0.55s cubic-bezier(.2, 1.6, .4, 1) 0.25s both; }
.sc-cell.now { border-color: var(--yl); box-shadow: 0 0 0 3px var(--yl); }
.reward { border-style: solid; border-color: var(--yl); }
.reward .sc-no { color: inherit; }
.reward.done { background: var(--yl); color: var(--on-accent); }
.compact .sc-grid { grid-template-columns: repeat(9, 1fr); gap: 6px; }
.compact .sc-cell { min-height: 46px; padding: 5px 6px; }
.compact .sc-name { font-size: 0.6rem; }
.compact .sc-stamp { width: 22px; height: 22px; font-size: 0.7rem; right: 4px; bottom: 3px; }
@keyframes stamp-in {
  from { transform: scale(2.6) rotate(-35deg); opacity: 0; }
  to { transform: scale(1) rotate(-12deg); opacity: 1; }
}
</style>
