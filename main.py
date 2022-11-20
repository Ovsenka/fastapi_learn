from enum import Enum
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

class UserNames(str, Enum):
    one = "John"
    two = "Max"
    three = "Jack" 

class Item(BaseModel):
    name: str
    description: str = None
    price: int = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello,world!"}

@app.get("/get/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/user/{user}")
async def get_user(user: UserNames):
    print(user.value, user)
    return {"user": user}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(title="The ID of the item", ge=1, le=1000), 
    q: str | None = Query(default=...)):
    results = {"item": item_id}
    print
    if q:
        results.update({'q': q})
    return results
    