#!/usr/bin/python3
"""
This is the module '3-to_json_string' suuplying one function ''to_json_string
"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representaiton of an object (string)

    Args:
       my_obj (a serializable object)
    """
    return json.dumps(my_obj)
