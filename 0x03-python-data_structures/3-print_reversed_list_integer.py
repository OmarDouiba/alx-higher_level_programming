#!/usr/bin/python3
def print_reversed_list_integer(my_list: list) -> int:
    my_list = reversed(my_list)
    for val in my_list:
        print("{:d}".format(val))
