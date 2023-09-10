#!/usr/bin/python3
def new_in_list(my_list: list, idx: int, element: int) -> list:
    if my_list:
        ln = len(my_list)
        if idx < 0 or idx >= ln:
            pass
        else:
            my_list = my_list.copy()
            my_list[idx] = element
        return my_list
