#!/usr/bin/python3
def uppercase(str):
    """
    uppercase Function That transfer a given string to upper case
    @str: the given string
    """
    _str = ""
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            _str += chr(ord(c) - 32)
        else:
            _str += c
    print("{}".format(_str))
