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