#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""
    with open(filename, encoding="utf-8") as file_data:
        for line in file_data:
            print(line, end="")
