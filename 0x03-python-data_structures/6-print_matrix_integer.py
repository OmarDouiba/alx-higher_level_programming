#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    row = len(matrix)
    for i in range(row):
        column = len(matrix[i])
        for j in range(column):
            if j != column - 1:
                print("{:d}".format(matrix[i][j]), end=' ')
            else:
                print("{:d}".format(matrix[i][j]))
#        print()
#    for row in matrix:
#        ln = len(row)
#        for num in row[:ln - 1]:
#            print("{:d}".format(num), end=' ')
#        print("{:d}".format(row[-1]), end='')
#        print()
