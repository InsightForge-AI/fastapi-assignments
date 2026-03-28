from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

# Root API
@app.get("/")
def read_root():
    return {"message": "API to get name and age"}

# POST API
@app.post("/person/")
async def create_person(person: Person) -> Person:
    return person

# GET API
@app.get("/person")
async def read_item(name: str, age: int) -> Person:
    return Person(name=name, age=age)