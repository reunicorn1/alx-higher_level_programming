#!/usr/bin/python3

"""
This is the '1-my_list' module.

This module supplies one class 'MyList' that inherits from list

>>> my_list = MyList()
>>> my_list.append(1)
>>> my_list.append(4)
>>> my_list.append(2)
>>> my_list.append(3)
>>> my_list.append(5)
>>> print(my_list)
[1, 4, 2, 3, 5]

>>> my_list.print_sorted()
[1, 2, 3, 4, 5]

>>> print(my_list)
[1, 4, 2, 3, 5]

"""


class MyList(list):
    """ This class inherits from the built-in class list.

    The __init__ method initlizes instances based on the super class.

    """
    pass

    def print_sorted(self):
        """This function takes a list and prints it as a new sorted list"""
        new_list = sorted(map(lambda x: int(x), self))
        print(new_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
