from fastapi import FastAPI

my_app = FastAPI()

@my_app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hellow World"}