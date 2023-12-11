#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
    obj1 = json.loads(expected)
    obj2 = json.loads(json_dictionary)
    print(obj1 == obj2)
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
