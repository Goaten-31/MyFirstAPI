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

class Page(BaseModel):
    name: str
    is_active : bool

@app.get('/')
def index():
    return {"how did you get here?"}

@app.get('/Main_Page')
def gateway():
    return {"Detail": "This is The Main Page of the App"}

@app.get('/Main_Page/{page.name}')
def current_page(page : Page):

    try:
        match page.name:

            case "Project Hub":
                return  { page.name : "All of your projects, private or not, in one concise page"}
            
            case "Public Projects":
                return  { page.name : "Public projects made by people from your contacts"}
            
            case _:
                raise HTTPException(status_code=404, detail="Gateway not found, HTTP status code: 404")
    
    except Exception as e:
        raise HTTPException(status_code=404, detail= f"Gateway not found, HTTP status code: 404, detail: {e}")


@app.get('/Main_Page/{page.name}/{project.id}')
def check(project: Project, page: Page):
    try:
        if page.name == "Project_Hub" and not project.is_private:
            return {project.id : 
                    {"Project Name": project.name, 
                     "Date Created" : project.date_made}}
        else:
            return {"detail" : "projects are currently private"}
        
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

    

@app.post('/projects/Main Page/Add a Project/')
def create_project(project : Project):
    try:
        return {project.id : {f"{project.name} successfully created!"}}
    except Exception as e:
        raise HTTPException(403, f"Forbidden, HTTP status code: 403. Detail: {e}")
    