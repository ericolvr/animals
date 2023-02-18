""" model class to animals """
# pylint: disable=E0401
from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class Animal(Base):
    """product defintions"""

    __tablename__ = "animals"
    id = Column(Integer, primary_key=True)
    bread = Column(String(50))
    name = Column(String(100), unique=True, index=True)
    marker = Column(Integer)
    picture = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
