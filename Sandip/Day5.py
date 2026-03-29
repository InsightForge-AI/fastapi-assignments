from fastapi import FastAPI

app = FastAPI()

# Home
@app.get("/")
def home():
    return {"message": "Calculator API is running"}

# Add
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Subtract
@app.get("/subtract")
def subtract(a: int, b: int):
    return {"result": a - b}

# Multiply
@app.get("/multiply")
def multiply(a: int, b: int):
    return {"result": a * b}

# Divide
@app.get("/divide")
def divide(a: int, b: int):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}

@app.get("/square")
def square(n: int):
    return {"result": n * n}