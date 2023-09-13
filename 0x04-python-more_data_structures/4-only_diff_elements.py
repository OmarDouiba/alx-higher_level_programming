#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1.symmetric_difference(set_2)
    # return set_1 ^ set_2
    # return set(list({ele for ele in set_1 if ele not in set_2}) +
    # list({ele for ele in set_2 if ele not in set_1}))
