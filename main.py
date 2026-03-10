from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get("/about")
def index():
    return {"message": "First Fully Fledged API!"}
