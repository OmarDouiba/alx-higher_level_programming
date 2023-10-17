#!/usr/bin/python3
"""
"Almost a circle" module
"""
import json


class Base:
    """
    Base class

    Attributs:
        __nb_objects: class attributs
        count number of objects.
        id: constructor attribut.

    Methods:
        __init__(self, id): Constructor
        to_json_string(list_dictionaries): returns the JSON
        string representation.
        save_to_file(cls, list_objs): save a list of objects to a JSON file.
        from_json_string(json_string): method that returns
        the list of the JSON string representation
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns the JSON string representation of
        list_dictionaries (where each dictionary in the list represents
        an object/instance)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a JSON file."""
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string(
                            [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON string representation"""
        if json_string is None or json_string == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method  that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        elif cls.__name__ == "Square":
            ins = cls(1)
        else:
            ins = None
        ins.update(**dictionary)
        return ins
