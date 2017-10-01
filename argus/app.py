from flask import Flask, request, jsonify
from flask import render_template, send_from_directory, make_response
from invariant_status import get_status



app = Flask(__name__)
app.url_map.strict_slashes = False

# A function to serve basic webpages
@app.route('/')
@app.route('/status/<plc>')
def basic_pages(**kwargs):
	return make_response(open('templates/index.html').read())

# API end to query the particular plc
@app.route('/api/status/<int:plc>', methods=["GET"])
def get_topic(plc):
	result = {}

	invariants = get_status(plc)


	if invariants:
		result['status']= 'success'
		result['invariants'] = invariants
		result['count'] = len(invariants)
		result['plc_name'] = 'PLC %d' %(plc)
		if plc == 7:
			result['plc_name'] = 'All PLCs'
	else:
		result['status']= 'error'
		result['plc_name'] = "Couldnt Fetch"


	return jsonify(**result), 200

@app.route('/api', methods=["GET"])
def get_plcs():
	return jsonify(**{
		'status': 'success',
		'count': 6,
		'plcs': [
			{'link': '/status/1', 'name': 'Raw Water', 'desc': 'Controls the raw water phase'},
			{'link': '/status/2', 'name': 'Pre-Treatment', 'desc': 'Does the chemical treatment'},
			{'link': '/status/3', 'name': 'Ultra Filtration', 'desc': 'Performs high level filtering'},
			{'link': '/status/4', 'name': 'De-Chlorination', 'desc': 'Removes chlorides from water'},
			{'link': '/status/5', 'name': 'Reverse Osmosis', 'desc': 'Performs RO on water'},
			{'link': '/status/6', 'name': 'RO Product', 'desc': 'Cleans UF membrane'},
			{'link': '/status/7', 'name': 'All PLCs', 'desc': 'All in One Screen'},
		]
	})


@app.route('/favicon.ico')
def favicon():
	return send_from_directory('static/img', 'favicon.ico')

@app.errorhandler(404)
def not_found(e):
	return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')