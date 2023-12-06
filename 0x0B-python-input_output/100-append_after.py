#!/usr/bin/python3
"""
This is the '100-append_after' module, supplying 'append_after' function
"""


def append_after(filename="", search_string="", new_string=""):
    """This function inserts a line of text to a file after each line
    containing a specific string.

    Args:
       filename (str): the string of the file name.
       search_string (str): the string inside the file line in which a new
       sting will get appended to it.
       new_string (str): the string to be added.
    """
    file = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            file.append(line)
            if search_string in line:
                file.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        for line in file:
            f.write(line)
