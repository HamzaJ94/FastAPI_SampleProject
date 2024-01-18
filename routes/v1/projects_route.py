# Routing Endpoints

from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get('/')
async def get_projects() -> dict:
    return {"data": projectlist}

@router.post("/")
async def add_projects(projects: dict) -> dict:
    projectlist.append(projects)
    return {
        "data": "A project has been added"
    }

@router.put("/update-projects/{id}")
async def update_projects_list(id: int, body: dict) -> dict:
    for projects in projectlist:
        if int((projects['id'])) == id:
            projects['Description'] = body ['Description']
            return{
                "data": f"Project with id {id} has been updated"
            }
        return{
            "data": f"Project with this id number {id} was not found!"
        }

@router.delete("/remove-projects/{id}")
async def delete_projects(id: int) -> dict:
    for projects in projectlist:
        if int((projects["id"])) == id:
            projectlist.remove(projects)
            return {
                "data": f"Project with id {id} has been deleted"
            }
        return {
            "data": f"Project with id {id} wasn't found!"
        }

projectlist = [
    {
        "id": "1",
        "name": "Project 1",
        "Description": "this is the 1st project",
        "Creation_Date": "04.01.2024"
    },
    {
        "id": "2",
        "name": "Project 2",
        "Description": "this is the 2nd project",
        "Creation_Date": "04.01.2024"
    }
]