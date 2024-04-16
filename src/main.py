from const import *
from game import Game
from pybaseball import *
from pybaseball.retrosheet import *
pybaseball.cache.enable()

def main():
    print('Hello Game Prediction V3.0')
    temp_teams = []
    # Load Rosters by year
    for year in ROSTER:
        dates = (f'{year}-01-01', f'{year}-12-31')
        data = batting_stats_range(dates[0], dates[1]).reset_index()
        for idx in range(len(data)):
            row = data.loc[idx]
            teams = row.loc['Tm'].split(',')
            leagues = row.loc['Lev'].split(',')
            for team, league in zip(teams, leagues):
                # Pybaseball only returns the city name, this accounts for teams in the same city
                if team in ('Chicago', 'New York', 'Los Angeles'):
                    if league == 'Maj-NL':
                        if team == 'Chicago':
                            team = 'Cubs'
                        elif team == 'New York':
                            team = 'Mets'
                        elif team == 'Los Angeles':
                            team = 'Dodgers'
                    elif league == 'Maj-AL':
                        if team == 'Chicago':
                            team = 'White Sox'
                        elif team == 'New York':
                            team = 'Yankees'
                        elif team == 'Los Angeles':
                            team = 'Angels'
                if team not in ROSTER[year]:
                    ROSTER[year][team] = dict()
                    temp_teams.append(team)
                ROSTER[year][team][row.loc['Name']] = row.loc['mlbID'] # Add player to team   

    print(ROSTER.keys())
    print(ROSTER[2023].keys())
    print(len(ROSTER[2023]))
    print(ROSTER[2023]['Arizona'].keys())

    # Print Roster
    for year in ROSTER:
        for team in ROSTER[year]:
            print(ROSTER[year][team])

    print('-'*50)

    # Load Schedule
    for year in ROSTER:
        for team in ROSTER[year]:
            schedule = schedule_and_record(year, TEAM_ABBR[team]).reset_index()
            for idx in range(len(schedule)):
                data = schedule.loc[idx]
                if data.loc['Home_Away'] == 'Home':
                    game = Game(data, year)
                    if game.home not in GAMES[year]:
                        GAMES[year][game.home] = dict()
                    GAMES[year][game.home][game.id] = game

    print(len(GAMES))
    print(len(GAMES[2023]))
    print(len(GAMES[2023]['ARI']))
    print(GAMES[2023].keys())

    # Load Games
    for year in GAMES:
        log = season_game_logs(year)
        for idx in range(len(log)):
            game = log.loc[idx]
            home_team = gl_conv_abbr(game.loc['home_team'])
            visitor_team = gl_conv_abbr(game.loc['visiting_team'])
            game_id = str(game.loc['date']) + home_team + visitor_team
            GAMES[year][home_team][game_id].setGameLog(game)
        # Load Stats for each team leading up to game
        # Compare stats and determine outcome

    # Repeat for each game
    # Output to CSV

# TO account for differences in abbreviations between data sources
def gl_conv_abbr(team):
    if team == 'CHN':
        team = 'CHC'
    elif team == 'LAN':
        team = 'LAD'
    elif team == 'NYN':
        team = 'NYM'
    elif team == 'NYA':
        team = 'NYY'
    elif team == 'SLN':
        team = 'STL'
    elif team == 'WAS':
        team = 'WSN'
    elif team == 'CHA':
        team = 'CHW'
    elif team == 'KCA':
        team = 'KCR'
    elif team == 'SFN':
        team = 'SFG'
    elif team == 'ANA':
        team = 'LAA'
    elif team == 'TBA':
        team = 'TBR'
    elif team == 'SDN':
        team = 'SDP'
    return team

if __name__ == '__main__':
    main()