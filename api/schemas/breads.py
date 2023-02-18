""" schema for categories """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class BreadSchema(BaseModel):
    """ data definitions  """

    name: str

    class Config:
        """ settings ORM mode """

        orm_mode = True
        