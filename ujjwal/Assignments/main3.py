from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()

@app.post("/createpost")
def create_post(payload:dict=Body(...)):
    print(payload)
    return {
    "message": "successfully created post",
    "new_post": f"title: {payload['title']} content: {payload['content']}"
           }