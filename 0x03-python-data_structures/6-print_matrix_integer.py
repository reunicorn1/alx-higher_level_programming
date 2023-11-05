#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) != 0:
            for i in range(len(row)):
                print("{:d}".format(row[i]), end=" "
                      if i + 1 != len(row) else "\n")
        else:
            print()
