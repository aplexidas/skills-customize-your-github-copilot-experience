# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a REST API using the FastAPI framework to learn how to create web services that handle HTTP requests and responses with proper endpoints and data validation.

## 📝 Tasks

### 🛠️ Create a Book Management API

#### Description
Build a REST API that manages a collection of books. The API should support basic CRUD (Create, Read, Update, Delete) operations for book records.

#### Requirements
Completed program should:

- Create a GET endpoint `/books` that returns a list of all books
- Create a GET endpoint `/books/{book_id}` that returns a specific book by ID
- Create a POST endpoint `/books` that adds a new book to the collection
- Create a PUT endpoint `/books/{book_id}` that updates an existing book
- Create a DELETE endpoint `/books/{book_id}` that removes a book from the collection
- Use Pydantic models for data validation
- Include at least these book fields: id, title, author, year, and genre
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Search and Filter Functionality

#### Description
Extend your API with query parameters to search and filter books by different criteria.

#### Requirements
Completed program should:

- Add query parameters to `/books` endpoint to filter by author
- Add query parameters to `/books` endpoint to filter by genre
- Add query parameters to `/books` endpoint to filter by year range
- Support combining multiple filters in a single request
- Return an empty list when no books match the filters
- Include example data (at least 5 books) to demonstrate filtering
