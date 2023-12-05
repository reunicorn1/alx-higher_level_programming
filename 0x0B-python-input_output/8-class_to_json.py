#!/usr/bin/python3
"""
This module is '8-class_to_json' and supplies function '8-class_to_json''
"""


def class_to_json(obj):
    """This function returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object. -- 

    It basically extracts information about attributes of an object
    dynamically and creates a dictionary that represents its structure in
    a JSON seriazable form.

    Args:
       obj (an instance of a class)

    Returns:
       a dictionary of class attributes.
    """
    return obj.__dict__
