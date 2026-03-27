from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get('/')
def home():
    return {'message': "Hello It's Day3"}

@app.post('/user/')
def create_user(user: User):
    return {
        "message": "User received successfully",
        "name": user.name,
        "age": user.age
    }