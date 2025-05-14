<template>
  <div class="controls flex space-x-4 p-4">
    <button
      @click="rollDice"
      :disabled="gameOver || isRolling"
      class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 disabled:opacity-50"
    >
      Roll Dice
    </button>
    <button
      @click="restartGame"
      class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
    >
      Restart Game
    </button>
  </div>
</template>

<script setup>
const emit = defineEmits(["roll", "restart"]);

const props = defineProps({
  gameOver: Boolean,
  isRolling: Boolean,
});

function rollDice() {
  emit("roll");
}

function restartGame() {
  emit("restart");
}
</script>
