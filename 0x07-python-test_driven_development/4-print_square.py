#!/usr/bin/python3


"""
This is the '4-print_square' module.

This module supplies one function, print_square. For example,

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Prints a square with the charcter #.

    This is necessite that size must be an integer >= 0.

    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########

    >>> print_square(-1)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0

    Parameters:
       size (int): The size of the square to be built.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
