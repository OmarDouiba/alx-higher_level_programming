#!/usr/bin/python3
def islower(c):
    """ islower Function That check if c is lower or upper
    @c: the char given
    Return: True if lower, othrwise False.
    """
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
