from django.core.management.base import BaseCommand, CommandError
from rosters.tasks import get_rosters


class Command(BaseCommand):
    help = 'Scrape Dota2 Pro Registration list'

    def handle(self, *args, **options):
        get_rosters()