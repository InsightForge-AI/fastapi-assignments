from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is running"}

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old"
    }