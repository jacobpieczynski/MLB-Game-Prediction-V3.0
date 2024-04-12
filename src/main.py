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
            for team in teams:
                if team not in ROSTER[year]:
                    ROSTER[year][team] = dict()
                ROSTER[year][team][row.loc['Name']] = row.loc['mlbID'] # Add player to team   

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