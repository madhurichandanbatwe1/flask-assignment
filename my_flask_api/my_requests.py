import requests

response = requests.post('http://127.0.0.1:5000/books', json={
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'year_published': 1925
})

print(response.json())
