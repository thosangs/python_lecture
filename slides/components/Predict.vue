<script setup>
// Kartu "Tebak output": opsi tampil dulu, jawaban terbuka setelah 1 klik
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  options: { type: Array, required: true },
  answer: { type: Number, required: true },   // index opsi yang benar (0 = A)
  at: { type: Number, default: 1 },           // klik ke berapa jawaban dibuka
  note: { type: String, default: '' },
})
const { $clicks } = useSlideContext()
const revealed = computed(() => $clicks.value >= props.at)
</script>

<template>
  <div class="predict">
    <div class="p-head">🤔 Tebak output</div>
    <div class="p-code"><slot /></div>
    <div class="p-opts">
      <div
        v-for="(o, i) in options"
        :key="i"
        class="p-opt"
        :class="{ right: revealed && i === answer, dim: revealed && i !== answer }"
      >
        <b>{{ 'ABCD'[i] }}</b><span>{{ o }}</span>
      </div>
    </div>
    <div v-click="at" class="p-note">✅ {{ 'ABCD'[answer] }}<template v-if="note"> · {{ note }}</template></div>
  </div>
</template>

<style scoped>
.predict {
  border: 3px solid var(--border);
  border-radius: 12px;
  background: var(--surface);
  box-shadow: 6px 6px 0 var(--yl);
  padding: 12px 14px;
}
.p-head { font-family: var(--f-mono); font-weight: 800; font-size: 0.74rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--tk-strong); margin-bottom: 6px; }
.p-code :deep(.slidev-code-wrapper) { margin: 0 0 10px; }
.p-code :deep(.slidev-code) { box-shadow: none !important; }
.p-opts { display: flex; gap: 10px; flex-wrap: wrap; }
.p-opt {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 5px 12px 5px 6px;
  border: 2.5px solid var(--border);
  border-radius: 8px;
  font-family: var(--f-mono);
  font-weight: 600;
  font-size: 0.86rem;
  white-space: pre;
  transition: all 0.25s;
}
.p-opt b {
  display: grid;
  place-items: center;
  width: 22px;
  height: 22px;
  border-radius: 5px;
  background: var(--fg);
  color: var(--bg);
  font-size: 0.74rem;
}
.p-opt.right { background: var(--tk); color: var(--on-accent); transform: rotate(-2deg) scale(1.06); box-shadow: 4px 4px 0 var(--shadow); }
.p-opt.right b { background: var(--on-accent); color: var(--tk); }
.p-opt.dim { opacity: 0.35; }
.p-note { margin-top: 10px; font-weight: 600; font-size: 0.9rem; }
</style>
