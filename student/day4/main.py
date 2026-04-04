from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Model
class User(BaseModel):
    name: str
    age: int

# PUT API (Update user)
@app.put("/user")
def update_user(user: User):
    return {
        "message": f"User {user.name} updated",
        "age": user.age
    }