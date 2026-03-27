from fastapi import FastAPI

app = FastAPI()

#  Addition

@app.get("/add")
def add(a: int, b: int):
    return {"operation": "addition", "result": a + b}

 # Subtraction

@app.get("/sub")
def subtract(a: int, b: int):
    return {"operation": "subtraction", "result": a - b}

#  Multiplication

@app.get("/mul")
def multiply(a: int, b: int):
    return {"operation": "multiplication", "result": a * b}

#  Division

@app.get("/div")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Division by zero not allowed"}
    return {"operation": "division", "result": a / b}