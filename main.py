from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import date, datetime

app = FastAPI()

class Project(BaseModel):
    id: int
    name: str
    date_made: date

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

@app.get('/project/project_lib/{proj_id}')
def check(project: Project):
    try:
        if project.id:
            return {project.id : {"Project Name": project.name, "Date Created" : project.date_made}}
        else:
            return {0 : "null"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Gateway not found, HTTP status code: 404, detail : {e}")

@app.get('/projects/private')
def private():
    return {"data" : "private project"}

@app.get('/projects/{proj_id}')
def show(proj_id : int):
    try:
        return {"data": proj_id}
    
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Content not found, HTTP status code: 404, detail : {e}")
    
@app.get('/projects/{proj_id}/comments')
def comments(proj_id : int):
    try:
        return {proj_id : {"comments" : {'user1' : 'comment1', 'user2' : 'comment2'}}}
    except:
        raise HTTPException(404, "Error 404, This content was not found")

@app.post('/projects/{proj_id}/{proj_comment}')
def post_comment(proj_id : int, proj_comment : str):
    try:
        return {proj_id : {"comments" : {"user" : proj_comment}}}
    except:
        raise HTTPException(403, "Error 403: Forbidden")