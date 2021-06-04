import pathlib
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR / "html" # /var/www/html/

app = FastAPI()

templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

@app.get("/", response_class=HTMLResponse) # html -> localhost:8000/
def read_index():
    return templates.TemplateResponse("index.nginx-debian.html", {})

@app.get("/abc") # html -> localhost:8000/abc
def read_abc():
    return {"hello": "abc"}