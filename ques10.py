from flask import Flask, render_template,abort

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the About Page."

# Example route to demonstrate 404 error
@app.route('/cause_404')
def cause_404():
    # This will simulate a 404 error by trying to access a non-existent resource
    abort(404)

# Example route to demonstrate 500 error
@app.route('/cause_500')
def cause_500():
    # This will simulate a 500 error by raising an exception
    raise Exception("This is a 500 Internal Server Error")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
