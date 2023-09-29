#!/usr/bin/python3
"""
square class with methods and attributes
"""


class Square:
    """define variables and methods"""
    def __init__(self, size: int = 0) -> None:
        """
        Initializes a new Square instance.
        Args:
            size: the size of Square
        """
        self.__size = size

    @property
    def size(self):
        """ getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """counting the area of a square
        Return:
            the area of square
        """
        return self.__size ** 2
