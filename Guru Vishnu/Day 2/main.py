from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Day 2 - GET APIs are running!"}


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI"}


@app.get("/add")
def add(a: int, b: int):
    result = a + b
    return {"a": a, "b": b, "result": result}