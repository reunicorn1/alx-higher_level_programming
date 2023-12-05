#!/usr/bin/python3
"""This is module ''10-square'' provides one class, Square."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class defines the geometric shape square.

    The __init__ function initiates a size for the square.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """This function calculates the area of a square

        Returns:
           The area of a square.
        """
        return self.__size ** 2
