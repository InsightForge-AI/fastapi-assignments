#Task _1
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

#Task_2
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

#Task_3
from pydantic import BaseModel
class Person(BaseModel):
    name: str
    age: int

@app.post("/person")
def create_person(person: Person):
    return {"message": f"Hello {person.name}! You are {person.age} years old."}
