from fastapi import FastAPI

app = FastAPI()

# API 1: Greet
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

# API 2: Add numbers
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}