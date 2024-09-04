from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index4.html')

@socketio.on('subscribe')
def handle_subscribe(data=None):
    # Handle subscription requests
    emit('notification', {'message': 'You have been subscribed!'}, broadcast=True)

@socketio.on('send_notification')
def handle_send_notification(data):
    # Broadcast notifications to all connected clients
    emit('notification', {'message': data['message']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
