from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Game
from .serializers import GameSerializer
from django.http import JsonResponse

class GameSearch(APIView):
    def get(self, request):
        game_name = request.query_params.get('name')
        print(f"The game name {{game_name}}")
        if game_name:
            games = Game.objects.filter(name__icontains=game_name)
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "Please provide a game name for search."}, status=400)
        
def game_list(request):
    games = Game.objects.all()
    data = [{'id': game.id,
             'name': game.name,
             'total_copies_sold': game.total_copies_sold,
             'series': game.series,
             'release_date': game.release_date,
             'genre': game.genre,
             'developer': game.developer,
             'publisher': game.publisher
            } for game in games]
    return JsonResponse(data, safe=False)
