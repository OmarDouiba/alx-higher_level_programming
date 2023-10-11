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
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Clc the area."""
        return self.__size * self.__size
