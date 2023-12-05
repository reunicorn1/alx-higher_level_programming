#!/usr/bin/python3
"""
This module is '9-student' supplying class Student
"""
class_to_json = __import__('8-class_to_json').class_to_json


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

    def to_json(self):
        return class_to_json(self)
