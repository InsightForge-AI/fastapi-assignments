from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Day 1
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello World"}

# Day 2
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Day 3
class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {
        "message": "User received successfully",
        "name": user.name,
        "age": user.age
    }