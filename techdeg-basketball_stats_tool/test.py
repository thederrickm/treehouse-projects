


players = copy.deepcopy(constants.PLAYERS)

start_val = 0
stop_val = int(round(len(players) / len(teams)) / 2)
incrementer = stop_val
roster = []

# Clean Data
players = copy.deepcopy(constants.PLAYERS)
for player in players:
    player['height'] = int(player['height'][0:2])
    if player['experience'] == 'NO':
        player['experience'] = False
    elif player['experience'] == 'YES':
        player['experience'] = True
    if "and" in player['guardians']:
        player['guardians'] = player['guardians'].split(' and ')
    elif "and" not in player['guardians']:
    	player['guardians'] = [player['guardians']]

# Balance Teams
for n in range(int(len(teams))): 
    list_exp = [player for player in players if player['experience'] == True][start_val:stop_val]
    list_noexp = [player for player in players if player['experience'] == False][start_val:stop_val]
    team_list = list_exp + list_noexp
    for player in team_list:
        player['team'] = teams[n]
    roster = team_list + roster
    start_val = start_val + incrementer
    stop_val = stop_val + incrementer

parents = [p['guardians'] for p in roster if p['team'] == team]

output = []
new_list = []
for n in range(len(parents)):
    if len(parents[n]) == 2:
        for x in range(2):
            output.append(parents[n][x])
    else:
    	print(parents[n])


 print(", ".join(output))