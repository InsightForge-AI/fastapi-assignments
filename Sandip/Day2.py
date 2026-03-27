from fastapi import FastAPI

app = FastAPI()

# ✅ Add this
@app.get("/")
def home():
    return {"message": "Server is running"}

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}