#!/usr/bin/python3


"""This is the '2-matrix_divided' module.

This module suuplies one function, matrix_divided(). For example,

>>> matrix = [
... [1, 2, 3],
... [4, 5, 6]
... ]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_check(matrix):
    """Checks the eligibility of the matrix if it meets certain conditions.

    Parameters:
       matrix (list): the list of lists.

    Returns:
       True if it meets all requirements, otherwise, False.
    """
    if not matrix:
        return False
    if not all(isinstance(element, list) and element for element in matrix):
        return False
    for element in matrix:
        if not all(isinstance(number, (int, float)) for number in element):
            return False
    return True


def matrix_divided(matrix, div):
    """Returns a list of all elements divided by div.

    Parameters:
       matrix (list): the list of lists
       div (int/ float): the number that will divide the matrix elements.

    Returns:
       A new list of the divided elements of the matrix.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix_check(matrix):
        raise TypeError(err)
    if not all(len(element) == len(matrix[0]) for element in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(number / div, 2) for number in element]
                  for element in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()
