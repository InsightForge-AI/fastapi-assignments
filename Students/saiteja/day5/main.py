from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    age: int

# CREATE
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "data": user}

# GET ALL
@app.get("/users")
def get_users():
    return {"users": users}

# GET ONE
@app.get("/user")
def get_user(name: str):
    for user in users:
        if user.name == name:
            return user
    return {"message": "User not found"}

# UPDATE
@app.put("/user")
def update_user(name: str, new_age: int):
    for user in users:
        if user.name == name:
            user.age = new_age
            return {"message": "User updated", "user": user}
    return {"message": "User not found"}

# DELETE
@app.delete("/user")
def delete_user(name: str):
    for user in users:
        if user.name == name:
            users.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}