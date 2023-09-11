#!/usr/bin/python3
def divisible_by_2(my_list: list) -> list:
    tup = ()
    for num in sorted(my_list):
        num = abs(num)
        if not num % 2:
            tup += (True,)
        else:
            tup += (False,)
    return tup
