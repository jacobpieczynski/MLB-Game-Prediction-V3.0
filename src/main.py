from const import *
from pybaseball import *
pybaseball.cache.enable()

def main():
    print('Hello Game Prediction V3.0')
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
                ROSTER[year][team][row.loc['Name']] = row.loc['mlbID'] # Add player to team   

    print(ROSTER.keys())
    print(ROSTER[2023].keys())
    print(len(ROSTER[2023]))
    print(ROSTER[2023]['Arizona'].keys())

    # Print Roster
    for year in ROSTER:
        for team in ROSTER[year]:
            print(ROSTER[year][team])

    # Load Games
        # Load Stats for each team leading up to game
        # Compare stats and determine outcome

    # Repeat for each game
    # Output to CSV

if __name__ == '__main__':
    main()