from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(nums: Numbers):
    return {"operation": "addition", "result": nums.a + nums.b}

@app.post("/subtract")
def subtract(nums: Numbers):
    return {"operation": "subtraction", "result": nums.a - nums.b}

@app.post("/multiply")
def multiply(nums: Numbers):
    return {"operation": "multiplication", "result": nums.a * nums.b}

@app.post("/divide")
def divide(nums: Numbers):
    if nums.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"operation": "division", "result": nums.a / nums.b}