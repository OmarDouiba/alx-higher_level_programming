#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id)

    for row in data:
        print("{}: {}".format(row.id, row.name))
    Base.metadata.create_all(engine)
