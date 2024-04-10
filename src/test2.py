from pybaseball import statcast_batter, spraychart
from pybaseball import  playerid_lookup
id = playerid_lookup('carroll', 'corbin')
print(id)

data = statcast_batter('2023-01-01', '2024-01-01', 682998)
print(data.to_string())
sub_data = data[data['home_team'] == 'AZ']
hit_data = sub_data[(sub_data['events'] == 'single') | (sub_data['events'] == 'double') | (sub_data['events'] == 'triple') | (sub_data['events'] == 'home_run')]
spraychart(hit_data, 'red_sox', title='Corbin Carroll: 2023 Season')