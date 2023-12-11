#!/usr/bin/python3
"""
This is the module 'models.square' which provides one class ''Square''
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a class defining a Square which has a size, a coordinates.

    The __init__ method initiates the attributes of a square.

    Note: the Square inherits from the Rectangle and it has not new attributes,
    as all attributes are used from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the string representation of square that is printed or when
        converted to a string.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """the square has a size but no actual attribute as it inherits
        width and height from the Rectangle, so width and height are
        assigned with the same value.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function updates the class Square tat assigns attributes.

        Args:
           args (no-keyword argument)
           kwargs (key-worded argument)
        """
        attr = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args:
            for i, value in enumerate(args):
                if i in attr:
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if key in attr.values():
                    setattr(self, key, value)

    def to_dictionary(self):
        """This function returns the dictionary representation of a
        Rectangle.

        Returns:
           the dictionary representation of a Rectangle.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
