#!/usr/bin/python3
"""
script that contains the class definition of a City and
an instance Base = declarative_base()
"""
from model_state import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey


class City(Base):
    """Class City that inherit from base"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
