<script setup>
// Timer istirahat: klik untuk mulai / jeda, klik dua kali untuk reset
import { computed, onUnmounted, ref } from 'vue'

const props = defineProps({
  minutes: { type: Number, default: 10 },
  small: { type: Boolean, default: false },
})
const left = ref(props.minutes * 60)
const running = ref(false)
let timer = null

const mmss = computed(() => {
  const m = Math.floor(left.value / 60)
  const s = left.value % 60
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`
})

function toggle() {
  if (running.value) {
    clearInterval(timer)
    running.value = false
    return
  }
  running.value = true
  timer = setInterval(() => {
    if (left.value > 0) left.value--
    else { clearInterval(timer); running.value = false }
  }, 1000)
}
function reset() {
  clearInterval(timer)
  running.value = false
  left.value = props.minutes * 60
}
onUnmounted(() => clearInterval(timer))
</script>

<template>
  <button class="countdown" :class="{ running, over: left === 0, small }" @click="toggle" @dblclick="reset">
    <span class="time">{{ mmss }}</span>
    <span class="hint">{{ left === 0 ? 'waktunya balik! ☕' : running ? 'klik = jeda' : 'klik = mulai · dobel klik = reset' }}</span>
  </button>
</template>

<style scoped>
.countdown {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  padding: 14px 34px 12px;
  border: 4px solid var(--border);
  border-radius: 16px;
  background: var(--surface);
  color: var(--fg);
  box-shadow: 8px 8px 0 var(--tk);
  cursor: pointer;
}
.countdown.running { box-shadow: 8px 8px 0 var(--yl); }
.countdown.over { background: var(--yl); color: var(--on-accent); }
.time { font-family: var(--f-display); font-size: 6.5rem; line-height: 1; letter-spacing: -0.02em; }
.small { padding: 8px 20px 8px; box-shadow: 6px 6px 0 var(--tk); }
.small .time { font-size: 3.6rem; }
.hint { font-family: var(--f-mono); font-weight: 800; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.7; margin-top: 4px; }
</style>
