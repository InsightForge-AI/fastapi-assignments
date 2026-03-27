from fastapi import FastAPI
app=FastAPI()

@app.get("/greet")
def greet(nsme: str):
    return {"message:",f"Hello,{name}"}

@app.get("/add")
def add(a: int,b: int):
    return{"result",a+b}