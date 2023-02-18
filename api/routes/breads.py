""" bread routes """
# pylint: disable=E0401
from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from api.schemas.breads import BreadSchema
from src.infra.configs.database import get_database
from src.infra.repositories.breads import BreadRepository


bread_routes = APIRouter(
    prefix="/bread",
)


@bread_routes.post("/", status_code=status.HTTP_201_CREATED)
async def add_bread(bread: BreadSchema, database: Session = Depends(get_database)):
    """add bread"""
    
    bread = await BreadRepository(database).add_bread(bread)
    return bread


@bread_routes.get("/")
async def list_all(
    offset: int = 0, limit: int = 100, database: Session = Depends(get_database)
):
    """list all breads - paginated"""
    bread_list = await BreadRepository(database).list_all(offset, limit)
    return bread_list


@bread_routes.patch("/update/{name}")
async def update_by_name(
    name: str,
    new_data: BreadSchema,
    database: Session = Depends(get_database),
):
    """update bread data by name"""
    bread= await BreadRepository(database).update_by_name(name, new_data)
    return bread


@bread_routes.delete("/delete/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_name(
    name: str,  
    database: Session = Depends(get_database)
):
    """delete bread by name"""
    return await BreadRepository(database).delete_by_name(name)
