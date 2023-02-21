""" animal routes """
# pylint: disable=E0401
from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from api.schemas.animals import AnimalSchema
from src.infra.configs.database import get_database
from src.infra.repositories.animals import AnimalRepository

animal_routes = APIRouter(
    prefix="/animal",
)

@animal_routes.post("/", status_code=status.HTTP_201_CREATED)
async def add_animal(animal: AnimalSchema, database: Session = Depends(get_database)):
    """add animal"""
    
    animal = await AnimalRepository(database).add_animal(animal)
    return animal


@animal_routes.get("/")
async def list_all(
    offset: int = 0, limit: int = 100, database: Session = Depends(get_database)
):
    """list all animals - paginated"""
    animal_list = await AnimalRepository(database).list_all(offset, limit)
    return animal_list


@animal_routes.patch("/update/{name}")
async def update_by_name(
    name: str,
    new_data: AnimalSchema,
    database: Session = Depends(get_database),
):
    """update animal data by name"""
    animal = await AnimalRepository(database).update_by_name(name, new_data)
    return animal


@animal_routes.delete("/delete/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_name(
    name: str,  
    database: Session = Depends(get_database)
):
    """delete animal by name"""
    return await AnimalRepository(database).delete_by_name(name)