#!/usr/bin/python3

"""
16. List relationship
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City).join(State).order_by(State.id, City.id).all()
    state = None
    for row in rows:
        if row.state != state:
            print("{}: {}".format(row.state.id, row.state.name))
            state = row.state
        print("    {}: {}".format(row.id, row.name))
