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
    is_private : bool


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
def check(project: Project, limit=5):
    try:
        if project.id < limit and not project.is_private:
            return {project.id : 
                    {"Project Name": project.name, 
                     "Date Created" : project.date_made}}
        else:
            return {"detail" : "project id out of scope or projects are currently private"}
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Gateway not found, HTTP status code: 404, detail : {e}")


@app.get('/projects/private/{project.id}')
def private(project: Project):
    try:
        if project.is_private:
            return {project.id :{
                "Project Name" : project.name,
                "Date Created" : project.date_made}}
        else:
            return {"detail" : "No private projects"}
    except Exception as e:
        raise HTTPException(status_code=403, detail=f"Forbidden, HTTP Status Code: 403. Detail : {e}")

    

@app.post('/projects/{Page_name}/{project.id}/{project.comments}')
def post_comment(project : Project):
    try:
        return {project.id : {"comments" : {"user" : project.comments}}}
    except:
        raise HTTPException(403, "Error 403: Forbidden")
    