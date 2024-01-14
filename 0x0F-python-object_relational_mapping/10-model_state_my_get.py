#!/usr/bin/python3
"""
script that prints the State object with
the name passed as argument
from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State
                          ).filter(State.name == '{}'.format(argv[4])).count()
    if query == 0:
        print('Not found')
    else:
        print(query)
    session.close()
