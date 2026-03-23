from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def home():
    return {'message':'welcome to my first app'}

@app.get('/hello')
def hello():
    return {'message':'hello rana'}