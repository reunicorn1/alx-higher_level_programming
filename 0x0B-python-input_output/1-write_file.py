#!/usr/bin/python3
"""
This module is '1-write_file' supplies one function ''write_file''
"""


def write_file(filename="", text=""):
    """This function writea string to a textfile UFT8 and returns the
    number of chars written.

    Args:
       filename (str): a string of the file name
       text (str): a string to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
