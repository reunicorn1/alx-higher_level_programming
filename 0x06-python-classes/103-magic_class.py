#!/usr/bin/python3

""""This is a module-level docstring. this is used to get pi value"""

import math


class MagicClass:
    """This function appears to take a radius and calculate the
    area ans circumference of a circle.

    There is no public parameters that were defined for this class.

    The __init__ method checks for the value of radius if its a valid
    integer or a float and raises an exception if it's otherwise.

    """
    def __init__(self, radius):
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius
        return None

    def area(self):
        """This method calculates the area of a circle.

        Returns:
           The result of the sum of pi * radius ^ 2.
        """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """This method calculates the circumference of a circle.

        Returns:
           The result of the sum of 2 * pi * radius.
        """
        return (2 * math.pi) * self._MagicClass__radius
