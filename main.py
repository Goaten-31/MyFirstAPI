from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/gateway')
def gateway():
    return {"Uhm": "This is awkward"}

@app.get('/gateway/{gate_id}')
def gateway_id(gate_id: int):
    match gate_id:
        case 1:
            return {gate_id : {"FinTech" : "MAD Fintech fetcher"} }
        case 2:
            return {gate_id : {"OSINT" : "Vulnerability detector"}}
        case 3:
            return {gate_id : {"System Monitor" : "Monitoring devices and their performance"}}
        case _:
            raise HTTPException(status_code=404, detail="Gateway not found, HTTP status code: 404")

@app.get('/projects/private')
def private():
    return {"data" : "private project"}

@app.get('/projects/{proj_id}')
def show(proj_id : int):
    return {"data": proj_id}

@app.get('/projects/{proj_id}/comments')
def comments(proj_id : int):
    return {proj_id : {"comments" : {'user1' : 'comment1', 'user2' : 'comment2'}}}