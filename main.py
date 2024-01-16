"""Entry point for the API."""

from enum import Enum
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()

router = APIRouter()

# @app.get('/projects', tags=['Read All Projects'])
# async def get_projects() -> dict:
#     return {"data": projectlist}


# @app.post("/projects", tags=["Read All Projects"])
# async def add_projects(projects: dict) -> dict:
#     projectlist.append(projects)
#     return {
#         "data": "A project has been added"
#     }

# @app.put("/projects/{id}", tags=["Read All Projects"])
# async def update_projects_list(id: int, body: dict) -> dict:
#     for projects in projectlist:
#         if int((projects['id'])) == id:
#             projects['Description'] = body ['Description']
#             return{
#                 "data": f"Project with id {id} has been updated"
#             }
#         return{
#             "data": f"Project with this id number {id} was not found!"
#         }

# @app.put("/projects/{id}", tags=["Read All Projects"])
# async def update_projects(id: int, body: dict) -> dict:
#     for projects in projectlist:
#         if int((projects['id'])) == id:
#             projects['Description'] = body['Description']
#             return {
#                 "data": f"Project with id {id} has been updated"
#             }
#         return {
#             "data": f"Project with this id number {id} was not found!"
#         }


# @app.delete("/projects/{id}", tags=["Read All Projects"])
# async def delete_projects(id: int) -> dict:
#     for projects in projectlist:
#         if int((projects["id"])) == id:
#             projectlist.remove(projects)
#             return {
#                 "data": f"Project with id {id} has been deleted"
#             }
#         return {
#             "data": f"Project with id {id} wasn't found!"
#         }

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


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Routing Endpoints

@router.get('/projects', tags=['Read All Projects'])
async def get_projects() -> dict:
    return {"data": projectlist}

@router.post("/projects", tags=["Read All Projects"])
async def add_projects(projects: dict) -> dict:
    projectlist.append(projects)
    return {
        "data": "A project has been added"
    }

@router.put("/projects/{id}", tags=["Read All Projects"])
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

@router.delete("/projects/{id}", tags=["Read All Projects"])
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

app.include_router(router, tags=["Projects Re-Routed"])
