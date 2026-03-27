from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Message":"Hello"}

@app.get('/tutorials')
def tutorials():
    return {"Message": "FastAPI  practice Day-1"}