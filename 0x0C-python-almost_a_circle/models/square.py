#!/usr/bin/python3
"""
"Almost a circle" module
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inhiret from Rectangle
    Attributs:
        size: size
        x: x
        y: y
        id: id

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor
        __str__(self): str method.
        size(self): Getter
        size(self, value): Setter
        update(self, *args, **kwargs): Update the class Square.
        to_dictionary(self): Method that returns the dictionary
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
        # self.size = size

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """str method."""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """Update the class Square"""
        up_list = ["id", "size", "x", "y"]
        if args is not None:
            for i, arg in enumerate(args):
                setattr(self, up_list[i], arg)

        if kwargs is not None:
            for kwarg, val in kwargs.items():
                setattr(self, kwarg, val)

    def to_dictionary(self):
        """Method that returns the dictionary"""
        return {"id": self.id, "x": self.x,
                "size": self.size, "y": self.y}
