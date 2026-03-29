from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model for the request body
class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Welcome to Day 3: POST APIs"}

@app.post("/user", status_code=201)
def create_user(user: User):
    # We can access data using user.name and user.age
    return {"message": f"User {user.name} created successfully", "age": user.age}