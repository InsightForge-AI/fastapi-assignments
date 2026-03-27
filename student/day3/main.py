from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    age: int

# POST API 1
@app.post("/user")
def create_user(user: User):
    return {
        "message": f"User {user.name} created",
        "age": user.age
    }

# POST API 2
class Numbers(BaseModel):
    a: int
    b: int

@app.post("/add")
def add_numbers(numbers: Numbers):
    return {
        "result": numbers.a + numbers.b
    }