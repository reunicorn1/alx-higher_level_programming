#!/usr/bin/python3
""" Defining the class Square"""


class Square:
    """This is the Square class which has no public attributes.

    The __init__ method initilizes the class.

    Args:
       size (int): the integer value of the size of the square.
       position (tuple): a typle made of 2 positive integers.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """This is the getter method for the attribute position
        There's also a setter method which error checks the type of value
        of the size attribute

        Returns:
           The position setted
        """
        return self.__position

    @position.setter
    def position(self, position):
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

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
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size == 0:
            print()
