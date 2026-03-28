from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message":"Hello It's Day2"}

@app.get('/greet')
def greet(name:str):
    return {"message":f"Hello {name}, It's Day2"}

@app.get('/addition')
def addition(a: int, b: int):
    return {"Sum of two numbers": f"{a}+{b}={a+b}"}