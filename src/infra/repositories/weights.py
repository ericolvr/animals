""" bread repository """
# pylint: disable=E0401
from typing import Any, List
from fastapi import HTTPException, status
from sqlalchemy import asc, desc, and_
from sqlalchemy.orm import Session

from api.schemas.weights import WeightSchema, UpdateWeightSchema
from src.infra.models.weights import Weight

class WeightRepository:
    """ weight repository class """

    def __init__(self, database: Session):
        self.database = database

    async def add_weight(self, weight: WeightSchema) -> Weight:
        """ create weight """

        new = Weight(
            name=weight.name,
            weight=weight.weight
        )

        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new
    
    async def get_by_name(self, name: str) -> Weight:
        """ get animal weight by name """
        weights = self.database.query(Weight).filter(Weight.name == name).all()
        return weights
    
    async def update_by_name(self, name: str, weight: float, new_data):
        """update weight data by name"""
        
        result = self.database.query(Weight).filter(and_(
            Weight.name == name, 
            Weight.weight == weight)
            ).first()

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Animal: {name} and Weigth {weight} not found",
            )

        data = new_data.dict(exclude_unset=True)
        
        for key, value in data.items():
            setattr(result, key, value)
        
        self.database.add(result)
        self.database.commit()
        self.database.refresh(result)

        return result
    
    async def delete_by_name(self, name: str, weight: float):
        """delete weight by name"""
        
        self.database.query(Weight).filter(Weight.name == name).delete()

        result = self.database.query(Weight).filter(and_(
            Weight.name == name, 
            Weight.weight == weight)
            ).first()
        
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Animal: {name} and Weight {weight} not found",
            )

        self.database.delete(result)
        self.database.commit()
        
        return {
            "message": "Weight deleted from database",
            "status_code": status.HTTP_204_NO_CONTENT,
        }
