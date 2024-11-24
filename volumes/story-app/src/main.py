from fastapi import FastAPI, Request, Response
import os

app = FastAPI()
story_path = os.environ["STORY_FOLDER"] + "story.txt"


@app.get("/")
async def hello():
    return {"message": "Hello World"}


@app.get("/story")
async def read_story(request: Request) -> Response:
    try:
        with open(story_path, 'r') as f:
            lines = f.readlines()
            return Response(str(lines), 200)

    except Exception as ex:
        msg = f"Exception while reading the story: {str(ex)}"
        return Response(msg, 500)


@app.post("/story")
async def write_story(request: Request) -> Response:
    try:
        req = await request.json()
        story_text = req["text"]
        with open(story_path, 'a+') as f:
            f.write(story_text)
            return Response("Story written to file", 200)
    except Exception as ex:
        msg = f"Exception while writing story: {str(ex)}"
        return Response(msg, 500)