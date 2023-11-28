#!/usr/bin/python3


"""
This module supplies one class 'LockedClass'
"""


class LockedClass:
    """This is a class with no way to crate any dynamiclaly instance
    attributes, except first_name

    ths init function initlizes instances but doesn't require inputs.

    """
    __slots__ = ['first_name']

    def __init__(self):
        self.first_name = None
