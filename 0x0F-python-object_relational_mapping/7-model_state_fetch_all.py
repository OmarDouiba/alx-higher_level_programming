#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1],
            argv[2],
            argv[3]
            ),
        pool_pre_ping=True
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)

    for row in query:
        print("{}: {}".format(row.id, row.name))

    session.close()
