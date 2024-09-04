from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for the database
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Item {self.name}>'

# Create the database and tables
with app.app_context():
    db.create_all()

# Home page - List items
@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

# Create a new item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        item_name = request.form['name']
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Update an existing item
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

# Delete an item
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
