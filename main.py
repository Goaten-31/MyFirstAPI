from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/blog/{blog_id}')
def show(blog_id):
    return {"data": blog_id}

@app.get('/blog/{blog_id}/comments')
def show(blog_id):
    return {blog_id : {"data" : "comments"}}