#!/usr/bin/python3
"""
This is module '6-load_from_json_file' supplying one function
''load_from_json_file
"""
import json


def load_from_json_file(filename):
    """This function creates an object from a JSON file

    Args:
       filename (str): a string og the filename

    Returns:
       The object that was inside the file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
