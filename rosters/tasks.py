# -*- coding: utf-8 -*-
import requests
import bs4
import pytz
import datetime

from .models import Player, Team

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'}

URL = "http://www.dota2.com/majorsregistration/list"


def get_rosters():
    response = requests.get(URL, headers=HEADERS)

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    for divs in soup.find_all('div', {'class': 'ConfirmationRow'}):
        div = divs.find_all('div', {'class': 'OptimizeTextRadiance'})
        year, month, day = div[0].string.split('-')
        hour, minute, sec = div[1].string.split(':')
        sec, tz = sec.split(' ')
        if tz == 'PDT':
            timezone = pytz.timezone('US/Pacific')
        dt = datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour), minute=int(minute),
                           second=int(sec), tzinfo=timezone)
        name = div[3].contents[0].string
        full_name = div[3].contents[1].strip(' (').strip(')')
        team_name, team_id = div[4].string.split(' (')
        team_id = team_id.split(')')[0].split('ID: ')[1]
        status = div[5].string

        team, created = Team.objects.get_or_create(id=team_id, name=team_name)
        player, created = Player.objects.get_or_create(name=name, full_name=full_name, status=status, updated=dt)
        player.save()
        player.team.add(team)

        print('Updated: {} at {}'.format(name, dt))


def scrape():
    get_rosters()