from fastapi import FastAPI

app = FastAPI()

# Root API
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Hello API with name
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}

# Add API
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}