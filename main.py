from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/blog/{blog_id}')
def show(blog_id : int):
    return {"data": blog_id}

@app.get('/blog/{blog_id}/comments')
def comments(blog_id : int):
    return {blog_id : {"comments" : {'user1' : 'comment1', 'user2' : 'comment2'}}}