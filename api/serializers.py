from rest_framework import serializers
from rosters.models import Player, Team


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player