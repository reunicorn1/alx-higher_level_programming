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
    if hasattr(obj, "__slots__") or type(obj) in [str, int, tuple, float]:
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
