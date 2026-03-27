from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI app"}

@app.get("/hello")
def hello():
    return {"message": "Hello koushik"}