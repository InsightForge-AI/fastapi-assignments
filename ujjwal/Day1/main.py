from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def first():
    return {"message":"Hi, This is Ujjwal"}

@app.get("/about")
async def about():
    return {"message": "this is the first day of creating API using fast api"}
