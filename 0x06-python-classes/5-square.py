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
        # if type(self.__size) is not int:
        if not isinstance(self.__size, int):
            raise Exception("size must be an integer")

        elif self.__size < 0:
            raise Exception("size must be >= 0")

    def area(self) -> int:
        """counting the area of a square
        Return:
            the area of square
        """
        return self.__size ** 2

    def my_print(self):
        """method that print #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
