from django.core.management.base import BaseCommand, CommandError
from rosters.tasks import get_leaderboard


class Command(BaseCommand):
    help = 'Scrape Dota2 Solo MMR list'

    def handle(self, *args, **options):
        get_leaderboard()