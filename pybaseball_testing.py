# To test the pybaseball library
from pybaseball import *
pybaseball.cache.enable()

# For the standings function, to improve readability
NL_WEST, NL_CENTRAL, NL_EAST, AL_WEST, AL_CENTRAL, AL_EAST = -1, -2, -3, 2, 1, 0

# TEST TEST TEST

def main():
    print('Testing Pybaseball')
    print('-'*50)
    #print('Player ID Lookup: ' + str(playerid_lookup('carroll', 'corbin')[0]))
    data = batting_stats_range("2024-01-01", "2024-04-10").reset_index()
    player_names = []
    for idx in range(len(data)):
        if data.loc[idx].loc['Tm'] == 'Chicago':
            if data.loc[idx].loc['Lev'] == 'Maj-NL':
                player_names.append({'Name': data.loc[idx].loc["Name"], 'Team': 'Cubs', 'Batting Average': data.loc[idx].loc['BA']})
            else:
                player_names.append({'Name': data.loc[idx].loc["Name"], 'Team': 'White Sox', 'Batting Average': data.loc[idx].loc['BA']})
        else:
            player_names.append({'Name': data.loc[idx].loc["Name"], 'Team': data.loc[idx].loc['Tm'], 'Batting Average': data.loc[idx].loc['BA']})


    for player_name in player_names:
        print(player_name)


if __name__ == '__main__':
    main()