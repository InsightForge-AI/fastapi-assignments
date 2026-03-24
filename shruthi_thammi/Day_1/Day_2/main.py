from fastapi import FastAPI   # ← make sure this line is at top

app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}