""" schema for animal weigths """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class WeightSchema(BaseModel):
    """ data definitions  """
    name: str
    weight: float

    class Config:
        """ settings ORM mode """

        orm_mode = True

class UpdateWeightSchema(BaseModel):
    """ data definitions  """
    weight: Optional[float]

