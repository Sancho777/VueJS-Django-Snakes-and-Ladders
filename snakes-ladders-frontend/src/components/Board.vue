<template>
  <div
    class="board-container max-w-[600px] w-full aspect-square mx-auto p-4"
    role="grid"
    aria-label="Snakes and Ladders Board"
  >
    <div
      class="board flex flex-col-reverse w-full h-full border border-gray-400 rounded-lg shadow-lg relative"
      style="
        background-image: url('/board5.png');
        background-size: cover;
        background-position: center;
      "
    >
      <div
        v-for="(row, rowIndex) in 10"
        :key="rowIndex"
        class="flex flex-row w-full flex-1"
      >
        <div
          v-for="cell in getRowCells(rowIndex)"
          :key="cell"
          class="cell flex-1 border border-black/10 flex flex-col justify-center items-center text-xs relative bg-white/70"
        >
          <!-- Positioning the number in the top-left corner of each cell -->
          <div class="absolute top-1 left-1 font-[700] text-[10px] select-none">
            {{ cell }}
          </div>

          <!-- Players in the cell -->
          <div class="players flex space-x-1 mt-6">
            <span
              v-for="player in playersInCell(cell)"
              :key="player.id"
              :title="player.name"
              class="w-6 h-6 rounded-full flex items-center justify-center text-sm text-white font-bold select-none"
              :style="{ backgroundColor: player.color }"
            >
              {{ player.icon }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  players: {
    type: Array,
    required: true,
  },
  snakes: {
    type: Object,
    required: true,
  },
  ladders: {
    type: Object,
    required: true,
  },
});

// Get players in a given cell
function playersInCell(cell) {
  return props.players.filter((p) => p.position === cell);
}

// Get cells for a specific row (0-based from bottom)
function getRowCells(rowIndex) {
  const start = rowIndex * 10 + 1;
  const cells = Array.from({ length: 10 }, (_, i) => start + i);
  return rowIndex % 2 === 1 ? cells.reverse() : cells;
}
</script>

<style scoped>
.cell {
  user-select: none;
  position: relative; /* Ensures the absolute positioning of the number works */
}

.player-token {
  font-size: 1.1rem;
  line-height: 1;
}
</style>
