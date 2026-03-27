from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}