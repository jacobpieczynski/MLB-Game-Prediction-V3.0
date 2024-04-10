# To test the pybaseball library
from pybaseball import *
pybaseball.cache.enable()

# For the standings function, to improve readability
NL_WEST, NL_CENTRAL, NL_EAST, AL_WEST, AL_CENTRAL, AL_EAST = -1, -2, -3, 2, 1, 0

# TEST TEST TEST

def main():
    print('Testing Pybaseball')
    print('-'*50)
    data = batting_stats_range("2023-01-01", "2024-04-10").reset_index()
    player_names = dict()
    for idx in range(len(data)):
        # TODO: Update to account for teams in same city - Mets-Yankees, Cubs-White Sox, Angels-Dodgers
        if data.loc[idx].loc['Tm'] not in player_names:
            player_names[data.loc[idx].loc['Tm']] = [{'Name': data.loc[idx].loc["Name"], 'Batting Average': data.loc[idx].loc['BA'], 'PlayerID': data.loc[idx].loc['mlbID']}]
        else:
            player_names[data.loc[idx].loc['Tm']] = [{'Name': data.loc[idx].loc["Name"], 'Batting Average': data.loc[idx].loc['BA'], 'PlayerID': data.loc[idx].loc['mlbID']}]
        #player_names.append({'Name': data.loc[idx].loc["Name"], 'Team': data.loc[idx].loc['Tm'], 'Batting Average': data.loc[idx].loc['BA']})


    for team in player_names:
        print(team)
        for player in player_names[team]:
            print(player)


if __name__ == '__main__':
    main()