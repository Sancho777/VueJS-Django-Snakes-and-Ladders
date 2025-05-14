# Snakes and Ladders 🎲🐍

A classic **Snakes and Ladders** game built with a Django REST API backend and a Vue 3 frontend. Play with multiple players, roll dice, climb ladders, avoid snakes, and race to the 100th cell to win!

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Backend Setup (Django)](#backend-setup-django)
  - [Frontend Setup (Vue 3)](#frontend-setup-vue-3)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Project Overview

This project implements the classic board game **Snakes and Ladders** with:

- **Backend:** Django + Django REST Framework managing game logic, sessions, and API endpoints.
- **Frontend:** Vue 3 with Tailwind CSS for a responsive, interactive user interface.
- **Session-based game state:** Game state is stored in Django sessions, allowing persistent play across requests.
- **API-driven:** Frontend communicates with backend via RESTful API calls.

---

## Features

- Select number of players (up to 10)
- Roll dice and move players on a 10x10 board
- Automatic handling of snakes and ladders
- Turn-based gameplay with current player indication
- Display of last move and move history
- Restart game functionality with player selection reset
- Responsive UI for desktop and mobile

---

## Tech Stack

| Layer         | Technology                |
| ------------- | ------------------------- |
| Backend       | Python, Django, DRF       |
| Frontend      | Vue 3, Vite, Tailwind CSS |
| Communication | REST API (JSON)           |
| Styling       | Tailwind CSS              |

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Node.js 16+ and npm/yarn
- Git (optional)

---

### Backend Setup (Django)

1. **Clone the repository**:

```
git clone https://github.com/yourusername/snakes-and-ladders.git
cd snakes-and-ladders/backend
```

2. **Create and activate a Python virtual environment:**

```
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows PowerShell
```

3. **Install backend dependencies:**

```
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, install manually:
>
> ```
> pip install django djangorestframework django-cors-headers
> ```

4. **Apply migrations:**

```
python manage.py migrate
```

5. **Run the Django development server:**

```
python manage.py runserver
```

The backend API will be available at `http://localhost:8000/api/`.

---

### Frontend Setup (Vue 3)

1. **Navigate to the frontend folder:**

```
cd ../frontend
```

2. **Install frontend dependencies:**

```
npm install
```

3. **Configure Vite dev server proxy**

Make sure `vite.config.js` contains:

export default {
server: {
proxy: {
'/api': '<http://localhost:8000>',
},
},
}

4. **Run the frontend development server:**

```
npm run dev
```

The frontend will be available at `http://localhost:5173` (or the port shown in terminal).

---

## Running the Project

1. Start the **backend** server:

```
cd backend
source venv/bin/activate # activate your venv
python manage.py runserver
```

2. Start the **frontend** server:

```
cd frontend
npm run dev
```

3. Open your browser and navigate to:

<http://localhost:5173>

4. Select number of players and start playing!

---

## Usage

- **Start Game:** Choose 2-10 players and click Start.
- **Roll Dice:** Click "Roll Dice" to move the current player.
- **View Moves:** See last move and move history on the left.
- **Players List:** See players and current turn on the right.
- **Restart Game:** Resets game and returns to player selection.

---

## Troubleshooting

- **API calls failing due to CORS:**
  Ensure `django-cors-headers` is installed and configured, and Vite proxy is set correctly.

- **Session not persisting:**
  Confirm Django session middleware is enabled and cookies are accepted by browser.

- **CSRF errors on POST requests:**
  The backend uses `@ensure_csrf_cookie` decorator; ensure frontend sends CSRF tokens or disable CSRF for API views carefully.

- **Port conflicts:**
  Make sure backend (default 8000) and frontend (default 5173) ports are free or configure accordingly.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- Inspired by the classic Snakes and Ladders board game.
- Built with love using Django and Vue.js.

---

Happy playing! 🎲🐍
