"""Entry point for the API."""

import random
from fastapi import FastAPI
from typing import Optional
from datetime import datetime

app = FastAPI()


@app.get('/todo', tags=['Read All Projects'])
async def get_projects() -> dict:
    return{"data": todos}



@app.post("/todo", tags=["Read All Projects"])
async def add_projects(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A project has beed added"
    }

@app.put("/todo/{id}", tags=["Read All Projects"])
async def update_projects(id: int, body: dict) -> dict:
    for todo in todos:
        if int((todo['id'])) == id:
            todo['Description'] = body ['Description']
            return{
                "data": f"Project with id {id} has been updated"
            }
        return{
            "data": f"Project with this id number {id} was not found!"
        }

@app.delete("/todo/{id}", tags=["Read All Projects"])
async def delete_projects(id:int) -> dict:
    for todo in todos:
        if ((todo["id"])) == id:
            todos.remove(todo)
            return{
                "data": f"Project with id {id} has been deleted"
            }
        return{
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