from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

db = []

@app.get("/")
def root():
    return {"project": "Todo API v1.0"}

@app.get("/todos", response_model=List[Todo])
def list_todos():
    return db

@app.post("/todos", status_code=201)
def create_todo(todo: Todo):
    db.append(todo)
    return todo

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for item in db:
        if item.id == todo_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")