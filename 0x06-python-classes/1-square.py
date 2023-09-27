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
