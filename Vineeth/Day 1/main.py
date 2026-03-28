from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def home():
    return {"message": "Hi, This is Vineeth"}

@app.get("/about")
def hello():
    return {"message": "this is the first day of creating API using fast API"}