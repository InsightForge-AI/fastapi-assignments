from fastapi import FastAPI

app = FastAPI()

# Day 1 APIs
@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/hello")
def hello():
    return {"message": "Hello Bindhu"}


# Day 2 APIs
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}