from const import *
from player import Player
from pybaseball import playerid_lookup

class Game:
    def __init__(self, data, year):
        self.date = conv_date(data.loc['Date'], year)
        home_away = data.loc['Home_Away']
        if home_away == 'Home':
            self.home = data.loc['Tm']
            self.away = data.loc['Opp']
        else:
            self.home = data.loc['Opp']
            self.away = data.loc['Tm']
        self.id = self.date + self.home + self.away\

    def setGameLog(self, log):
        self.gl = log
        self.load_starting_lineups()

    def load_starting_lineups(self):
        self.home_starting_lineup, self.visitor_starting_lineup = [None], [None] # To improve readability, I want this list to start counting from 1, so 0 is None
        for i in range(1, 10):
            try:
                home_rs_id = self.gl.loc[f'home_{i}_id']
            except:
                home_rs_id = playerid_lookup(self.gl.loc[f'home_{i}_name'].split(' ')[1], self.gl.loc[f'home_{i}_name'].split(' ')[0], True).loc[0].loc['key_retro']
            try:
                visitor_rs_id = self.gl.loc[f'visiting_{i}_id']
            except:
                visitor_rs_id = playerid_lookup(self.gl.loc[f'visiting_{i}_name'].split(' ')[1], self.gl.loc[f'visiting_{i}_name'].split(' ')[0], True).loc[0].loc['key_retro']
            if home_rs_id not in PLAYERS:
                PLAYERS[home_rs_id] = Player(self.gl.loc[f'home_{i}_name'], self.gl.loc[f'home_{i}_pos'])
            if visitor_rs_id not in PLAYERS:
                PLAYERS[visitor_rs_id] = Player(self.gl.loc[f'visiting_{i}_name'], self.gl.loc[f'visiting_{i}_pos'])
            self.home_starting_lineup.append(PLAYERS[home_rs_id])
            self.visitor_starting_lineup.append(PLAYERS[visitor_rs_id])

    def __repr__(self):
        return f'{self.id}: {self.away} at {self.home} on {self.date}'
    

def conv_date(date, year):
    # TODO: Deal with double headers
    date = date.split(' ')
    day = date[2]
    if len(day) == 1:
        day = '0' + day
    return str(year) + MONTHS[date[1]] + day
