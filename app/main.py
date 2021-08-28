import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List

from config import get_settings
from ip import get_ip
from schema import EntryCreateSchema, EntryListSchema

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


@app.get("/entries/", response_model=List[EntryListSchema]) # html -> localhost:8000/abc
def entry_list_view():
    items = [
        {"id": 1, "title": "Hello world", "content": "again"},
        {"id": 2, "title": "Hello worlder", "content": "abc"},
    ]
    return items


@app.post("/entries/", response_model=EntryCreateSchema)
def entry_create_view(data: EntryCreateSchema):
    # data = {"id": 1, "title": "Hello world", "content": "abc"}
    return data