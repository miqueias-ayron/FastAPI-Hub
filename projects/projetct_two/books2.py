from fastapi import FastAPI

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

BOOKS = [
    Book(1, 'Computer Science Pro', 'Code', 'A very nice book', 5),
    Book(2, 'Be FastAPI', 'Code', 'A great book', 5),
    Book(1, 'Master Endpoints', 'Code', 'A awesome book', 5),
    Book(1, 'HP1', 'Author 01', 'Book description 1', 5),
    Book(1, 'HP2', 'Author 02', 'Book description 2', 5),
    Book(1, 'HP3', 'Author 03', 'Book description 3', 5),
]

@app.get('/books')
async def read_all_the_books():
    return BOOKS