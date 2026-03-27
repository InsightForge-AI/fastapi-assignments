from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "use /greet/name to get a personalized greeting and /add/a/b to add two numbers."}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}"}

@app.get('/add/{a}/{b}')
def add(a:int,b:int):
    return {'result': a+b}
