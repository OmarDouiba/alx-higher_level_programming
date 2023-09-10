#!/usr/bin/python3
def replace_in_list(my_list: list, idx: int, element: int) -> list:
    if idx < 0 or idx >= len(my_list):
        my_list = None
    else:
        my_list[idx] = element
    return my_list
