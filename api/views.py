from rest_framework import viewsets
from .serializers import TeamSerializer, PlayerSerializer
from rosters.models import Team, Player
from rest_framework import permissions


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint for players
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )