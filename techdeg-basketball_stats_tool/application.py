import constants
import copy


def clean_data(): 
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
    return players


def get_response(): 
	response = input('\nEnter an option > ')
	try:
		response = int(response)
	except ValueError:
		print('That is not a valid option, please try again.')
	else:
		return response - 1


def balance_teams(teams, players): 
    start_val = 0
    stop_val = int(round(len(players) / len(teams)) / 2)
    incrementer = stop_val
    roster = []
    for n in range(int(len(teams))): 
        list_exp = [player for player in players if player['experience'] == True][start_val:stop_val]
        list_noexp = [player for player in players if player['experience'] == False][start_val:stop_val]
        team_list = list_exp + list_noexp
        for player in team_list:
            player['team'] = teams[n]
        roster = team_list + roster
        start_val = start_val + incrementer
        stop_val = stop_val + incrementer
    return roster


def get_guardians(team):
    output = []
    new_list = []
    parents = [p['guardians'] for p in roster if p['team'] == team]
    for n in range(len(parents)):
        if len(parents[n]) == 2:
            for x in range(2):
                output.append(parents[n][x])
        else:
            output.append("".join(parents[n]))
    return output


if __name__ == "__main__":
    print('\nBASKETBALL TEAM STATS TOOL')
    teams = copy.deepcopy(constants.TEAMS)
    players = clean_data()
    roster = balance_teams(teams, players)
    
    while True:
        print('\n---- MENU ----')
        print('Here are your choices:')
        print('1) Display Team Stats')
        print('2) Quit')
        response = get_response()
        if response == 0:
            for index, item in enumerate(teams, 1):
                print(f'{index}. {item}')
            response = get_response() 
            team = teams[response]
            num_players = len([p for p in roster if p['team'] == team])

            avg_height = round(sum([p['height'] for p in roster if p['team'] == team]) / num_players)
            exp_num = len([p for p in roster if p['experience'] == True and p['team'] == team])
            noexp_num = len([p for p in roster if p['experience'] == False and p['team'] == team])

            names = [p['name'] for p in roster if p['team'] == team]
            player_names = ", ".join(names)

            parents = get_guardians(team)
            gnames = ", ".join(parents)

            print(f'\nTeam: {team} Stats')
            print('====================')
            print(f'Total players: {num_players}')
            print(f'Total experienced: {exp_num}')
            print(f'Total inexperienced: {noexp_num}')
            print(f'Average height: {avg_height} inches\n')  

            print(f'Player names: {player_names}\n') 

            print(f'Guardian names: {gnames}\n')    

            input('\nPress enter to continue... ')
            continue
        elif response == 1:
            print('Have a great day! Quitting.')
            break
        else:
            print('Response not valid, please try again.')
            continue