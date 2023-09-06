#!/usr/bin/python3
def uppercase(_str):
    """
    uppercase Function That transfer a given string to upper case
    @str: the given string
    """
    st = ""
    for c in _str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            st += chr(ord(c) - 32)
        else:
            st += c
    print("{}".format(st, end=''))
