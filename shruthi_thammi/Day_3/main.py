from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/person")
def create_person(person: Person):
    return {"message": f"Hello {person.name}! You are {person.age} years old."}