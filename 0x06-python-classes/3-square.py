#!/usr/bin/python3
""" Defining the class Square"""


class Square:
    """This is the Square class which has no public attributes.

    The __init__ method initilizes the class.

    Args:
       size (int): the integer value of the size of the square.
    """
    def __init__(self, size=0):
        self.set_size(size)

    def get_size(self):
        """This is the getter method for the attribute size.

        Returns:
          The size setted.
        """
        return self.__size

    def set_size(self, size):
        """This is the setter method for the attribute size but not in
        a very pythonic way without using properties.

        Args:
           size: the size of the square.

        Returns:
           None
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """This method returns the current square area.

        Returns:
           square of size
        """
        return self.__size * self.__size
