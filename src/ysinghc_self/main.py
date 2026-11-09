from ast import Not
from email.errors import NonPrintableDefect
from operator import truediv
from sre_constants import SUCCESS
from typing import Any, Optional
from unittest.mock import Base

from fastapi import FastAPI, HTTPException, Response, responses, status
from fastapi.params import Body

from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

my_app = FastAPI()

#in memory storage

latest_id = 2
my_posts = [
    {"id": 1, "title": "This the title of post with id 1", "content": "this is the content of the post with id 1"},
    {"id": 2, "title": "This the title of post with id 2", "content": "this is the content of the post with id 2"}
]

def find_post(id: int)-> dict[str, Any] | None:
    for p in my_posts:
        if p["id"] == id:
            return p

def delete_post(id: int) -> bool:
    for p in my_posts:
        if p["id"] == id:
            my_posts.remove(p)
            return True

    return False

#root path
@my_app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to my website"}


## CRUD for posts
### GET POSTS
@my_app.get("/v1/posts/")
def get_posts() -> dict:
    all_posts = {"data": my_posts}
    return all_posts

### CREATE NEW POST
@my_app.post("/v1/posts/", status_code=status.HTTP_201_CREATED)
def create_post(post: Post) ->dict[str, Any]:
    global latest_id
    post_dict = post.model_dump()
    post_dict["id"] = latest_id+1
    my_posts.append(post_dict)
    latest_id += 1
    return {"success": "true", "data": post_dict}

### GET POST BY ID
@my_app.get("/v1/posts/{id}")
def get_post_id(id):
    try:
        post = find_post(int(id))
        if post == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Input")
        return {"success": "true", "data": post}
    except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Input")

### DELETE A POST BY ID
@my_app.delete("/v1/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post_id(id: int):
    if delete_post(id):
        return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)