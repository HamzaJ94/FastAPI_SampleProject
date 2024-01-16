"""Provides a new router instance, containing all the endpoints available."""

from fastapi import APIRouter

from app.routes.v1 import (   
 projects_route
)

api_router = APIRouter()

# Add the routers
api_router.include_router(projects_route.router, prefix="/projects", tags=["Projects"])