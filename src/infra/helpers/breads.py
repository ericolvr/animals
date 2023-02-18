""" bread helpers """
# pylint: disable=E0401
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.models.breads import Bread


class BreadHelper:
    """ helpers to bread """

    async def check_exists(self, name: str) -> Any:
        """check bread name already exists before insert"""
        
        bread = self.database.query(Bread).filter(Bread.name == name).first()
        
        if bread:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Bread: {name} has already exists!",
            )

        return
    
    
    def __init__(self, database: Session):
        self.database = database

    async def get_by_name(self, name: str):
        """ check bread exists """
    
        bread = self.database.query(Bread).filter(Bread.name == name).first()

        if not bread:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Bread: {name} not found",
            )

        return bread
