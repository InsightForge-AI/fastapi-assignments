from fastapi import FastAPI

app = FastAPI()
# Root API
@app.get("/") 
def read_root():
    return {"Hello World"}