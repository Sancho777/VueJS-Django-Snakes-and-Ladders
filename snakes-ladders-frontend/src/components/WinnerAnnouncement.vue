<template>
  <div
    v-if="winner"
    class="winner-announcement p-4 bg-yellow-200 rounded text-center"
  >
    <h2 class="text-2xl font-bold mb-2">🎉 Winner: {{ winner.name }} 🎉</h2>
    <p>Congratulations! The game has ended.</p>
  </div>
</template>

<script setup>
const props = defineProps({
  winner: {
    type: Object,
    default: null,
  },
});
</script>
