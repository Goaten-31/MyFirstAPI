from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import date, datetime

app = FastAPI()

# I will take a break for 2 weeks
# I need time to rest and then build the frontend

class Project(BaseModel):
    id: int
    name: str
    date_made: date
    date_last_edit : date

class Page(BaseModel):
    name: str
    state : str

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
                raise HTTPException(status_code=404, detail="Gateway not found. Detail: HTTP status code: 404")
    
    except Exception as e:
        raise HTTPException(status_code=404, detail= f"Gateway not found. Detail: {e}")


@app.get('/Main_Page/{page.name}/{page.state}')
def fetch_projects(project: Project, page: Page):
    try:
        if page.state == "fetch":
            return {"Project ID" : project.id,
                    "Project Name": project.name, 
                     "Date Created" : project.date_made,
                     "Date of Last Edit" : project.date_last_edit}
        else:
            return HTTPException(status_code=404, detail=f"Gateway not found. Detail : HTTP status code: 404")  
        
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Gateway not found. Detail : {e}")  

@app.post('/Main_Page/{page.name}/{page.state}')
def create_project(project : Project, page: Page):
    try:
        if page.name == "Home" and page.state == "create":
            project.date_made, project.date_last_edit = datetime.now(), datetime.now()
            return {f"{project.name} successfully created!" : 
                    {"Project ID" : project.id,
                        "Project Name": project.name, 
                        "Date Created" : project.date_made,
                        "Date of Last Edit" : project.date_last_edit}}
        else:
            raise HTTPException(403, f"Forbidden. Detail: HTTP status code: 403.")
    
    except Exception as e:
        raise HTTPException(403, f"Forbidden. Detail: {e}")
    
@app.patch('/Main_Page/{page.name}/{page.state}')
def update_project(project : Project, page: Page):
    try:
        if page.name == "Home" and page.state == "update":
            project.date_made, project.date_last_edit = datetime.now(), datetime.now()
            return {f"{project.name} successfully created!" : 
                    {"Project ID" : project.id,
                        "Project Name": project.name, 
                        "Date Created" : project.date_made,
                        "Date of Last Edit" : project.date_last_edit}}
        else:
            raise HTTPException(403, f"Forbidden. Detail: HTTP status code: 403")
    
    except Exception as e:
        raise HTTPException(403, f"Forbidden. Detail: {e}")