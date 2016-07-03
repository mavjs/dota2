# -*- coding: utf-8 -*-
import requests
import bs4
import pytz
import datetime

from .models import Player, Team

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36'
}


def get_rosters():
    pro_roster_url = "http://www.dota2.com/majorsregistration/list"
    response = requests.get(pro_roster_url, headers=HEADERS)
    response.encoding = 'utf-8'
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
        team.save()
        player, created = Player.objects.get_or_create(name=name, full_name=full_name, team=team, status=status,
                                                       updated=dt)
        player.save()

        print('Updated: {} ({}) at {}'.format(name, full_name, dt))


def get_leaderboard():
    leaderboard_url = 'http://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001'
    divisions = ['americas', 'europe', 'se_asia', 'china']

    for division in divisions:
        response = requests.get(leaderboard_url, params={'division': division}, headers=HEADERS)
        division_leaderboard = response.json()
        leaderboard = division_leaderboard["leaderboard"]

        print("Querying rankings in division: {}".format(division))

        for rank in leaderboard:
            if "team_id" in rank:
                if "country" in rank:
                    team, created = Team.objects.update_or_create(id=rank["team_id"],
                                                                  defaults={"tag": rank["team_tag"]})
                    team.save()
                    player, created = Player.objects.update_or_create(name=rank["name"], team=team,
                                                                      defaults={"country": rank["country"],
                                                                                "rank": rank["rank"],
                                                                                "mmr": rank["solo_mmr"]})
                    player.save()

                    print(
                        "Updated: {} ({}) (mmr: {}, rank: {})".format(rank["name"], rank["team_tag"], rank["solo_mmr"],
                                                                      rank["rank"]))
                else:
                    team, created = Team.objects.update_or_create(id=rank["team_id"],
                                                                  defaults={"tag": rank["team_tag"]})
                    team.save()
                    player, created = Player.objects.update_or_create(name=rank["name"], team=team,
                                                                      defaults={"rank": rank["rank"],
                                                                                "mmr": rank["solo_mmr"]})
                    player.save()

                    print(
                        "Updated: {} ({}) (mmr: {}, rank: {})".format(rank["name"], rank["team_tag"], rank["solo_mmr"],
                                                                      rank["rank"]))
            else:
                if "country" in rank:
                    player, created = Player.objects.get_or_create(name=rank["name"], country=rank["country"],
                                                                   rank=rank["rank"], mmr=rank["solo_mmr"])
                    player.save()

                    print("Updated: {} (mmr: {}, rank: {})".format(rank["name"], rank["solo_mmr"], rank["rank"]))
                else:
                    player, created = Player.objects.get_or_create(name=rank["name"],
                                                                   rank=rank["rank"], mmr=rank["solo_mmr"])
                    player.save()

                    print("Updated: {} (mmr: {}, rank: {})".format(rank["name"], rank["solo_mmr"], rank["rank"]))
