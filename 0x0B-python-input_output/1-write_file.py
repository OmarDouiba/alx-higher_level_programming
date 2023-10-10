#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written."""

    with open(filename, "w", encoding="utf-8") as w_file:
        return w_file.write(text)
