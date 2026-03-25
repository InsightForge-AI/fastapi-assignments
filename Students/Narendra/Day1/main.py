from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Welcome to FastAPI"}

@app.get("/school")
def school():
      return {"School": "Day 1 FastAPI"}