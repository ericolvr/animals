""" bread helpers """
# pylint: disable=E0401
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.models.animals import Animal


class AnimalHelper:
    """ helpers to animal """

    async def check_exists(self, name: str) -> Any:
        """check bread name already exists before insert"""
        
        animal = self.database.query(Animal).filter(Animal.name == name).first()
        
        if animal:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Animal: {name} has already exists!",
            )

        return
    
    
    def __init__(self, database: Session):
        self.database = database

    async def get_by_name(self, name: str):
        """ check animal exists """
    
        animal = self.database.query(Animal).filter(Animal.name == name).first()

        if not animal:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Animal: {name} not found",
            )

        return animal
    
