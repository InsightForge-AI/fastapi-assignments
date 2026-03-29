from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



class Person(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "Day 3 - POST APIs are running!"}


# POST route - user sends JSON body with name and age
@app.post("/person")
def create_person(person: Person):
    return {
        "message": f"Hello {person.name}!",
        "your_age": person.age,
        "status": "Person received successfully"
    }