from fastapi import  APIRouter
from models.note import Note
from fastapi import FastAPI, Request
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from pymongo import MongoClient


note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn['notes']['notes'].find({})
    print(docs)
    newDocs = list()

    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc['title'],
            "desc": doc['desc'],
            "important": doc['important']
        })
    print(newDocs)
    return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs})


@note.post("/")
async def add_note(request: Request):
    form = await request.form()
    formDict = dict(form)

    formDict['important'] = False if "important" not in formDict.keys() else True
    # formDict['important'] = True if formDict['important'] == "on" else False
    print(form)
    note = conn.notes.notes.insert_one(dict(formDict))

    return {
        "Success":True
    }
