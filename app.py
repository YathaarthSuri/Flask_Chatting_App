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



