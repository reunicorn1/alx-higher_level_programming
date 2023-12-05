#!/usr/bin/python3
"""This is the '100-my_int' module, which supplies one function 'MyInt'"""


class MyInt(int):
    """
    This is a class that overwrites the int class

    the == and != are reversed in functionality.
    """
    pass


    def __eq__(self, other):
        """This function reverses the functinality of ==.

        Arguments:
           self (int)
           other (another int)
        """
        diff = 0 if self - other == 0 else 1
        return bool(diff)

    def __ne__(self, other):
        """This function reverses the functinality of !=.

        Arguments:
           self (int)
           other (another int)
        """
        diff = 1 if self - other == 0 else 0
        return bool(diff)
