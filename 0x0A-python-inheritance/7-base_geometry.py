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
