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
        if attrs and type(attrs) is list and all(type(attr)
                                                 is str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)