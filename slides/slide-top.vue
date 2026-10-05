<script setup>
import { computed } from 'vue'
import { useSlideContext } from '@slidev/client'

const { $page, $nav } = useSlideContext()
const pct = computed(() => Math.round(($page.value / $nav.value.total) * 100))
</script>

<template>
  <div class="deck-progress"><div class="bar" :style="{ width: `${pct}%` }" /></div>
</template>

<style scoped>
.deck-progress { position: absolute; top: 0; left: 0; right: 0; height: 6px; z-index: 20; pointer-events: none; }
.bar { height: 100%; background: var(--tk); border-right: 6px solid var(--yl); }
</style>
