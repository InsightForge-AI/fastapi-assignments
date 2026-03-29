from fastapi import FastAPI

app = FastAPI()

todos = []

# Home
@app.get("/")
def home():
    return {"message": "Todo API is running"}

# Add Todo
@app.post("/add")
def add_todo(task: str):
    todos.append(task)
    return {"message": "Added", "todos": todos}

# Get Todos
@app.get("/todos")
def get_todos():
    return todos

# Delete Todo
@app.delete("/delete/{index}")
def delete_todo(index: int):
    todos.pop(index)
    return {"message": "Deleted", "todos": todos}
@app.put("/update/{index}")
def update_todo(index: int, task: str):
    if index < len(todos):
        todos[index] = task
        return {"message": "Updated", "todos": todos}
    return {"error": "Invalid index"}