from fastapi import FastAPI
import sys

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "Hello World"}

@app.get("/exit")
async def exit():
    sys.exit(1)