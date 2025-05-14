<template>
  <div class="choose-players p-4">
    <h2 class="text-xl font-bold mb-2">Select Number of Players</h2>
    <select v-model.number="numPlayers" class="border rounded p-1 mb-4">
      <option v-for="n in maxPlayers" :key="n" :value="n">{{ n }}</option>
    </select>
    <button
      @click="startGame"
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
    >
      Start Game
    </button>
  </div>
</template>

<script setup>
import { ref } from "vue";

const emit = defineEmits(["start"]);

const maxPlayers = 4;
const numPlayers = ref(2);

function startGame() {
  emit("start", numPlayers.value);
}
</script>
