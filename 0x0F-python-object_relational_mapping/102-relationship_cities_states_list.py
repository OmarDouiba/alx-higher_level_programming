#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]
        ),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(City.state_id == State.id)

    for city, state in query:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    # OR
    # query = session.query(State)
    # for state in query:
    #     for city in state.cities:
    #         print("{}: {} -> {}".format(city.id, city.name,
    #                                     state.name))
    session.close()
