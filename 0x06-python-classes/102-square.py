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

    def __eq__(self, other):
        """This method defines the behavior for the equality operator ==

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
           A boolean value of either True or False
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        if isinstance(other, int):
            return self.area() == other
        return NotImplemented

    def __ne__(self, other):
        """This method defines the behavior for the equality operator !=.

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
            A boolean value of either True or False
        """
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    def __lt__(self, other):
        """This method defines  the behavior for the equality operator <.

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
           A boolean value of either True or False
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        if isinstance(other, int):
            return self.area() < other
        return NotImplemented

    def __gt__(self, other):
        """This method defines  the behavior for the equality operator >.

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
           A boolean value of either True or False
        """
        result = self.__lt__(other)
        if result is NotImplemented:
            return result
        return not result

    def __le__(self, other):
        """This method defines  the behavior for the equality operator <=.

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
           A boolean value of either True or False

        """
        equal = self.__eq__(other)
        lesser = self.__lt__(other)
        if lesser is NotImplemented or equal is NotImplemented:
            return NotImplemented
        return equal or lesser

    def __ge__(self, other):
        """This method defines  the behavior for the equality operator >=.

        Args:
           other (obj:): the second object to be compared with Square.

        Returns:
           A boolean value of either True or False

        """
        equal = self.__eq__(other)
        greater = self.__gt__(other)
        if greater is NotImplemented or equal is NotImplemented:
            return NotImplemented
        return equal or greater

    def area(self):
        """This method returns the current square area.

        Returns:
           square of size
        """
        return self.__size * self.__size
