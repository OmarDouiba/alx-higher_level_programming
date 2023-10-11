#!/usr/bin/python3
"""
Rectangle module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry



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
