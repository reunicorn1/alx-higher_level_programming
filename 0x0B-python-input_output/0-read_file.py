#!/usr/bin/python3
"""
This is '0-read_file' module which supplies one function ''read_file''
"""


def read_file(filename=""):
    """This function reads a txt file (UTF8) and prints it to stdout

    Args:
       filename (str): a string of the filename.
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
