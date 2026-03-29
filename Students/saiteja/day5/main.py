from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
users = []

class User(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Day 5 API Running"}

# CREATE
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User added successfully", "data": user}

# READ
@app.get("/users")
def get_users():
    return users

# UPDATE
@app.put("/user")
def update_user(user: User):
    for u in users:
        if u.name == user.name:
            u.age = user.age
            return {"message": "User updated"}
    return {"message": "User not found"}

# DELETE
@app.delete("/user")
def delete_user(name: str):
    for u in users:
        if u.name == name:
            users.remove(u)
            return {"message": "User deleted"}
    return {"message": "User not found"}