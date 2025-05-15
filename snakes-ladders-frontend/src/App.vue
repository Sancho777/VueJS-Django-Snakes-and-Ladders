<template>
  <div class="app max-w-6xl mx-auto p-6">
    <h1 class="text-3xl font-bold mb-6 text-center">Snakes and Ladders</h1>

    <!-- Show player selection if game not started -->
    <ChoosePlayers v-if="!gameStarted" @start="startGame" />

    <!-- Main game UI -->
    <div v-else class="space-y-6">
      <!-- Top Row: LastMove | Board | Players -->
      <div class="flex flex-col lg:flex-row lg:space-x-6">
        <!-- Left Column: Last Move -->
        <div class="lg:w-1/5 w-full mb-4 lg:mb-0">
          <LastMove :lastMove="lastMove" />
        </div>

        <!-- Center: Board -->
        <div class="lg:w-3/5 w-full order-first lg:order-none">
          <Board :players="players" :snakes="snakes" :ladders="ladders" />
        </div>

        <!-- Right Column: Players & Winner -->
        <div class="lg:w-1/5 w-full mt-4 lg:mt-0 flex flex-col space-y-4">
          <PlayerList :players="players" :currentPlayerId="currentPlayerId" />
          <WinnerAnnouncement :winner="winner" />
        </div>
      </div>

      <!-- Bottom Row: Controls -->
      <div class="w-full flex justify-center">
        <Controls
          :gameOver="!!winner"
          :isRolling="isRolling"
          @roll="rollDice"
          @restart="restartGame"
        />
      </div>
    </div>

    <!-- Loading indicator -->
    <div
      v-if="loading"
      class="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center text-white text-xl z-50"
    >
      Loading...
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// ✅ Set baseURL depending on environment
axios.defaults.baseURL =
  import.meta.env.MODE === "production"
    ? "https://vuejs-django-snakes-and-ladders.onrender.com"
    : "http://localhost:8000";
axios.defaults.withCredentials = true;

console.log("Enviroment: ", import.meta.env.MODE);

import ChoosePlayers from "./components/ChoosePlayers.vue";
import Board from "./components/Board.vue";
import PlayerList from "./components/PlayerList.vue";
import LastMove from "./components/LastMove.vue";
import Controls from "./components/Controls.vue";
import WinnerAnnouncement from "./components/WinnerAnnouncement.vue";

// Reactive state
const gameStarted = ref(false);
const loading = ref(false);
const isRolling = ref(false);

const players = ref([]);
const currentPlayerId = ref(null);
const lastMove = ref(null);
const winner = ref(null);

// Snakes and ladders positions (hardcoded or fetched from backend)
const snakes = {
  16: 6,
  47: 26,
  49: 11,
  56: 53,
  62: 19,
  64: 60,
  87: 24,
  93: 73,
  95: 75,
  98: 78,
};

const ladders = {
  1: 38,
  4: 14,
  9: 31,
  21: 42,
  28: 84,
  36: 44,
  51: 67,
  71: 91,
  80: 100,
};

// Utility: Map player colors for UI
const playerColors = ["#EF4444", "#3B82F6", "#10B981", "#F59E0B"];

// Helper: Map backend game state to frontend players array
function mapGameStateToPlayers(gameState) {
  return gameState.players.map((p, i) => ({
    id: p.id,
    name: p.name,
    icon: p.icon,
    position: p.position,
    color: playerColors[i % playerColors.length],
  }));
}

function updateGameState(gameState) {
  players.value = mapGameStateToPlayers(gameState);

  // current_turn is an index, get player id safely
  if (
    typeof gameState.current_turn === "number" &&
    players.value[gameState.current_turn]
  ) {
    currentPlayerId.value = players.value[gameState.current_turn].id;
  } else {
    currentPlayerId.value = null;
  }

  winner.value = gameState.winner || null;
  lastMove.value = gameState.last_move || null;
}

async function startGame(numPlayers) {
  loading.value = true;
  try {
    const res = await axios.post("/start/", { num_players: numPlayers });
    if (res.data.success) {
      updateGameState(res.data.state);
      gameStarted.value = true;
      lastMove.value = null;
      winner.value = null;
    } else {
      alert("Failed to start game");
    }
  } catch (error) {
    alert("Error starting game: " + error.message);
  } finally {
    loading.value = false;
  }
}

async function fetchGameState() {
  loading.value = true;
  try {
    const res = await axios.get("/state/");
    updateGameState(res.data);
    gameStarted.value = true;
  } catch (error) {
    // No game in session
    gameStarted.value = false;
  } finally {
    loading.value = false;
  }
}

async function rollDice() {
  if (winner.value) return;
  isRolling.value = true;
  try {
    const res = await axios.post("/roll/");
    if (res.data.success) {
      updateGameState(res.data.state);
    } else {
      alert("Failed to roll dice");
    }
  } catch (error) {
    alert("Error rolling dice: " + error.message);
  } finally {
    isRolling.value = false;
  }
}

async function restartGame() {
  loading.value = true;
  try {
    const res = await axios.post("/restart/");
    if (res.data.success) {
      updateGameState(res.data.state);
      lastMove.value = null;
      winner.value = null;
      gameStarted.value = false; // Show player selection again
    } else {
      alert("Failed to restart game");
    }
  } catch (error) {
    alert("Error restarting game: " + error.message);
  } finally {
    loading.value = false;
  }
}

// On app mount, try to load existing game state
onMounted(() => {
  fetchGameState();
});
</script>

<style>
/* Add any global styles or overrides here */
</style>
