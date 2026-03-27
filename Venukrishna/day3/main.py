from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Structure of the incoming JSON data
class UserData(BaseModel):
    name: str
    age: int

@app.get("/")
def home():
    return {"message": "Day 3: POST API Task"}

@app.post("/user-info")
def create_user(user: UserData):
    # This function accepts a JSON object matching the UserData model
    return {
        "status": "Success",
        "received_data": {
            "name": user.name,
            "age": user.age
        },
        "message": f"Hello {user.name}, you are {user.age} years old!"
    }