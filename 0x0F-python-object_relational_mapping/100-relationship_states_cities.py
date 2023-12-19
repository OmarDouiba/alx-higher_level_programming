#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
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

    city = City(name='San Francisco')
    state = State(name='California', cities=[city])

    session.add(city)
    session.add(state)
    session.commit()
    session.close()
