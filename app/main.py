from fastapi import FastAPI

app = FastAPI()

@app.get("/") # html -> localhost:8000/
def read_index():
    return {"hello": "world this is supervisor"}

@app.get("/abc") # html -> localhost:8000/abc
def read_abc():
    return {"hello": "abc"}