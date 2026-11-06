from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to my website"}

@my_app.get("/v1/posts/")
def get_posts() -> dict[str, str]:
    return {"data": "This is your posts"}