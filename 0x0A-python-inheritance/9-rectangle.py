#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """BaseGeometry
    Methods:
        area(self): print the area of Geometry
    """
    def area(self):
        """Method area raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        self.name = name
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


"""
Rectangle module
"""


class Rectangle(BaseGeometry):
    """
    class Rectangle that inherits from BaseGeometry

    Methods:
        __init__: Constructor.
        area: Clc the area.
        __str__: Print the string format of Rectangle.
    """
    def __init__(self, width, height):
        self.__width = width
        super().integer_validator("width", self.__width)
        self.__height = height
        super().integer_validator("height", self.__height)

    def area(self):
        """Clc the area."""
        return self.__width * self.__height

    def __str__(self):
        """Print the string format of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
