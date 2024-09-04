from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the dynamic content app! Go to /greet/<name>/page/<int:page_number> to see dynamic content.'

@app.route('/greet/<name>/page/<int:page_number>')
def greet(name, page_number):
    return render_template('dynamic.html', name=name, page_number=page_number)

if __name__ == '__main__':
    app.run(debug=True)
