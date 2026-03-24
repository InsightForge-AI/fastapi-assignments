
from fastapi import FastAPI

app = FastAPI()

# Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to my API 🚀"}

# /greet?name=YourName
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}! 👋"}

# /add?a=5&b=10
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}