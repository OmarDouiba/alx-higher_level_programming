#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtx = []
    for row in matrix:
        mtx += [list(map(lambda x: x ** 2, row))]
    # --------------------------------
    # for row in matrix:
    #     matrix = [col ** 2 for col in row]
    #     mtx.append(matrix)
    # ------------------------
    # for row in matrix:
    #     mtx += [[col * col for col in row]]
    return mtx
