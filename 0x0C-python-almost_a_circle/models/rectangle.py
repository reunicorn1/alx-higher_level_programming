#!/usr/bin/python3
"""
This is the module 'models.rectangle' which provides one class
''Rectangle''
"""
from models.base import Base


class Rectangle(Base):
    """This is a class defining a rectangle.

    The __init__ method function initiates the attributes of the
    rectangle.

    Args:
       width (int): the width of the rectangle
       height (int): the height of the rectanlge
       x (int): the coordinates of the rectangle
       y (int): the coordinates of the rectangle
       id (int): id number of the object

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """The string representation of the rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.__x, self.__y,
                        self.__width, self.__height))

    @property
    def width(self):
        """The width property is provided using a getter and a setter
        the value has to be an integer greater than zero. if otherwise
        an exception is raised.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """The height property is provided using a getter and a setter
        the value has to be an integer greater than zero. if otherwise
        an exception is raised.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """This x property is provided using a getter and a setter.
        the value has to be an integer greater than zero. Otherwise
        an exception will be raised.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """This y property is provided using a getter and a setter.
        the value has to be an integer greater than zero. Otherwise
        an excpetion will be raised.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """This method calculates the area of a rectangle.

        Returns:
           the area of a rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Thid method prints in stdout the rectangle with '#' chars.
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        """This function updates the class and assigns an argument to
        each attribute.

        Args:
           *args: no-keyword argument
        """
        attr = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args:
            for i, value in enumerate(args):
                if i in attr:
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if key in attr.values():
                    setattr(self, key, value)

    def to_dictionary(self):
        """This function returns the dictionary representation of a Rectangle.

        Returns:
           the dictionary representation of a Rectangle.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
