#!/usr/bin/python3

"""
This module is '4-inherits_from' and it supplies one function which is
''inherits_from(obj, a_class)''
"""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of the
    specified class that inherited from (directly or indirectly), otherwise
    False.

    Arguments:
       obj (obj): The object to be tested.
       a_class (obj): The object type to be matched

    Returns:
       Boolean: True or False.

    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
