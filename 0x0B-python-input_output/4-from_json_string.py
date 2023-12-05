#!/usr/bin/python3
"""
This is method '4-from_json_string', supplying one function
''from_json_string''
"""
import json


def from_json_string(my_str):
    """This function returns an object represented by a JSON string

    Args:
       my_str (str): the object as a JSON string

    Returns:
       a Python data structure (object)
    """
    return json.loads(my_str)
