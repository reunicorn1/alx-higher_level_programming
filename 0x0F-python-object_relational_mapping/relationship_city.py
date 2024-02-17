#!/usr/bin/python3

"""
14. Cities in state
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    This class represents the cities table inside the  hbtn_0e_14_usa
    database, with specific columns assigned as attributes using
    the Object Relation Mapping Concept.

      id (int)
      name (str)
      state_id (int)
    """
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey('states.id'))
