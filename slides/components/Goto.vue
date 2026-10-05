<script setup>
// Penanda "pindah ke mana" yang besar, buat trainer & peserta
import { computed } from 'vue'

const props = defineProps({
  to: { type: String, default: 'colab' },   // colab | hands-on | vscode | break | slide
  where: { type: String, default: '' },
  href: { type: String, default: '' },
})
const MAP = {
  'colab': ['🧪', 'Pindah ke Colab', 'trainer live coding, kalian boleh ikut ngetik'],
  'hands-on': ['🎯', 'Hands-on', 'giliran kalian ngetik'],
  'vscode': ['💻', 'Pindah ke VSCode', 'demo trainer'],
  'break': ['⏸️', 'Istirahat', ''],
  'slide': ['🖥️', 'Balik ke slide', ''],
}
const info = computed(() => MAP[props.to] ?? MAP.colab)
</script>

<template>
  <component :is="href ? 'a' : 'div'" class="goto" :class="to" :href="href || undefined" target="_blank">
    <span class="g-ico">{{ info[0] }}</span>
    <span class="g-txt">
      <b>{{ info[1] }}</b>
      <small>{{ where || info[2] }}</small>
    </span>
    <span class="g-arrow">➜</span>
  </component>
</template>

<style scoped>
.goto {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 8px 16px 8px 12px;
  border: 3px solid var(--border) !important;
  border-radius: 12px;
  background: var(--tk);
  color: var(--on-accent) !important;
  box-shadow: 5px 5px 0 var(--shadow);
  text-decoration: none;
}
.goto.hands-on { background: var(--yl); }
.goto.vscode, .goto.break, .goto.slide { background: var(--surface-2); color: var(--fg) !important; }
.g-ico { font-size: 1.6rem; line-height: 1; }
.g-txt { display: flex; flex-direction: column; line-height: 1.15; }
.g-txt b { font-family: var(--f-mono); font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; font-size: 0.86rem; }
.g-txt small { font-size: 0.78rem; opacity: 0.8; }
.g-arrow { font-family: var(--f-display); font-size: 1.3rem; margin-left: 4px; }
</style>
