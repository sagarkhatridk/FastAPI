from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

conn =  MongoClient("mongodb+srv://sagarkhatridk:{password}@cluster0.wlv1zuq.mongodb.net/notes")

app = FastAPI()





@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
