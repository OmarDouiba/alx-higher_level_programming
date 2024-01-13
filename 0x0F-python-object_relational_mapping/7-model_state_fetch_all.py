#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    # # Create an MySql database engine in memory
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306/{}""".format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    # Create a session factory using sessionmaker
    Session = sessionmaker(bind=engine)
    # Create a session instance(object)
    session = Session()

    query = session.query(State).order_by(State.id).all()
    
    for state in query:
        print("{}: {}".format(state.id, state.name))

    session.close()
