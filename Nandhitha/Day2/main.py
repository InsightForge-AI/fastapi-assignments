from fastapi import FastAPI

app = FastAPI()

# 1. /greet?name=YourName
@app.get("/greet")
def greet(name: str = "Guest"):
    return {"message": f"Hello, {name}!"}

# 2. /add?a=5&b=10
@app.get("/add")
def add(a: int, b: int):
    result = a + b
    return {"a": a, "b": b, "sum": result}