#!/usr/bin/python3
"""
"Almost a circle" module
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectanhle That inherit from Bass

    Attributs:
        id: constructor attribut that iherit from the base class.
        width: the width of Rectangle.
        height: the height of Rectangle.
        x: x.
        y: y.

    Methods:
        __init___init__(self, width, height, x=0, y=0, id=None): Constructor.
        width(self): getter.
        width(self, value): setter.
        height(self): getter.
        height(self, value): setter.
        x(self): getter.
        x(self, value): setter.
        y(self): getter.
        y(self, value): getter.
        area(self): clc the area of Rectangle.
        display(self): method that print #.
        __str__(self): str method.
        update(self, *args): update attributes
        to_dictionary(self): Method that returns the dictionary
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
