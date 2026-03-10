from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get("/about")
def index():
    return {"data": "First Fully Fledged API!"}
