#!/usr/bin/python3
"""
BaseGeometry class
"""


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
