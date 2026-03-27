from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return{"message:","Hello!"}

@app.get("/hello")
def hello():
    return{"message","Hi!,I am sreeja!"}