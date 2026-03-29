from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Calculator API"}

# Addition
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Subtraction
@app.get("/sub")
def sub(a: int, b: int):
    return {"result": a - b}

# Multiplication
@app.get("/mul")
def mul(a: int, b: int):
    return {"result": a * b}

# Division
@app.get("/div")
def div(a: int, b: int):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": a / b}