from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

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

class BookRequest(BaseModel):
    id: Optional[int] = Field(description='O ID não precisa ser passado', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title": "A new book",
                "author": "New Author",
                "description": "A new description of a book",
                "rating": 5
            }
        }
    }


    

BOOKS = [
    Book(1, 'Computer Science Pro', 'Code', 'A very nice book', 5),
    Book(2, 'Be FastAPI', 'Code', 'A great book', 5),
    Book(3, 'Master Endpoints', 'Code', 'A awesome book', 5),
    Book(4, 'HP1', 'Author 01', 'Book description 1', 5),
    Book(5, 'HP2', 'Author 02', 'Book description 2', 5),
    Book(6, 'HP3', 'Author 03', 'Book description 3', 5),
]

@app.get('/books')
async def read_all_the_books():
    return BOOKS

@app.post('/create-book')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

# funcao utilitaria para preenchimento automático de id
def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book