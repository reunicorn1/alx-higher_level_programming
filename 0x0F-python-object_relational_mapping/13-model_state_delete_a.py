#!/usr/bin/python3

"""
12. Update a state
"""

import sys
from sqlalchemy import create_engine, bindparam
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    objs = session.query(State).filter(State.name.like('%a%'))
    for obj in objs:
        session.delete(obj)
    session.commit()
