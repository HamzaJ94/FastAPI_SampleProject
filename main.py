"""Entry point for the API."""

import logging
from fastapi import FastAPI, APIRouter
from app.routes.api import api_router

app = FastAPI()

router = APIRouter()

# app.include_router(api_router)


# projectlist = [
#     {
#         "id": "1",
#         "name": "Project 1",
#         "Description": "this is the 1st project",
#         "Creation_Date": "04.01.2024"
#     },
#     {
#         "id": "2",
#         "name": "Project 2",
#         "Description": "this is the 2nd project",
#         "Creation_Date": "04.01.2024"
#     }
# ]

# @router.get('/projects', tags=['Read All Projects'])
# async def get_projects() -> dict:
#     return {"data": projectlist}

# @router.post("/projects", tags=["Read All Projects"])
# async def add_projects(projects: dict) -> dict:
#     projectlist.append(projects)
#     return {
#         "data": "A project has been added"
#     }

# @router.put("/projects/{id}", tags=["Read All Projects"])
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

# @router.delete("/projects/{id}", tags=["Read All Projects"])
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

# app.include_router(router, tags=["Projects Re-Routed"])