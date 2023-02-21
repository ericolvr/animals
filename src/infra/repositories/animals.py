""" animalrepository """
# pylint: disable=E0401
from typing import Any, List
from fastapi import HTTPException, status
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from api.schemas.animals import AnimalSchema
from src.infra.models.animals import Animal
from src.infra.helpers.animals import AnimalHelper


class AnimalRepository:
    """ animal respository class """

    def __init__(self, database: Session):
        self.database = database

    async def add_animal(self, animal: AnimalSchema) -> Animal:
        """ create animal """

        await AnimalHelper(self.database).check_exists(animal.name)
        
        new = Animal(
            name=animal.name,
            breed=animal.breed,
            age=animal.age,
            maker=animal.marker,
            picture=animal.picture
        )

        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new
    
    async def list_all(self, offset: int, limit: int) -> List[Animal]:
        """list all animals with pagination"""

        animals = self.database.query(Animal).offset(offset).limit(limit).all()
        return animals
    
    async def update_by_name(self, name: str, new_data):
        """update animal by name"""
        result = await AnimalHelper(self.database).get_by_name(name)

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
        """delete animal by name"""
        
        result = await AnimalHelper(self.database).get_by_name(name)

        if not result:
            return result

        self.database.delete(result)
        self.database.commit()

        return {
            "message": "Animaldeleted from database",
            "status_code": status.HTTP_204_NO_CONTENT,
        }
    
