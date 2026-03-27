from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hi!"}

@app.get("/hello")
def get_data():
    return {"message":"This is mounika's api"}

