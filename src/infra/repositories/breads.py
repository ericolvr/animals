""" bread repository """
# pylint: disable=E0401
from typing import Any, List
from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from api.schemas.breads import BreadSchema
from src.infra.models.breads import Bread
from src.infra.helpers.breads import BreadHelper


class BreadRepository:
    """ bread respository class """

    def __init__(self, database: Session):
        self.database = database

    async def add_bread(self, bread: BreadSchema) -> Bread:
        """ create bread """

        await BreadHelper(self.database).check_exists(bread.name)
        
        new = Bread(
            name=bread.name
        )

        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new
    

    async def list_all(self, offset: int, limit: int) -> List[Bread]:
        """list all breads with pagination"""

        breads = self.database.query(Bread).offset(offset).limit(limit).all()
        return breads
    
    async def update_by_name(self, name: str, new_data):
        """update bread by name"""
        result = await BreadHelper(self.database).get_by_name(name)

        if not result:
            return result

        data = new_data.dict(exclude_unset=True)
        
        for key, value in data.items():
            setattr(result, key, value)
        
            self.database.add(result)
        self.database.commit()
        self.database.refresh(result)

        return result
    
    async def delete_by_name(self, name: str):
        """delete bread by name"""
        
        result = await BreadHelper(self.database).get_by_name(name)
        
        if not result:
            return result

        self.database.delete(result)
        self.database.commit()
        
        return {
            "message": "Product deleted from database",
            "status_code": status.HTTP_204_NO_CONTENT,
        }


