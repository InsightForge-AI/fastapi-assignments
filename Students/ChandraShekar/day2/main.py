from fastapi import FastAPI

app=FastAPI()

@app.get("/greet")  #Get greet API
def greet(name: str):
    return {"message": f"hello {name} ,Welcome to FastAPI"}

@app.get("/add")   #Get add API
def add(a: int, b : int):
    return{"result": a+b}