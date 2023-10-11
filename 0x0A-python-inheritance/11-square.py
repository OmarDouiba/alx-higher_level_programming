#!/usr/bin/python3
"""Square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle

    Methods:
        __init__: Constructor.
        area: Clc the area.
    """
    def __init__(self, size):
        """Constructor."""
        self.__width = size
        self.__height = size
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """Clc the area."""
        return self.__width * self.__height

    def __str__(self):
        """Print the string format of Square."""
        return "[Square] {}/{}".format(self.__width, self.__height)
