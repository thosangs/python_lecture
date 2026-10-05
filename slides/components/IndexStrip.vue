<script setup>
// Visual indexing & slicing string. Tiap klik menyorot satu ekspresi dari `sels`.
// Contoh: <IndexStrip text="TRX-20261005-JKT-0170" :sels="['[0:3]', '[4:12]']" />
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const props = defineProps({
  text: { type: String, required: true },
  sels: { type: Array, default: () => [] },
  name: { type: String, default: 'kode_trx' },
  neg: { type: Boolean, default: true },
})
const { $clicks } = useSlideContext()
const chars = computed(() => [...props.text])
const n = computed(() => chars.value.length)

function toNum(v) { return v === '' || v === undefined ? null : Number(v) }

// Index yang terambil, mengikuti aturan slicing Python
function pick(sel) {
  const body = sel.replace(/^\[|\]$/g, '')
  const len = n.value
  if (!body.includes(':')) {
    const i = Number(body)
    const idx = i < 0 ? len + i : i
    return idx >= 0 && idx < len ? [idx] : []
  }
  const [a, b, c] = body.split(':').map(toNum)
  const step = c ?? 1
  const out = []
  if (step > 0) {
    const s = a === null ? 0 : a < 0 ? Math.max(len + a, 0) : Math.min(a, len)
    const e = b === null ? len : b < 0 ? Math.max(len + b, 0) : Math.min(b, len)
    for (let i = s; i < e; i += step) out.push(i)
  }
  else {
    const s = a === null ? len - 1 : a < 0 ? len + a : Math.min(a, len - 1)
    const e = b === null ? -1 : b < 0 ? len + b : b
    for (let i = s; i > e; i += step) out.push(i)
  }
  return out
}

const active = computed(() => {
  const k = $clicks.value
  return k >= 1 && k <= props.sels.length ? props.sels[k - 1] : null
})
const picked = computed(() => (active.value ? pick(active.value) : []))
const result = computed(() => picked.value.map(i => chars.value[i]).join(''))
</script>

<template>
  <div class="istrip">
    <span v-for="k in sels.length" :key="k" v-click="k" class="trigger" />
    <div class="row lab"><span class="rl">index +</span><span v-for="(_, i) in chars" :key="i" class="cell idx">{{ i }}</span></div>
    <div class="row">
      <span class="rl">karakter</span>
      <span
        v-for="(ch, i) in chars"
        :key="i"
        class="cell ch"
        :class="{ on: picked.includes(i), first: picked[0] === i }"
      >{{ ch }}</span>
    </div>
    <div v-if="neg" class="row lab"><span class="rl">index −</span><span v-for="(_, i) in chars" :key="i" class="cell idx">{{ i - n }}</span></div>
    <div class="expr">
      <template v-if="active">
        <code>{{ name }}{{ active }}</code>
        <span class="arw">→</span>
        <code class="res">'{{ result }}'</code>
      </template>
      <span v-else class="hint">klik ➜ untuk mencoba ekspresi</span>
    </div>
  </div>
</template>

<style scoped>
.istrip { font-family: var(--f-mono); }
.trigger { display: none; }
.row { display: flex; align-items: center; gap: 3px; }
.rl { width: 62px; flex: 0 0 62px; font-size: 0.66rem; font-weight: 800; text-transform: uppercase; color: var(--muted); letter-spacing: 0.04em; }
.cell { width: 36px; flex: 0 0 36px; text-align: center; }
.idx { font-size: 0.72rem; color: var(--muted); padding: 3px 0; }
.ch {
  height: 40px;
  line-height: 34px;
  font-size: 1.15rem;
  font-weight: 800;
  border: 3px solid var(--border);
  border-radius: 7px;
  background: var(--surface);
  transition: all 0.2s;
}
.ch.on { background: var(--yl); color: var(--on-accent); transform: translateY(-4px); box-shadow: 0 4px 0 var(--border); }
.expr { margin: 14px 0 0 65px; display: flex; align-items: center; gap: 12px; min-height: 38px; font-size: 1.1rem; }
.expr code { font-size: 1.05rem !important; padding: 4px 10px !important; }
.expr .res { background: var(--yl) !important; color: var(--on-accent) !important; border-color: var(--border) !important; }
.arw { font-family: var(--f-display); color: var(--tk-strong); font-size: 1.3rem; }
.hint { color: var(--muted); font-size: 0.85rem; }
</style>
