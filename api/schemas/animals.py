""" schema for animals """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class AnimalSchema(BaseModel):
    """ data definitions  """
    bread: str
    name: str
    marker: str
    picture: str

    class Config:
        """ settings ORM mode """

        orm_mode = True
        
