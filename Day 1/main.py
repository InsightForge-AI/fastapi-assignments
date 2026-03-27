from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI im Mahesh"}

@app.get("/hello")
def say_hello():
    return {"message": "/Hello"}


