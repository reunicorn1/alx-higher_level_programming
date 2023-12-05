#!/usr/bin/python3
"""
This module is '10-student' supplying class Student
"""


def class_to_json(obj):
    """This function returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    It basically extracts information about attributes of an object
    dynamically and creates a dictionary that represents its structure in
    a JSON seriazable form.

    Args:
       obj (an instance of a class)

    Returns:
       a dictionary of class attributes.
    """
    return obj.__dict__


class Student:
    """This class defines a student.

    Attributes:
       first_name
       last_name
       age

    Methods:
       to_json(self)

    The __init__ method initilizes a student by a first name, last name,
    and an age.

    Args:
      first_name (str)
      last_name (str)
      age (int)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function returns a dictionary of the object"""
        dictionary = class_to_json(self)
        if attrs:
            return {attr: dictionary[attr] for attr in attrs if attr
                    in dictionary}
        return dictionary
