#!/usr/bin/python3
def uppercase(str):
    """
    uppercase Function That transfer a given string to upper case
    @str: the given string
    """
    for alp in str:
        if ord(alp) >= ord('a') and ord(alp) <= ord('z'):
            print("{}".format(chr(ord(alp) + 32)))
        else:
            print("{}".format(alp))
