#!/usr/bin/python3

"""
This is the '0-add_integer' module.

This module supplies one function, add_integer. For example,

>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """Returns the addition of a and b, which must be integers or floats.

    >>> add_integer(100, -2)
    98

    >>> add_integer(2)
    100

    >>> add_integer(100.3, -2)
    98

    If a and b are not floats or integers, a TypeError exception is raised.

    >>> add_integer(4, 'School')
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
