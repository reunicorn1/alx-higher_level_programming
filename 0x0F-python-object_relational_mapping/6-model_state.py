#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(r'mysql+pymysql://root:Pl#y1999@127.0.0.1/hbtn_0e_6_usa', pool_pre_ping=True)
    Base.metadata.create_all(engine)

