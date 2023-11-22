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
        self.__size = size
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
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def __str__(self):
        """This method insruuts Python how to print an instance of this class

        Returns:
           a string of the printed square in the same pattern as my_print()

        """
        strlist = []
        if self.__size != 0:
            if self.__position[1] > 0:
                strlist.append('\n' * (self.__position[1] - 1))
            for i in range(self.__size):
                strlist.append(" " * self.__position[0] + "#" * self.__size)
            return '\n'.join(strlist)
        else:
            return ''

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
        if self.__size != 0:
            for j in range(self.__position[1]):
                print("*")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
