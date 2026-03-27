from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World!"}

@app.get("/hello")
def hello():
    return {"message": "Hi! this is first API"}

# NEW: greet API
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

# NEW: add API
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}