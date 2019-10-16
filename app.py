from flask import Flask, jsonify, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'		# encryption key
socketio = SocketIO(app)				# wrapping of app in SocketIO that is this app has SocketIO enabled

@app.route('/')
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handleMsg(data):
	socketio.emit('push', data, broadcast=True, include_self=False)



if __name__ == "__main__":
	socketio.run(app)

# SocketIO pushes data from server to user like push notifications














# from flask import Flask, jsonify, request

# # creating our own api which is a list containing users as dictionaries
# users = [
# 	{
# 		"id": 2,
# 		"name": "Anne",
# 		"age": 23
# 	},
# 	{
# 		"id": 3,
# 		"name": "Bill",
# 		"age": 21
# 	},
# 	{
# 		"id": 1,
# 		"name": "Cathy",
# 		"age": 22
# 	}
# ]


# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return app.send_static_file('index.html')

# @app.route('/users')				# decorator changes the function of the function below it
# def getUsers():
# 	return jsonify(users)   # jsonify converts this to a string

# @app.route('/users/<id>')		# <id> means that it is a variable
# def getUser(id):
# 	user = [u for u in users if str(u['id'])==id]
# 	return jsonify(user)

# @app.route('/users/sort')			# /users/sorted?field=age
# def getUsersSorted():
# 	field = request.args.get('field')
# 	usersSorted = sorted(users, key=lambda u: u[field])
# 	return jsonify(usersSorted)


# if __name__ == "__main__":
# 	app.run()

























