import json

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.jinja2", {"request": request})


@app.get("/step")
async def root(request: Request):
    step = request.query_params.get("step", "start")
    data = json.load(open('dados.json'))
    return data.get(step)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
