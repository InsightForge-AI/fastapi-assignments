#                         --------------Day-2 Video Learning ---------------

from fastapi import FastAPI
app = FastAPI()

# decorator it turns the function into an endpoint 
# HTTP methods like GET, POST , PUT , DELETE etc
# / is root path || if its change to login or post/vote should update in end of URL 
# root is the name of the endpoint
# Request get method url : "/"

@app.get("/")
# URL -http://127.0.0.1:8000
def root():
    return {"message": "Welcome to FastAPI!,Day-2 of Learning FastAPI!!!!!!!"}

@app.get("/posts")
# URL - http://127.0.0.1:8000/posts
def get_posts():
    return {"data": "This is my posts"}



#                                         --------Task Day-2---------------
@app.get("/greet")
async def greet(name: str = None):
    if name:
        return {"message": f"Hello, {name}!"} # http://127.0.0.1:8000/greet?name=Chandra Sekhar
    else:
        return {"message": "Hello, world!"}  # http://127.0.0.1:8000/greet
    


@app.get("/add")
async def add(a: int = 5, b: int = 10):
    return {"result": a + b}
