from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create Pydantic model
class User(BaseModel):
    name: str
    age: int

# Step 2: Create POST API
@app.post("/user-info")
def user_info(user: User):
    return {
        "message": f"Hello {user.name}, you are {user.age} years old!"
    }