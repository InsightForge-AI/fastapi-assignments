from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    age: int

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old!"
    }