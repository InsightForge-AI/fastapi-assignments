from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request body model
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Day 3 API Running"}

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old"
    }