#!/usr/bin/python3
"""This is module ''7-base_geometry'' provides one class, BaseGeometry."""


class BaseGeometry:
    """This is The BaseGeometry class"""

    def area(self):
        """This function is not implemented yet!"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This function validates value.

        Args:
           name: this is always a string
           value: this should always be an integer

        Raises:
           TypeError
           Value Error
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """This class is for Rectangles

    In the __init__ function we initlize a rectangle using a width and a height

    Arguments:
       width: (int): the width of the rectangle
       height: (int): the height of the rectangle

    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """This function prints and returns the rectangle decription

        Returns:
           A string of the description.
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """This function calculates the area of a rectangle

        Returns:
           the area of a rectangle.
        """
        return self.__width * self.__height
