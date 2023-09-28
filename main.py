from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

handler = Mangum(app)