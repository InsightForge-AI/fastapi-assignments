from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return {
        "message": f"{user.name} is {user.age} years old"
    }