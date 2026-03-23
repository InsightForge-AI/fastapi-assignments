from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def read_root():
    return {"Hello": "BomB planted successfully. Defuse it here: http://127.0.0.1:8000/unplant. Time's ticking!"}

@app.get('/unplant')
def unplant_bomb():
    return {"message": "BomB exploded successfully :-) BOOM"}

# to run use cd Thrun and then run the command below
# python -m uvicorn day1:app --reload