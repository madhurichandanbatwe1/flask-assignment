from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a real secret key in production

@app.route('/', methods=['GET'])
def login():
    if 'username' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    session['username'] = request.form['username']
    return redirect(url_for('profile'))

@app.route('/profile', methods=['GET'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
