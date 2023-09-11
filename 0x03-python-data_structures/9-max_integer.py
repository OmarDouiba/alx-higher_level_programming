#!/usr/bin/python3
def max_integer(my_list: list) -> int:
    if not my_list:
        num = None
    else:
        num = my_list[0]
        for i in my_list:
            if i > num:
                num = i
            else:
                num
    return num
