#!/usr/bin/python3

"""
6. First state model
"""

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    This is a class that identifies the table STATE using ORM

    attributes or columns of the table are:
      id (int)
      name (str)
    """
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
