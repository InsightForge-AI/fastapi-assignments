from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET API
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# POST API
class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old"
    }