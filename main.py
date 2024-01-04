"""Entry point for the API."""

import random
from fastapi import FastAPI
from typing import Optional
from datetime import datetime

app = FastAPI()

# class ReadAllProjects():
#     """This base model for reading all projects."""

#     name: str
#     description: Optional[str]
#     creation_date: Optional[datetime]


@app.get('/todo', tags=['Read All Projects'])
async def get_projects() -> dict:
    return{"data": todos}



@app.post("/todo", tags=["Read All Projects"])
async def add_project(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data": "A project has beed added"
    }


todos = [
    {
        "name": "Project 1",
        "Description": "this is the 1st project",
        "Creation_Date": "04.01.2024"
    },
    {
        "name": "Project 2",
        "Description": "this is the 2nd project",
        "Creation_Date": "04.01.2024"
    }
]