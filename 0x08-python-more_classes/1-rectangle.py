#!/usr/bin/python3
"""
This is '0-rectangle' module.

This module suuplies one class, Rectangle.
"""


class Rectangle:
    """This class creates an empty rectangle.

    No attributes are publically defined yet.
    The __init__ method which works as the constructor for the
    Rectangle instances by providing a height and a width.

    Attributes:
       width (int): is a prive instance attribute
       height (int): is a private instance attribute

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width property is checked and provided using both getter
        and setter functions.
        The value in the setter function is checked if it's an integer
        and not less than zero. If otherwise, an exception is raised.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """The height function has both a getter and a setterr.

        The setter checks for the value if it's an int and above 0.
        If not it raises an excption error.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
