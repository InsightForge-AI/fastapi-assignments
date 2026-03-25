from fastapi import FastAPI

app = FastAPI()

# 1️⃣ Greet API
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello  {name}"}

# 2️⃣ Add API
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}