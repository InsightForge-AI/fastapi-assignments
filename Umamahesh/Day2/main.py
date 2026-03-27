from fastapi import FastAPI
print("Day 2 running...")
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Day 2 FastAPI"}

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}