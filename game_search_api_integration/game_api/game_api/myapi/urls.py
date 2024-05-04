from django.urls import path
from .views import GameSearch, game_list

urlpatterns = [
     path('game/', GameSearch.as_view(), name='game-search'),
     path('games/', game_list, name='game_list'),
    # Add other URL patterns as needed
]