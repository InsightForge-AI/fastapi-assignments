from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Calculator API")

@app.get("/")
def home():
    return {"message": "Welcome to Calculator API"}

@app.get("/add")
def add(a: float, b: float):
    result = a + b
    return {"operation": "addition", "a": a, "b": b, "result": result}

@app.get("/subtract")
def subtract(a: float, b: float):
    result = a - b
    return {"operation": "subtraction", "a": a, "b": b, "result": result}

@app.get("/multiply")
def multiply(a: float, b: float):
    result = a * b
    return {"operation": "multiplication", "a": a, "b": b, "result": result}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return JSONResponse(status_code=400, content={"error": "Cannot divide by zero"})
    result = a / b
    return {"operation": "division", "a": a, "b": b, "result": result}