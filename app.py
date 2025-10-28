import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='build')
CORS(app)

@app.route('/checkin_hardware', methods=['POST'])
def checkIn_hardware():
	data = request.get_json()
	projectId = data.get('projectId')
	qty = data.get('qty')
	return jsonify({
		'message': f"{qty} hardware checked in",
		'projectId': projectId,
		'qty': qty
	})

@app.route('/checkout_hardware', methods=['POST'])
def checkOut_hardware():
	data = request.get_json()
	projectId = data.get('projectId')
	qty = data.get('qty')
	return jsonify({
		'message': f"{qty} hardware checked out",
		'projectId': projectId,
		'qty': qty
	})

@app.route('/join_project', methods=['POST'])
def joinProject():
	data = request.get_json()
	projectId = data.get('projectId')
	return jsonify({
		'message': f"Joined {projectId}",
		'projectId': projectId
	})

@app.route('/leave_project', methods=['POST'])
def leaveProject():
	data = request.get_json()
	projectId = data.get('projectId')
	return jsonify({
		'message': f"Left {projectId}",
		'projectId': projectId
	})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
	if path != '' and os.path.exists(app.static_folder + '/' + path):
		return send_from_directory(app.static_folder, path)
	else:
		return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
	app.run(debug=True)
