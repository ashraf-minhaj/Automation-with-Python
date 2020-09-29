""" Getting live cricket score using python

install:
$ pip install pycricbuzz

author: ashraf minhaj
mail: ashraf_minhaj|@yahoo.com
"""

from pycricbuzz import Cricbuzz  # import library

cricket = Cricbuzz()    # instantiate

# get current matches
matches = cricket.matches()

# score
for match in matches:

	print('____')        # just a separator for scores
	print(match['srs'], ' ', match['type'])  # league name, game type (t20, ODI etc)
	print(match['team1']['name'])
	print(match['team2']['name'])
	print(match['status'])

	# get score if the game started
	try:
		data = cricket.livescore(match['id'])   # check for every matches
		print("Batting: ", data['batting']['team'])
		print("Score: ", data['batting']['score'][0]['runs'])

		print("Bowling: ", data['bowling']['team'])
		print("Score: ", data['bowling']['score'][0]['runs'])
	except:
		print("Not started")
