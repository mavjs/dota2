from rest_framework import viewsets
from .serializers import TeamSerializer, PlayerSerializer
from rosters.models import Team, Player


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