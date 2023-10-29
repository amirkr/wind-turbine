from fastapi import FastAPI
from starlette.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def hello_world():
    return HTMLResponse(f"<h1>Hello World!</h1>")