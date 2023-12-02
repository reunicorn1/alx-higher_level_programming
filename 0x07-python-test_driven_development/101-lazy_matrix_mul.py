#!/usr/bin/python3


"""
This is a module for '101-lazy_matrix_mul'.

This module supplies one function lazy_matrix_mul(m_a, m_b). For example,

>>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
array([[ 7, 10],
       [15, 22]])

"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns the multiplication of 2 matrices.

    >>> lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    array([[13, 16]])

    Parameters:
       m_a (list): this is the first list of a list of integers and floats
       m_b (list0: this is the second list of a list of integers and floats

    Returns:
       A list of a list which is the result of mutliplication of matrices.
    """
    a = np.array(m_a)
    b = np.array(m_b)
    return a @ b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
