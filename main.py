from enum import Enum

from fastapi import FastAPI

class UserNames(str, Enum):
    one = "John"
    two = "Max"
    three = "Jack" 

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
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item": item_id, "q": q}
    return {"item": item_id}
    