""" weight routes """
# pylint: disable=E0401
from typing import List, Union, Optional
from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from api.schemas.weights import WeightSchema, UpdateWeightSchema
from src.infra.configs.database import get_database
from src.infra.repositories.weights import WeightRepository

weight_routes = APIRouter(
    prefix="/weight",
)

@weight_routes.post("/", status_code=status.HTTP_201_CREATED)
async def add_weight(weight: WeightSchema, database: Session = Depends(get_database)):
    """add weight"""
    
    weight = await WeightRepository(database).add_weight(weight)
    return weight


@weight_routes.get("/{name}")
async def get_by_name(name : str, database: Session = Depends(get_database)):
    """ get animal weight by name"""
    weight = await WeightRepository(database).get_by_name(name)
    return weight


@weight_routes.patch("/update/{name}")
async def update_by_name(
    name: str,
    weight: float,
    new_data: WeightSchema,
    database: Session = Depends(get_database),
):
    """update weight data by name"""
    weight = await WeightRepository(database).update_by_name(name, weight, new_data)
    return weight


@weight_routes.delete("/delete/{name}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_name(
    name: str,  
    weight: float,
    database: Session = Depends(get_database)
):
    """delete weight by name"""
    return await WeightRepository(database).delete_by_name(name, weight)