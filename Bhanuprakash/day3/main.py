from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Create a model (structure of JSON input)
class User(BaseModel):
    name: str
    age: int

# POST API
@app.post("/user")
def create_user(user: User):
    return {
        "message": f"Hello {user.name}",
        "age": user.age
    }

   