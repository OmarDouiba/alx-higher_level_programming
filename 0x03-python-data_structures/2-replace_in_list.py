#!/usr/bin/python3
def replace_in_list(my_list: list, idx: int, element: int) -> list:
    if idx < 0 or idx >= len(my_list):
        my_list = my_list
    else:
        # my_list[idx] = element
        # OR
        for i in range(len(my_list) + 1):
            if i == idx:
                my_list[i] = element
    return my_list
