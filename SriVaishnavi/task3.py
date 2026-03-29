from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    name: str
    age: int

@app.post("/person")
async def create_person(person: Person):
    return {
        "message": f"Person created successfully!",
        "received_data": {
            "name": person.name,
            "age": person.age
        },
        "status": "success"
    }

@app.get("/")
async def root():
    return {"message": "POST API Example", "endpoints": ["/person"]}