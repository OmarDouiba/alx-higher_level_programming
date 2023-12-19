#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa:
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).filter(
        State.id == City.state_id).all()

    for row in query:
        print("{}: ({}) {}".format(row[0].name,
                                   row[1].id,
                                   row[1].name))

    session.close()
    Base.metadata.create_all(engine)
