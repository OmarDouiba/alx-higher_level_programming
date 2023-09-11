#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()) -> tuple:
    len_a, len_b = len(tuple_a), len(tuple_b)
    if len_a == 0:
        tuple_a += (0, 0)
    elif len_a == 1:
        tuple_a += (0, )
    elif len_b == 0:
        tuple_b += (0, 0)
    elif len_b == 1:
        tuple_b += (0, )
    add = ()
    for i in range(2):
        add += (tuple_a[i] + tuple_b[i],)
    return add
#    len_a, len_b = len(tuple_a), len(tuple_b)
#    if len_a < 2 or len_b < 2:
#        if len_a < 2:
#            if tuple_a == ():
#                tuple_a = (0, 0)
#            else:
#                tuple_a += (0,)
#        else:
#            if tuple_b == ():
#                tuple_b = (0, 0,)
#            else:
#                tuple_b += (0,)
#    add = tuple()
#    for i, j in zip(tuple_a, tuple_b):
#        add += (i + j,)
#    return format(add)
