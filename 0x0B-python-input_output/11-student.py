#!/usr/bin/python3
"""Student module"""


class Student:
    """
    Student Class

    Methods:
        ___init__: The constructor of the student class.
        to_json:  that retrieves a dictionary
        representation of a Student instance.
        reload_from_json: Method that replaces all attributes
        of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """Constructuer of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method That retrieves a dictionary
        representation of a Student instance.

        Returns:
            If attrs is a list of strings,
            only attribute names contained in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        dic = {}

        if attrs is None:
            return self.__dict__

        for name in attrs[:]:
            if name in self.__dict__.keys():
                dic[name] = self.__dict__[name]
        return dic

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance."""

        for key, val in json.items():
            self.__dict__[key] = val
