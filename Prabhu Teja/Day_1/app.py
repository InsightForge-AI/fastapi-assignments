from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome"}

@app.get("/hello")
def hello(name: str = "Guest"):
    return {"message": f"Hello, {name}"}