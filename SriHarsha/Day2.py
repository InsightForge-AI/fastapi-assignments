from fastapi import FastAPI

app = FastAPI()

# Root API
@app.get("/")
def read_root():
    return {"Im Running"}

# Greetings API
@app.get("/greet")
def greet(name: str):
    name="Sri Harsha"
    return {"message": f"Hello  {name}"}

# Addition API
@app.get("/add")
def add(a: int, b: int):
    result = a + b
    return {"result": result, "Operation": f"{a} + {b} = {result}"}