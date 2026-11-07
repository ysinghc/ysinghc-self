from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to my website"}

@my_app.get("/v1/posts/")
def get_posts() -> dict[str, str]:
    return {"data": "This is your posts"}

@my_app.post("/v1/posts/new/")
async def create_posts(payload: dict = Body(...)) -> dict[str, dict[Any, Any]]:
    return {"Recieved successfully": payload}