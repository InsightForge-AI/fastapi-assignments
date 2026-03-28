# Day 5: Todo API Project

This project provides a simple interface to manage tasks using FastAPI.

## Functionality
- Retrieve the full list of todo items.
- Add new tasks via JSON payloads.
- Fetch specific tasks using path parameters.

## Endpoints

### List Todos
GET /todos

### Create Todo
POST /todos
Payload: {"id": 1, "task": "Finish assignment", "completed": false}

### Get Single Todo
GET /todos/{id}
Returns 404 if the ID does not exist.