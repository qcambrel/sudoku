## This file defines the player data API and endpoints.

from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# example dictionary
players = [
	{'id': 0,
	 'name': '',
	 'rank': 0,
	 'top_score': 0,
	 'games_played': 0,
	 'average_score': 0,
	 'games_completed': 0},
	{'id': 1,
	 'name': '',
	 'rank': 0,
	 'top_score': 0,
	 'games_played': 0,
	 'average_score': 0,
	 'games_completed': 0}
]


@app.route('/', methods=['GET'])
def home():
	html = "<h1>Sudoku API</h1><p>This is an API for retrieving player and game data.</p>"
	return html

@app.route('/api/v1/resources/players/all', methods=['GET'])
def api_all():
	return jsonify(players)

@app.route('/api/v1/resources/players', methods=['GET'])
def api_id():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return 'Error: No id field specified. You must specify an id.'

	results = []

	for player in players:
		if player['id'] == id:
			results.append(player)

	return jsonify(results)

app.run()