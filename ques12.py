from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index3.html')

@socketio.on('update_data')
def handle_update(data):
    # Broadcast the data to all connected clients
    emit('data_update', {'data': data['data']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
