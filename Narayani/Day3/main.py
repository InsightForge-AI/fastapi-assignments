from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request Body Model
class User(BaseModel):
    name: str
    age: int

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": "User received successfully",
        "name": user.name,
        "age": user.age
    }