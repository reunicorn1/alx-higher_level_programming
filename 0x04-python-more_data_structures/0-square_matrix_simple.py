#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix[0], list):
        new_matrix = [[x**2 for x in row] for row in matrix]
        return new_matrix
