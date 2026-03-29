from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# Request Body Model
class User(BaseModel):
    name: str
    age: int

# Root API
@app.get("/")
def read_root():
    return {"message": "Welcome to Day 3 FastAPI"}

# POST API
@app.post("/user", status_code=201)
def create_user(user: User):
    # We can access data using user.name and user.age
    return {"message": f"User {user.name} created successfully", "age": user.age}