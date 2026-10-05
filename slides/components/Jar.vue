<script setup>
// Toples berlabel = variabel. label = nama variabel, value = isi, type = tipe data
defineProps({
  label: { type: String, required: true },
  value: { type: String, required: true },
  type: { type: String, default: '' },
  accent: { type: String, default: 'tk' },
})
</script>

<template>
  <div class="jar" :class="accent">
    <div class="lid" />
    <div class="body">
      <div class="val">{{ value }}</div>
      <div class="label">{{ label }}</div>
    </div>
    <div v-if="type" class="type">{{ type }}</div>
  </div>
</template>

<style scoped>
.jar { display: flex; flex-direction: column; align-items: center; width: 190px; }
.lid { width: 62%; height: 18px; border: 3px solid var(--border); border-radius: 6px 6px 2px 2px; background: var(--tk); }
.jar.yl .lid { background: var(--yl); }
.body {
  width: 100%;
  margin-top: -3px;
  height: 116px;
  border: 3px solid var(--border);
  border-radius: 14px 14px 22px 22px;
  background: var(--surface);
  box-shadow: 5px 5px 0 var(--shadow);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding: 12px 8px 10px;
}
.val { font-family: var(--f-mono); font-weight: 800; font-size: 1.05rem; text-align: center; word-break: break-all; }
.label {
  font-family: var(--f-mono);
  font-weight: 800;
  font-size: 0.78rem;
  padding: 3px 9px;
  background: var(--yl);
  color: var(--on-accent);
  border: 2.5px solid var(--border);
  transform: rotate(-2deg);
}
.type { margin-top: 8px; font-family: var(--f-mono); font-size: 0.7rem; font-weight: 800; color: var(--muted); }
</style>
