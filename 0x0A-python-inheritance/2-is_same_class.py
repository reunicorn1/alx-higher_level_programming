#!/usr/bin/python3

"""
This module is '2-is_same_class' and it supplies one function which is
''is_same_class(obj, a_class)''
"""


def is_same_class(obj, a_class):
    """This function returns True if the object is exactly an instance of
    the specified class, otherwise False.

    Arguments:
       obj (obj): The object to be tested.
       a_class (obj): The object type to be matched

    Returns:
       Boolean: True or False.

    """
    return type(obj) is a_class
