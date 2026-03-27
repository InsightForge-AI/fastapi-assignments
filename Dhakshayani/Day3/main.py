from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Step 1: Create a request body model
class Person(BaseModel):
    name: str
    age: int

# Step 2: Basic POST API
@app.post("/create-person")
def create_person(person: Person):
    return {
        "message": "Person created successfully",
        "data": person
    }

# Step 3: Another POST API with logic
@app.post("/greet")
def greet_person(person: Person):
    return {
        "message": f"Hello {person.name}, you are {person.age} years old!"
    }

# Step 4: Simple calculator POST API
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/add")
def add_numbers(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {
        "operation": "addition",
        "result": result
    }