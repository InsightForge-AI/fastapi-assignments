from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(title="Todo API", version="1.0.0")



class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class Todo(TodoBase):
    id: str
    created_at: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }




todos_db = []



@app.get("/")
async def root():
    return {
        "message": "Welcome to Todo API!",
        "version": "1.0.0",
        "endpoints": {
            "GET": ["/", "/todos", "/todos/{todo_id}"],
            "POST": ["/todos"],
            "PUT": ["/todos/{todo_id}"],
            "DELETE": ["/todos/{todo_id}"]
        }
    }




# Get all todos
@app.get("/todos", response_model=List[Todo])
async def get_all_todos():
    return todos_db


# Get todo by ID
@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo_by_id(todo_id: str):
    for todo in todos_db:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# Create todo
@app.post("/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate):
    new_todo = {
        "id": str(uuid.uuid4()),
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "created_at": datetime.now()
    }
    todos_db.append(new_todo)
    return new_todo


# Update todo
@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, todo_update: TodoUpdate):
    for i, todo in enumerate(todos_db):
        if todo["id"] == todo_id:

            if todo_update.title is not None:
                todos_db[i]["title"] = todo_update.title

            if todo_update.description is not None:
                todos_db[i]["description"] = todo_update.description

            if todo_update.completed is not None:
                todos_db[i]["completed"] = todo_update.completed

            return todos_db[i]

    raise HTTPException(status_code=404, detail="Todo not found")


# Delete todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    for i, todo in enumerate(todos_db):
        if todo["id"] == todo_id:
            deleted_todo = todos_db.pop(i)
            return {
                "message": "Todo deleted successfully",
                "deleted_todo": deleted_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")




# Delete all todos
@app.delete("/todos")
async def delete_all_todos():
    deleted_count = len(todos_db)
    todos_db.clear()
    return {"message": f"Deleted {deleted_count} todos successfully"}


# Get completed todos
@app.get("/todos/completed/{completed}", response_model=List[Todo])
async def get_todos_by_status(completed: bool):
    return [todo for todo in todos_db if todo["completed"] == completed]


# Search todos
@app.get("/todos/search/{keyword}", response_model=List[Todo])
async def search_todos(keyword: str):
    return [todo for todo in todos_db if keyword.lower() in todo["title"].lower()]