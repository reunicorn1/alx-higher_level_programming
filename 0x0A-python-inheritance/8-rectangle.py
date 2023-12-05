#!/usr/bin/python3
"""This is module ''7-base_geometry'' provides one class, BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
