#!/usr/bin/python3


"""
This is a module for '100-matrix_mul'.

This module supplies one function matrix_mul(m_a, m_b). For example,

>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def matrix_validation(m_a, m_b):
    """This function validates the matrices with the requriements"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    elif not m_a or len(m_a) < 1:
        raise ValueError("m_a can't be empty")
    elif not m_b or len(m_b) < 1:
        raise ValueError("m_b can't be empty")
    elif not all(isinstance(elem, list) for elem in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(elem, list) for elem in m_b):
        raise TypeError('m_b must be a list of lists')
    elif any(not isinstance(num, (int, float)) for elem in m_a
             for num in elem):
        raise TypeError('m_a should contain only integers or floats')
    elif any(not isinstance(num, (int, float)) for elem in m_b
             for num in elem):
        raise TypeError('m_b should contain only integers or floats')
    elif any(len(m_a[0]) != len(elem) for elem in m_a):
        raise TypeError('each row of m_a must be of the same size')
    elif any(len(m_b[0]) != len(elem) for elem in m_b):
        raise TypeError('each row of m_b must be of the same size')


def matrix_mul(m_a, m_b):
    """Returns the multiplication of 2 matrices.

    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]

    Parameters:
       m_a (list): this is the first list of a list of integers and floats
       m_b (list0: this is the second list of a list of integers and floats

    Returns:
       A list of a list which is the result of mutliplication of matrices.
    """
    matrix_validation(m_a, m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for r in range(len(m_a)):
        for c in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                new[r][c] += m_a[r][k] * m_b[k][c]
    return new


if __name__ == "__main__":
    import doctest
    doctest.testmod()
