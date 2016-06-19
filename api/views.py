from rest_framework import serializers, viewsets
from rosters.models import Player, Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for players
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer