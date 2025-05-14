<template>
  <div class="player-list p-4">
    <h3 class="font-semibold mb-2">Players</h3>
    <ul>
      <li
        v-for="player in players"
        :key="player.id"
        :class="[
          'mb-1 p-2 rounded flex items-center',
          player.id === currentPlayerId
            ? 'bg-blue-200 font-bold'
            : 'bg-gray-100',
        ]"
      >
        <span
          class="w-5 h-5 rounded-full mr-2"
          :style="{ backgroundColor: player.color }"
          :title="player.name"
        ></span>
        {{ player.name }} - Position: {{ player.position }}
      </li>
    </ul>
  </div>
</template>

<script setup>
const props = defineProps({
  players: {
    type: Array,
    required: true,
  },
  currentPlayerId: {
    type: Number,
    required: true,
  },
});
</script>
