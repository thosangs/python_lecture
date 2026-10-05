<script setup>
// Navigasi per slide (terinspirasi footer dbt_lecture):
// bab aktif · progres transkrip · penanda lokasi (Colab/VSCode/Hands-on) · nomor slide
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $page, $nav, $frontmatter } = useSlideContext()

const total = computed(() => $nav.value.total)
const fm = computed(() => $frontmatter ?? {})

// section & bab = frontmatter `section` / `bab` dari slide terdekat di atas (atau slide ini)
const current = computed(() => {
  let section = ''
  let bab = 0
  for (const r of $nav.value.slides) {
    const f = r?.meta?.slide?.frontmatter ?? {}
    if (r.no > $page.value) break
    if (f.section) section = f.section
    if (typeof f.bab === 'number') bab = f.bab
  }
  return { section, bab }
})

const MODES = {
  'colab-demo': { icon: '🧪', label: 'Colab · demo' },
  'hands-on': { icon: '🎯', label: 'Hands-on' },
  'vscode': { icon: '💻', label: 'VSCode' },
  'break': { icon: '⏸️', label: 'Istirahat' },
}
const mode = computed(() => MODES[fm.value.mode])
const show = computed(() => fm.value.footer !== false && $page.value > 1 && $page.value < total.value)
const pad = n => String(n).padStart(2, '0')
</script>

<template>
  <div v-if="show" class="deck-nav">
    <div class="sec"><span class="tick">■</span>{{ current.section }}</div>
    <div class="stamps" :title="`Transkrip: ${Math.min(current.bab - 1, 8)}/8 lulus`">
      <span
        v-for="i in 8"
        :key="i"
        class="st"
        :class="{ done: i < current.bab, now: i === current.bab }"
      />
    </div>
    <div class="right">
      <span v-if="mode" class="mode" :class="fm.mode">
        {{ mode.icon }} {{ mode.label }}<template v-if="fm.where"> · {{ fm.where }}</template>
      </span>
      <span class="pg">{{ pad($page) }}<span class="sep">/</span>{{ pad(total) }}</span>
    </div>
  </div>
</template>

<style scoped>
.deck-nav {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 30px;
  padding: 0 16px 0 18px;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--fg);
  background: var(--surface);
  border-top: 3px solid var(--border);
  z-index: 20;
  pointer-events: none;
}
.sec { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.tick { color: var(--tk-strong); margin-right: 8px; }
.stamps { display: flex; gap: 5px; }
.st {
  width: 13px; height: 13px;
  border: 2px solid var(--border);
  border-radius: 3px;
}
.st.done { background: var(--tk); }
.st.now { background: var(--yl); }
.right { display: flex; justify-content: flex-end; align-items: center; gap: 12px; min-width: 0; }
.mode {
  padding: 2px 9px;
  border: 2px solid var(--border);
  border-radius: 999px;
  color: var(--on-accent);
  background: var(--tk);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  text-transform: none;
  letter-spacing: 0.02em;
}
.mode.hands-on { background: var(--yl); }
.mode.vscode { background: var(--surface-2); color: var(--fg); }
.mode.break { background: var(--surface-2); color: var(--fg); }
.pg { white-space: nowrap; }
.sep { color: var(--muted); margin: 0 3px; }
</style>
