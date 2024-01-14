#!/usr/bin/python3
"""
script that prints all City objects from the database hbtn_0e_14_usa:
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
