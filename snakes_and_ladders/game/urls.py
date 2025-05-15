from django.urls import path
from .views import StartGame, GameState, RollDice, RestartGame
from django.http import JsonResponse
from django.views import View

class TestView(View):
    def get(self, request):
        return JsonResponse({"message": "Test view works!"})

def root_view(request):
    return JsonResponse({"message": "Root URL works"})

urlpatterns = [
    path('start/', StartGame.as_view()),
    path('state/', GameState.as_view()),
    path('roll/', RollDice.as_view()),
    path('restart/', RestartGame.as_view()),
    path('test/', TestView.as_view()),
    path('', root_view),
]
