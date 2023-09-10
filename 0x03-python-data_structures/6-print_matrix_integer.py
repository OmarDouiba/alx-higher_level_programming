#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    row = len(matrix)
    for i in range(row):
        column = len(matrix[i])
        for j in range(column):
            if j != column - 1:
                print("{}".format(matrix[i][j]), end=' ')
            else:
                print("{}".format(matrix[i][j]))
