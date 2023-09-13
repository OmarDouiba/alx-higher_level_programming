#!/usr/bin/python3
def common_elements(set_1, set_2):
    ## 1st Method
    return [i for i in set_1 for j in set_2 if i == j]
    ## --------------------
    ## 2nd
    # return set(set_1 & set_2)
    ## --------------------
    ## 3rd
    # for i in set_1:
    #     for j in set_2:
    #         if i == j:
    #             return [i]
