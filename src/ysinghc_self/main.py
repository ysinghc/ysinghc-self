from typing import Any, Optional
from unittest.mock import Base

from fastapi import FastAPI
from fastapi.params import Body

from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    mood: Optional[int] = None

my_app = FastAPI()

@my_app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to my website"}

@my_app.get("/v1/posts/")
def get_posts() -> dict[str, str]:
    return {"data": "This is your posts"}

@my_app.post("/v1/posts/new/")
async def create_posts(new_post: Post) -> dict[str, Post]:
    return {"Recieved successfully": new_post}