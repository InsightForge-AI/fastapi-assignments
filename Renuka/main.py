from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI app"}

@app.get("/hello")
def hello():
    return {"message": "Hello Renuka"}

# Greeting API
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

# Addition API
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}