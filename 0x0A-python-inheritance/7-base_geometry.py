#!/usr/bin/python3


"""
This is module ''7-base_geometry'' provides one class, BaseGeometry.
"""


class BaseGeometry:
    """This is a class that does not do anything until it's lastly
    updated on 5th Dec, 12:18 am.

    5th Dec, 12:22 am: an area method is defined which also does nothing
    but raising an exception with the message (area() is not implemented

    5th Dec, 12:51 am: A second method is added 'integer_valiator' which
    validates value.

    """
    pass

    def area(self):
        """This function should calculate the area of the geometric shape in
        the future. For now it only raises and exception of not being
        implemented yet!
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This function validates value.

        Parameters:
           name: this is always a string
           value: this should always be an integer

        """
        if type(value) is not int:
            raise TypeError('<name> must be an integer')
        if value < 1:
            raise ValueError('<name> must be greater than 0')
