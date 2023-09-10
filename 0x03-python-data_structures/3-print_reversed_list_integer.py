#!/usr/bin/python3
def print_reversed_list_integer(my_list: list) -> list:
    for val in range(len(my_list) - 1, -1, -1):
        print("{}".format(my_list[val]))
