#!/usr/bin/python3
"""This is module ''101-add_attribute'' provides one functon add_attribute."""


def add_attribute(obj, attribute, value):
    """This function adds a new attribute to an object if possible.

    Arguments:
       obj (obj): an object to add attributes into.
       attribute (string): the attribute to be added
       value: the value of the attribute to be assigned

    """
    try:
        setattr(obj, attribute,  value)
    except Exception as e:
        raise TypeError("can't add new attribute")
