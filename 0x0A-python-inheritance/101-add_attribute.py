#!/usr/bin/python3
"""This is module ''101-add_attribute'' provides one functon add_attribute."""


def add_attribute(obj, attribute, value):
    """This function adds a new attribute to an object if possible.

    Args:
       obj (obj): an object to add attributes into.
       attribute (string): the attribute to be added
       value: the value of the attribute to be assigned

    Raises:
       TypeError: If the attribute cannot be added to the object.
    """
    setattr(obj, attribute, value)
    if hasattr(obj, '__setattr__') and callable(obj,type(obj). __setattr__)
        raise TypeError("can't add new attribute")
    if (hasattr(obj, '__slots__')
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, class)
