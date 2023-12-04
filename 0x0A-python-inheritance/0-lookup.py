#!/usr/bin/python3


""" This module supplies one function 'lookup()' """


def lookup(obj):
    """This function returns the list of available attributes and
    methods of an object.

    Args:
       obj (object): The object to be looked in.

    Returns:
       a list of the attributes and methods

    """
    return dir(obj)
