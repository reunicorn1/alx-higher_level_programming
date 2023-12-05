#!/usr/bin/python3
"""
This module is '2-append_write' supplies one method ''append_write''
"""


def append_write(filename="", text=""):
    """This method appends a string at the end of a text file UTF8
    and returns the number of charcters added.

    Args:
       filename (str): a string of the file name
       text (str): the text to be added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
