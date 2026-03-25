# FastAPI Basic App

A simple FastAPI application with two endpoints.

## Endpoints

- `GET /` - Returns a welcome message
- `GET /hello` - Returns "Hello, World!" message

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the App

Start the server using uvicorn:
```bash
uvicorn main:app --reload
```

The app will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- OpenAPI JSON: `http://localhost:8000/openapi.json`
