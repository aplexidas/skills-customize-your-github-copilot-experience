"""
FastAPI REST API - Starter Code
Build a Book Management API with CRUD operations
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# TODO: Define your Book model using Pydantic BaseModel
# Include fields: id, title, author, year, genre

class Book(BaseModel):
    pass  # Replace with your implementation


# Sample data - feel free to add more books
books_db = []


# TODO: Implement GET /books endpoint
# Return all books, with optional filtering by author, genre, or year
@app.get("/books")
def get_books():
    pass


# TODO: Implement GET /books/{book_id} endpoint
# Return a specific book by ID or 404 if not found
@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


# TODO: Implement POST /books endpoint
# Add a new book to the collection and return it
@app.post("/books", status_code=201)
def create_book(book: Book):
    pass


# TODO: Implement PUT /books/{book_id} endpoint
# Update an existing book or return 404 if not found
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    pass


# TODO: Implement DELETE /books/{book_id} endpoint
# Remove a book from the collection or return 404 if not found
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    pass


# Run the server with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
