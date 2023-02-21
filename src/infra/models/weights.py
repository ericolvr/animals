""" model class to animal weight """
# pylint: disable=E0401
from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class Weight(Base):
    """ animal weight defintions"""

    __tablename__ = "weights"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, index=True)
    weight = Numeric(10, 2)

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
