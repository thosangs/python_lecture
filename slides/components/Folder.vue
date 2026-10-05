<script setup>
// Map berlabel = variabel. label = nama variabel, value = isi, type = tipe data
defineProps({
  label: { type: String, required: true },
  value: { type: String, required: true },
  type: { type: String, default: '' },
  accent: { type: String, default: 'tk' },
})
</script>

<template>
  <div class="folder" :class="accent">
    <div class="tab">{{ label }}</div>
    <div class="body">
      <div class="paper">{{ value }}</div>
    </div>
    <div v-if="type" class="type">{{ type }}</div>
  </div>
</template>

<style scoped>
.folder { display: flex; flex-direction: column; width: 200px; }
.tab {
  align-self: flex-start;
  max-width: 85%;
  font-family: var(--f-mono);
  font-weight: 800;
  font-size: 0.76rem;
  padding: 4px 12px 3px;
  background: var(--tk);
  color: var(--on-accent);
  border: 3px solid var(--border);
  border-bottom: none;
  border-radius: 8px 8px 0 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.folder.yl .tab { background: var(--yl); }
.body {
  height: 104px;
  border: 3px solid var(--border);
  border-radius: 0 10px 10px 10px;
  background: var(--tk);
  box-shadow: 5px 5px 0 var(--shadow);
  padding: 12px 10px 10px;
  display: flex;
}
.folder.yl .body { background: var(--yl); }
.paper {
  flex: 1;
  display: grid;
  place-items: center;
  text-align: center;
  background: var(--surface);
  color: var(--fg);
  border: 2.5px solid var(--border);
  border-radius: 6px;
  font-family: var(--f-mono);
  font-weight: 800;
  font-size: 0.95rem;
  padding: 4px;
  word-break: break-word;
}
.type { margin-top: 8px; font-family: var(--f-mono); font-size: 0.7rem; font-weight: 800; color: var(--muted); text-align: center; }
</style>
