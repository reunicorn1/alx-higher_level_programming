#!/usr/bin/python3
"""
This is module '12-pascal_triangle' supplying one function
''pascal_triangle()''
"""


def pascal_triangle(n):
    """This function returns a list of lists of integers representing
    the Pascal's triangle of n.

    Arguments:
       n (int): The size of the triangle.

    Returns:
       a list of lists represnting the Pascal's triangle
    """
    triangle = [[1 for _ in range(i)] for i in range(1, n + 1)]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if j != 0 and j != len(triangle[i]) - 1:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    return triangle
