from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

# Root API
@app.get("/")
def read_root():
    return {"API to get name and age"}

@app.post("/person/")
async def create_person(person: Person) -> Person:
    return Person(name=person.name, age=person.age)

@app.get("/person")
async def read_item(name: str, age: int) -> Person:
    return Person(name= "Sri Harsha", age= 25)