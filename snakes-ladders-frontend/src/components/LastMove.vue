<template>
  <div class="last-move p-4" v-if="lastMove">
    <p class="text-lg">
      {{ lastMove.player_icon }} rolled a 🎲 {{ lastMove.dice_roll }} and moved
      from {{ lastMove.old_position }} to {{ lastMove.new_position }}
    </p>
    <p class="text-sm text-gray-700">{{ lastMove.message }}</p>
  </div>
</template>

<script setup>
const props = defineProps({
  lastMove: {
    type: Object,
    default: null,
  },
});
</script>
