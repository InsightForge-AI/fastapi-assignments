from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
     return{"message": "Hello World!"}

@app.get("/hello")
def hello():
     return {"Greetings ": "Hi! This is Nishant's first API"}