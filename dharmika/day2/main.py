from fastapi import FastAPI

app = FastAPI()

# Basic API
@app.get("/")
def home():
    return {"message": "Welcome API 🚀"}

# New APIs
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {Dharmika}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}