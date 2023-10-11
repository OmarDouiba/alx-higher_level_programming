#!/usr/bin/python3
"""Student module"""


class Student:
    """
    Student Class

    Methods:
        ___init__: The constructor of the student class.
        to_json:  that retrieves a dictionary
        representation of a Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """Constructuer of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method That retrieves a dictionary
        representation of a Student instance.
        """
        return self.__dict__
