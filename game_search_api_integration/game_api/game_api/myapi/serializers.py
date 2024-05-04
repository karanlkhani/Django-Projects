from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'total_copies_sold', 'series', 'release_date', 'genre', 'developer', 'publisher']