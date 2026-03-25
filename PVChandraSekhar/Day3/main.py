from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

class Post(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}

@app.get("/posts")
def get_posts():
    return {"data": "This is my posts"}

@app.post("/createposts")
def create_posts():
    return {"data": "successfully created posts."}
#                                   --------Day-3 Task---------------

# JSON Payload input in postman 
# {
#   "name": "Chandrasekhar",
#   "age": 22
# }
@app.post("/day3task")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"data": "task."}


@app.post("/day3task2")
def create_day3task2_posts(post: Post):
    print(post)
    print(type(post))
    print(post.dict())
    return {"data": post.dict()}