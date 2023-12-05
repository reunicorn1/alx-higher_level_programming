#!/usr/bin/python3
"""This is the '5-save_to_json_file' module, supplying one function
''save_to_json_file''
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an Object to a text file using JSON representation

    Args:
       my_obj (obj): the object to be added to the file
       filename (str): a tring of the file name.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
