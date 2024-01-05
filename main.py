"""Entry point for the API."""

from enum import Enum
from fastapi import FastAPI

app = FastAPI()


@app.get('/todo', tags=['Read All Projects'])
async def get_projects() -> dict:
    return {"data": todos}


@app.post("/todo", tags=["Read All Projects"])
async def add_projects(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A project has been added"
    }

@app.put("/todo/{id}", tags=["Read All Projects"])
async def update_projects_list(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Description'] = body ['Description']
            return{
                "data": f"Project with id {id} has been updated"
            }
        return{
            "data": f"Project with this id number {id} was not found!"
        }

@app.put("/todo/{id}", tags=["Read All Projects"])
async def update_projects(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Description'] = body['Description']
            return {
                "data": f"Project with id {id} has been updated"
            }
        return {
            "data": f"Project with this id number {id} was not found!"
        }


@app.delete("/todo/{id}", tags=["Read All Projects"])
async def delete_projects(id: int) -> dict:
    for todo in todos:
        if (todo["id"]) == id:
            todos.remove(todo)
            return {
                "data": f"Project with id {id} has been deleted"
            }
        return {
            "data": f"Project with id {id} wasn't found!"
        }

todos = [
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
    