#!/usr/bin/python3
"""
inherits_from module
"""


def inherits_from(obj, a_class):
    """
    Write a function that returns True if the object
    is an instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """

    # To check for inheritance, we should
    # first check if the object's class is not the same
    # as the specified class because inheritance happens
    # from other classes.
    # if not type(obj) == a_class: # not the same class
    #     if issubclass(type(obj), a_class): #check inheritance from a_class
    #         return True
    # return False

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
