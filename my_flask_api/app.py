from flask import Flask, request, jsonify
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# @app.before_first_request
def initialize_database():
    with app.app_context():
        db.create_all()

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year_published = data.get('year_published')
    
    if not title or not author or not year_published:
        return jsonify({'error': 'Missing data'}), 400
    
    new_book = Book(title=title, author=author, year_published=year_published)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'id': new_book.id}), 201

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    result = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year_published': book.year_published
        } for book in books
    ]
    return jsonify(result)

# Get a single book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    if book:
        result = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'year_published': book.year_published
        }
        return jsonify(result)
    return jsonify({'error': 'Book not found'}), 404

# Update a book by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    title = data.get('title')
    author = data.get('author')
    year_published = data.get('year_published')
    
    if title:
        book.title = title
    if author:
        book.author = author
    if year_published:
        book.year_published = year_published
    
    db.session.commit()
    return jsonify({'message': 'Book updated'})

# Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': 'Book not found'}), 404
    
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
