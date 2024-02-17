#!/usr/bin/python3

"""
10. Get a state
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
    row = session.query(State, State.id).filter(State.name == bindparam('nme'))
    row = row.params(nme=sys.argv[4]).first()
    if row:
        print(row.id)
    else:
        print("Not found")
