from django.urls import path
from .views import StartGame, GameState, RollDice, RestartGame

urlpatterns = [
    path('api/start/', StartGame.as_view()),
    path('api/state/', GameState.as_view()),
    path('api/roll/', RollDice.as_view()),
    path('api/restart/', RestartGame.as_view()),
]
