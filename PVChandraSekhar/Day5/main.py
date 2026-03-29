from fastapi import FastAPI, HTTPException
from pydantic import AliasChoices, BaseModel, Field

app = FastAPI(title="Todo API")


class TodoCreate(BaseModel):
    task: str = Field(
        ...,
        validation_alias=AliasChoices("task", "name"),
        description="Task text for the todo item",
    )


class Todo(BaseModel):
    id: int
    task: str
    done: bool


todos: list[Todo] = [
    Todo(id=1, task="Learn FastAPI", done=False),
    Todo(id=2, task="Build an API", done=False),
]


@app.get("/")
def home():
    return {"message": "Welcome to the Todo API"}


@app.get("/todos", response_model=list[Todo])
def get_todos():
    return todos


@app.post("/", response_model=Todo)
@app.post("/todos", response_model=Todo)
def add_todo(todo_data: TodoCreate):
    new_todo = Todo(
        id=len(todos) + 1,
        task=todo_data.task,
        done=False,
    )
    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def mark_todo_done(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todo.done = True
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
