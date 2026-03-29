from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Day 3 Project - FastAPI"}

class Person(BaseModel):
    name: str
    age: int

@app.post("/person")
def create_person(person: Person):
    return {
        "message": f"{person.name} is {person.age} years old"
    }