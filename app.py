import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='./build', static_url_path='/')
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

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
