from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello to Shivam test app"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#
@app.post("/posts")
async def say_hello(payload: dict = Body(...)):
    return {"new_post": f"title {payload['title']}"}


@app.post("/pydantic/posts")
async def say_hello(newPost: Post):
    return {"data" : newPost.dict()}
