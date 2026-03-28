from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request model
class Person(BaseModel):
    name: str
    age: int

# POST API
@app.post("/person")
async def create_person(person: Person):
    return {
        "message": f"Hello {person.name}, age {person.age} received!"
    }