from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from .models.game_logic import Game

SESSION_KEY = 'snakes_and_ladders_game'

def get_game_from_session(request):
    data = request.session.get(SESSION_KEY)
    if data:
        return Game.deserialize(data)
    return None

def save_game_to_session(request, game):
    request.session[SESSION_KEY] = game.serialize()
    request.session.modified = True

class StartGame(APIView):
    @method_decorator(ensure_csrf_cookie)
    def post(self, request):
        try:
            num_players = int(request.data.get("num_players", 2))
            game = Game(num_players)
            save_game_to_session(request, game)
            return Response({"success": True, "state": game.serialize()})
        except Exception as e:
            import traceback
            traceback.print_exc()
            return Response({"error": str(e)}, status=500)

class GameState(APIView):
    def get(self, request):
        game = get_game_from_session(request)
        if not game:
            return Response({"error": "No game in session. Start a new game."}, status=status.HTTP_404_NOT_FOUND)
        return Response(game.serialize())

class RollDice(APIView):
    def post(self, request):
        game = get_game_from_session(request)
        if not game:
            return Response({"error": "No game in session. Start a new game."}, status=status.HTTP_404_NOT_FOUND)

        # Perform a full turn: roll dice, move player, update state
        game.next_turn()

        save_game_to_session(request, game)
        return Response({
            "success": True,
            "roll_result": game.last_move,  # you can customize this if you want just dice number
            "state": game.serialize()
        })

class RestartGame(APIView):
    def post(self, request):
        game = get_game_from_session(request)
        if not game:
            return Response({"error": "No game in session. Start a new game."}, status=status.HTTP_404_NOT_FOUND)

        num_players = game.num_players  # Make sure this attribute exists in Game.__init__
        new_game = Game(num_players)
        save_game_to_session(request, new_game)
        return Response({"success": True, "state": new_game.serialize()})
