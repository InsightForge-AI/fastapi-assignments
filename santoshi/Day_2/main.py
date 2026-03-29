from fastapi import FastAPI
app=FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message":f"Hello {name}!"}

@app.get("/add")
def adding(a: int,b: int):
    result=a+b
    return{"message":result}