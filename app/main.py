import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config import get_settings
from ip import get_ip

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_PROJECT_DIR = BASE_DIR.parent
TEMPLATE_DIR = ROOT_PROJECT_DIR / "html" # /var/www/html/
app = FastAPI()
settings = get_settings()

templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@app.get("/", response_class=HTMLResponse) # html -> localhost:8000/
def read_index(request:Request):
    return templates.TemplateResponse("index.nginx-debian.html", {"request": request, "title": "Hello World from Jinja", "hostname": get_ip() })

@app.get("/abc") # html -> localhost:8000/abc
def read_abc():
    return {"hello": "world", "db": settings.app_db is not None}