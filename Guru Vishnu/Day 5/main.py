from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TodoInput(BaseModel):
    task: str

todos = [
    {"id": 1, "task":"Learn FastAPI","Done":False},
    {"id":2, "task":"Build a API","Done":False},
]

@app.get("/")
def home():
    return {"message":"Welcome to TODO API!"}

@app.get("/todos")
def get_todos():
    return {"todos":todos}

@app.post("/todos")
def add_todo(todo: TodoInput):
    new_id = len(todos) + 1
    new_todo = {"id": new_id, "task": todo.task, "Done": False}
    todos.append(new_todo)
    return {"message": "Todo added!", "todo": new_todo}

@app.put("/todos/{todo_id}")

def mark_done(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["Done"] = True
            return {"message": "Todo marked as done!", "todo": todo}
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted!"}
    return {"error": "Todo not found"}