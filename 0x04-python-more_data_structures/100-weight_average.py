#!/usr/bin/python3
def weight_average(my_list=[]):
    som, div = 0, 0
    if not my_list:
        return 0
    for tup in my_list[:]:
        som += tup[0] * tup[1]
        div += tup[1]
    return som / div
