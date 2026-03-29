#Testing for Postman

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API testing with Postman!"}

#Day 1 Root API
@app.get("/Day1") 
def read_root():
    return {"Hello World"}

# Day 2 Root API
@app.get("/Day2")
def read_root():
    return {"Im Running"}

# Greetings API
@app.get("/Day2/greet")
def greet(name: str):
    name="Sri Harsha"
    return {"message": f"Hello  {name}"}

# Addition API
@app.get("/Day2/add")
def add(a: int, b: int):
    result = a + b
    return {"result": result, "Operation": f"{a} + {b} = {result}"}

class Person(BaseModel):
    name: str
    age: int

# Day 3 Root API
@app.get("/Day3")
def read_root():
    return {"message": "Welcome to Day 3 API!"}

class Person(BaseModel):
    name: str
    age: int

# POST API
@app.post("/Day3/person")
async def create_person(person: Person):
    return {
        "message": f"Hello {person.name}, age {person.age} received!"
    }