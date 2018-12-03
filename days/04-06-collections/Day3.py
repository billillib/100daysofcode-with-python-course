from collections import defaultdict, namedtuple, Counter
import csv
from sys import argv

file = str(argv[1])
num = int(argv[2])
offensive_players = defaultdict(list)


def get_season_by_player():
    '''
    Creates a dictionary of players with key = players name
    Value is a list of named_tuples for each season
    '''

    player_season = namedtuple('player_season', 'year team hits hrs')

    with open(file) as f:
        for row in csv.DictReader(f):
            name = row['playerID']
            year = row['yearID']
            team = row['teamID']
            hits = row['H']
            hr = row['HR']

            # create
            b = player_season(year=year, team=team, hits=hits, hrs=hr)
            # append the tuple into the values of the dict (list)

            offensive_players[name].append(b)


def get_most_seasons(n):
    '''
    Return n most seasons in MLB history by player
    '''
    season_counter = Counter()

    for k, v in offensive_players.items():
        season_counter[k] += len(v)

    return season_counter.most_common(n)


def get_most_hits(n):
    '''
    Return n most hits in MLB history by player
    '''
    hit_counter = Counter()

    for k, v in offensive_players.items():
        for i in v:
            hit_counter[k] += int(i.hits)

    return hit_counter.most_common(n)


def get_most_hrs(n):
    '''
    Return n most hrs in MLB history by player
    '''
    hr_counter = Counter()

    for k, v in offensive_players.items():
        for i in v:
            hr_counter[k] += int(i.hrs)

    return hr_counter.most_common(n)


def print_counter(counter):
    '''
    Prints string representation
    '''
    for idx, i in enumerate(counter):
        print('{}. {} {}\n'.format(idx+1, i[0], i[1]))


if __name__ == '__main__':

    get_season_by_player()

    print("Most seasons by a player:\n")
    season = get_most_seasons(num)
    print_counter(season)

    print("Most hits by a player:\n")
    hits = get_most_hits(num)
    print_counter(hits)

    print("Most HRs by a player:\n")
    homers = get_most_hrs(num)
    print_counter(homers)
