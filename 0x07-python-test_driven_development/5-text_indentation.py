#!/usr/bin/python3


"""
This is the '5-text_indentation' module.

This module supplies one function, text_indentation. For example,

>>> text_indentation("Hello there! How are you doing? This is a test.")
Hello there! How are you doing?
<BLANKLINE>
This is a test.
<BLANKLINE>
"""


def text_indentation(text):
    """This function prints test with 2 new lines after each of these
    charcters: ".", "?" and ":"

    There is no space at the beginning or at the end of each printed line.
    And an TypeError exception is raised if <text> wasn't a string.

    Parameters:
       text (str): the long string to be printed and intended with newlines.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    text = text.lstrip().rstrip()
    start = 0
    for index, char in enumerate(text):
        if char in ['?', '.', ':']:
            print(text[start: index + 1] + '\n')
            start = index + 1
            if start == len(text):
                break
            while text[start] == ' ':
                start += 1
    if start < len(text):
        print(text[start:], end="")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
