#!/usr/bin/python3
"""
This module is 'models.base' supplying one class ''Base''
"""
import json
import os
import csv


class Base:
    """This class will be the base of all other classes.

    The __init__ methods will construct the id number of each instance
    of the class.

    Args:
       id (int): the number id of each instance of the class

    Attributes:
    id (int): the number id of each instance of the class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the JSON string representation of a list
        of dictionaries

        Returns:
           a string representation of a list.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of JSON string representation.

        Args:
           json_string (str): the string representation of a list

        Returns:
           the list of the json string representation
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of a list
        to a file.

        Args:
           list_objs (list): a list of instances who inherits of Base
        """
        saved = []
        if list_objs:
            for obj in list_objs:
                saved.append(obj.to_dictionary())
        saved = Base.to_json_string(saved)
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(saved)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method writes the JSON string representation of a list
        to a csv file.

        Args:
           list_objs (list): a list of instances who inherits of Base
        """
        saved = []
        names_rectangle = ["id", "width", "height", "x", "y"]
        names_square = ["id", "size", "x", "y"]
        if list_objs:
            for obj in list_objs:
                saved.append(obj.to_dictionary())
        filename = "{}.csv".format(cls.__name__)
        fieldnames = names_square if cls.__name__ == "Square" else \
            names_rectangle
        with open(filename, "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in saved:
                writer.writerow(row)

    @classmethod
    def create(cls, **dictionary):
        """This method creates a new instance with all attributes already set

        Args:
           dictionary (dict): a dictionary of all attributes to be setted

        Returns:
           (obj): a new instance of attributes
        """
        s = cls(1, 1)
        s.update(**dictionary)
        return s

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances from a file based on
        the class.

        Returns:
           (list) of instances
        """
        a_list = []
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, encoding="utf-8") as f:
            contents = cls.from_json_string(f.read())
        for item in contents:
            a_list.append(cls.create(**item))
        return a_list

    @classmethod
    def load_from_file_csv(cls):
        """This method returns a list of instances from a file based on
        the class.

        Returns:
           (list) of instances
        """
        a_list = []
        filename = "{}.csv".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row = {key: int(row[key]) for key in row}
                obj = cls.create(**row)
                a_list.append(obj)
        return a_list
