import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated
import datetime
from bson import ObjectId
import motor.motor_asyncio
from pymongo import ReturnDocument


app = FastAPI(
    title="Projects",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection and modify projects-endpoint.",
)
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.projects
collection = db.get_collection("ProjectLists")

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]


class ProjectsLists(BaseModel):
    """
    Container for a single project record.
    """

    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    Description: str = Field(...)
    Creation_Date: datetime
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "1",
                "name": "Project 1",
                "Description": "this is the 1st project",
                "Creation_Date": "01.01.2024",
            }
        },
    )


class UpdateProjectsLists(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    name: Optional[str] = None
    Description: Optional[str] = None
    Creation_Date: datetime = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "id": "1",
                "name": "Project 1",
                "Description": "this is the 1st project",
                "Creation_Date": "01.01.2024",
            }
        },
    )


class ProjectCollection(BaseModel):
    """
    A container holding a list of `ProjectsListsModel` instances.

    """
    projects: List[ProjectsLists]


@app.post(
    "/projects/",
    response_description="Add new project",
    response_model=ProjectsLists,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_project(project: ProjectsLists = Body(...)):
    """
    Insert a new project record.

    A unique `id` will be created and provided in the response.
    """
    new_project = await collection.insert_one(
        project.model_dump(by_alias=True, exclude=["id"])
    )
    created_project = await collection.find_one(
        {"_id": new_project.inserted_id}
    )
    return created_project


@app.get(
    "/projects/",
    response_description="List all projects",
    response_model=ProjectCollection,
    response_model_by_alias=False,
)
async def list_projects():
    """
    List all of the project data in the database.

    """
    return ProjectCollection(project=await collection.find().to_list(1000))


@app.get(
    "/projects/{id}",
    response_description="Get a single project",
    response_model=ProjectsLists,
    response_model_by_alias=False,
)
async def show_project(id: str):
    """
    Get the record for a specific project, looked up by `id`.
    """
    if (
        project := await collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return project

    raise HTTPException(status_code=404, detail=f"project {id} not found")


@app.put(
    "/projects/{id}",
    response_description="Update a project",
    response_model=ProjectsLists,
    response_model_by_alias=False,
)
async def update_projects(id: str, project: UpdateProjectsLists = Body(...)):
    """
    Update individual fields of an existing project record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    project = {
        k: v for k, v in project.model_dump(by_alias=True).items() if v is not None
    }

    if len(project) >= 1:
        update_result = await collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": project},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"project {id} not found")

    # The update is empty, but we should still return the matching document:
    if (existing_project := await collection.find_one({"_id": id})) is not None:
        return existing_project

    raise HTTPException(status_code=404, detail=f"project {id} not found")


@app.delete("/projects/{id}", response_description="Delete a project")
async def delete_project(id: str):
    """
    Remove a single project record from the database.
    """
    delete_result = await collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"project {id} not found")
