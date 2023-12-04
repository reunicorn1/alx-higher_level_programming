#!/usr/bin/python3

"""
This module is '3-is_kind_of_class' and it supplies one function which is
''is_kind_of_class(obj, a_class)''
"""


def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of the
    specified class, or if the object is an instance of a class that
    inherited from, otherwise False.

    Arguments:
       obj (obj): The object to be tested.
       a_class (obj): The object type to be matched

    Returns:
       Boolean: True or False.

    """
    return isinstance(obj, a_class)
