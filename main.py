from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/projects/private')
def private():
    return {"data" : "private project"}

@app.get('/projects/{proj_id}')
def show(proj_id : int):
    return {"data": proj_id}

@app.get('/projects/{proj_id}/comments')
def comments(proj_id : int):
    return {proj_id : {"comments" : {'user1' : 'comment1', 'user2' : 'comment2'}}}