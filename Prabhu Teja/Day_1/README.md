# Day 1 - FastAPI Setup + Basic App

## Task Completion Overview

We completed the Day 1 task by following these steps:

1. **Installation**: Installed FastAPI and Uvicorn using pip:
   ```
   pip install fastapi uvicorn
   ```

2. **Code Creation**: Created app.py with the required endpoints.

3. **Server Execution**: Ran the server using uvicorn:
   ```
   uvicorn app:app --reload
   ```

4. **Testing**: Verified endpoints in the browser at localhost:8000.

## About FastAPI and Uvicorn

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints. It provides automatic API documentation and is built on top of Starlette and Pydantic.

- **Uvicorn**: An ASGI web server implementation for Python. It is used to run FastAPI applications and supports features like auto-reload during development.

## What app.py Does

The app.py file creates a basic FastAPI application with two endpoints:

- **Root endpoint (/)**: Returns a welcome message.
- **Hello endpoint (/hello)**: Accepts an optional name parameter and returns a personalized greeting.

The code initializes a FastAPI app instance and defines these routes using decorators.

## How to Run

1. Ensure FastAPI and Uvicorn are installed.
2. Navigate to the directory containing app.py.
3. Run: `uvicorn app:app --reload`
4. Open http://localhost:8000 in your browser.

## Endpoints

- GET / : Returns {"message": "Welcome"}
- GET /hello?name=YourName : Returns {"message": "Hello, YourName"}