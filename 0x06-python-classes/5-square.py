#!/usr/bin/python3
""" Defining the class Square"""


class Square:
    """This is the Square class which has no public attributes.

    The __init__ method initilizes the class.

    Args:
       size (int): the integer value of the size of the square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """This is the getter method for the attribute size.
        There's also a setter method which error checks the type of value
        of the size attribute

        Returns:
          The size setted.
        """
        return self.__size

    @size.setter
    def size(self, size):
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

    def my_print(self):
        """This method prints to the stdout character '#'

        Returns:
           None
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
