from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import date, datetime

app = FastAPI()

class Project(BaseModel):
    id: int
    name: str
    date_made: date
    date_last_edit : date
    activity_status: str
    comments : Optional[str] = None


@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/Main_Page')
def gateway():
    return {"Uhm": "This is awkward"}

@app.get('/Main_Page/{Page_name}')
def gateway_id(Page_name: str):

    try:
        match Page_name:

            case "Artsy":
                return {Page_name : {"Artsy" : "All of my collages and artworks"} }
            
            case "Cody":
                return {Page_name : {"Cody" : "My projects, what probably interests you"}}
            
            case "Writey":
                return {Page_name : {"Writey" : "All my written works"}}
            
            case "Contacty":
                return {Page_name : {"Contacty" : "My contact information"}}
            
            case _:
                raise HTTPException(status_code=404, detail="Gateway not found, HTTP status code: 404")
    
    except Exception as e:
        raise HTTPException(status_code=404, detail= f"Gateway not found, HTTP status code: 404, detail: {e}")


@app.get('/project/{Page_name}/{project.id}')
def check(project: Project):
    try:
        if project.id:
            return {project.id : 
                    {"Project Name": project.name, 
                     "Date Created" : project.date_made}}
        else:
            return {0 : "null"}
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Gateway not found, HTTP status code: 404, detail : {e}")


@app.get('/projects/private')
def private():
    return {"data" : "private project"}

    

@app.post('/projects/{Page_name}/{project.id}/{project.comments}')
def post_comment(project : Project):
    try:
        return {project.id : {"comments" : {"user" : project.comments}}}
    except:
        raise HTTPException(403, "Error 403: Forbidden")
    