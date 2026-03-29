# Testing for Postman

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Root API
@app.get("/")
def root():
    return {"message": "Welcome to the API testing with Postman!"}


# Day 1 API
@app.get("/Day1")
def day1():
    return {"message": "Hello World"}


# Day 2 API
@app.get("/Day2")
def day2():
    return {"message": "I'm Running"}


# Greetings API
@app.get("/Day2/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


# Addition API
@app.get("/Day2/add")
def add(a: int, b: int):
    result = a + b
    return {
        "result": result,
        "operation": f"{a} + {b} = {result}"
    }


# Day 3 API
@app.get("/Day3")
def day3():
    return {"message": "Welcome to Day 3 API!"}


# Pydantic Model
class Person(BaseModel):
    name: str
    age: int


# POST API
@app.post("/Day3/person")
async def create_person(person: Person):
    return {
        "message": f"Hello {person.name}, age {person.age} received!"
    }

