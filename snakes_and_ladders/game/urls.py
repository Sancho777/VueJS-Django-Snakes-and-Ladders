from django.urls import path
from .views import StartGame, GameState, RollDice, RestartGame

urlpatterns = [
    path('start/', StartGame.as_view()),
    path('state/', GameState.as_view()),
    path('roll/', RollDice.as_view()),
    path('restart/', RestartGame.as_view()),
]
