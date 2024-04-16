from pybaseball import playerid_lookup

class Player:
    def __init__(self, name, pos):
        self.name = name
        self.fname = name.split(' ')[0]
        self.lname = name.split(' ')[1]
        self.pos = pos
        ids = playerid_lookup(self.lname, self.fname, True).loc[0]
        self.bbref_id = ids.loc['key_bbref']
        self.mlb_id = ids.loc['key_mlbam']
        self.fangraphs_id = ids.loc['key_fangraphs']
        self.retrosheet_id = ids.loc['key_retro']