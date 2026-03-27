from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request Model
class User(BaseModel):
    name: str
    age: int


# 1️ GET API (Home)
@app.get("/")
def home():
    return {"message": "Day 4 API Running "}


# 2️ GET API with Query Params
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


# 3️ GET API for Addition
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}




# 4️ POST API
@app.post("/user")
def create_user(user: User):
    return {
        "status": "success",
        "data": {
            "name": user.name,
            "age": user.age
        }
    }

    #pr practice change
    