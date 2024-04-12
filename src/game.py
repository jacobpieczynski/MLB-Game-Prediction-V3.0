from const import *

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
        self.id = self.date + self.home + self.away

    def __repr__(self):
        return f'{self.id}: {self.away} at {self.home} on {self.date}'
    

def conv_date(date, year):
    # TODO: Deal with double headers
    date = date.split(' ')
    day = date[-1]
    if len(day) == 1:
        day = '0' + day
    return str(year) + MONTHS[date[1]] + day
