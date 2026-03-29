from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Day 2 APIs
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Day 3 API
class User(BaseModel):
    name: str
    age: int

@app.post("/create_user")
def create_user(user: User):
    return {
        "message": f"User {user.name} created successfully",
        "age": user.age
    }

# Day 4 extra API (status check)
@app.get("/status")
def status():
    return {"message": "API is running successfully"}