#!/usr/bin/python3


"""
This is the '3-say_my_name' module.

This module supplies one function, say_my_name. For example,

>>> say_my_name("John", "Smith")
My name is John Smith
"""


def say_my_name(first_name, last_name=""):
    """Prints the string "My name is" followed by first name and last name.

    >>> say_my_name("Walter", "White")
    My name is Walter White

    Parameters:
       first_name (str): The first name to be added
       last_name (str): The last name to be added
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
