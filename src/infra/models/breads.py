""" model class to breads """
# pylint: disable=E0401
from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class Bread(Base):
    """ bread defintions"""

    __tablename__ = "breads"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, index=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
