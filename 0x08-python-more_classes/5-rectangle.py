#!/usr/bin/python3
"""
Rectangle Module
"""


class Rectangle:
    """
    A class to represent Rectangle

    Methods:
        __init__(self, width=0, height=0): Initializes a new Rectangle instance
        width (property): Getter method for the width attribute
        width (setter): Setter methode for the width attribute  with validation
        height (getter): Getter method for the height attribute
        height (setter): Setter method for the height attribute with validtion
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Custom string representation of the rectangle.
        __repr__(self): Custom representation of the rectangle for debugging.
        __del__(self): Destructor method to clean up instances.
    """
    def __init__(self, width: int = 0, height: int = 0) -> None:
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): the width of rectangle.
            height (int): the height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute with validation.

        Args:
            value (int): the width to set.
        Raises:
            TypeError, ValueError: If the width is not integer or
            less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute with validation.

        Args:
            value (int): the height to set.

        Raises:
            TypeError, ValueError: if the height is not integer or
            less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__width) + (self.__height + self.__height)

    def __str__(self):
        """
        Custom string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        ptr = ""
        if self.__width == 0 or self.__height == 0:
            return ptr

        for i in range(self.__height):
            for j in range(self.__width):
                ptr += "#"
            if i < self.__height - 1:
                ptr += "\n"
        return ptr

    def __repr__(self):
        """
        Custom representation of the rectangle for debugging.

        Returns:
            str: A string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method to clean up instances."""
        print("Bye rectangle...")
