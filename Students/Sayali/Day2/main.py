from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Day 2 API running 🚀"}

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}