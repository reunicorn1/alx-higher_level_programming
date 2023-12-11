#!/usr/bin/python3
"""
Unittest for the baseclass
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os

class TestBase(unittest.TestCase):
    """Define unittest for Base class"""
    
    def test_regular(self):
        """This function tests for the class instances id creation"""
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_none(self):
        """This function tests when you create an instance w/ no args"""
        obj1 = Base()
        self.assertEqual(obj1.id, 1)
        obj2 = Base()
        self.assertEqual(obj2.id, 2)
        obj3 = Base()
        self.assertEqual(obj3.id, 3)
    
    def test_negative(self):
        """This function tests when given a negative value"""
        obj = Base(-5)
        self.assertEqual(obj.id, -5)
    
    def test_zero(self):
        """This function tests when the value given is zero"""
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_large_value(self):
        """The ensures that the class can handle large values for id"""
        obj = Base(99999999)
        self.assertEqual(obj.id, 99999999)

    def test_reset_counter(self):
        """This ensures the class properly resets the id if needed"""
        Base._Base__nb_objects = 0
        obj = Base()
        self.assertEqual(obj.id, 1)

class Test_to_json_string(unittest.TestCase):
    """This class tests the static method to_json_string()"""
    def test_dict_0(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        obj1 = json.loads(expected)
        obj2 = json.loads(json_dictionary)
        self.assertTrue(obj1 == obj2)
        self.assertIs(type(json_dictionary), str)

    def test_dict_1(self):
        a_list = []
        r1 = Rectangle(10, 7, 2, 8, 3)
        a_list.append(r1.to_dictionary())
        s1 = Square(10, 2, 1, 4)
        a_list.append(s1.to_dictionary())
        json_dictionary = Base.to_json_string(a_list)
        expected = '[{"x": 2, "width": 10, "id": 3, "height": 7, "y": 8},\
                {"id": 4, "x": 2, "y": 1, "size": 10}]'
        obj1 = json.loads(expected)
        obj2 = json.loads(json_dictionary)
        self.assertTrue(obj1 == obj2)
        self.assertIs(type(json_dictionary), str)

    def test_dict_2(self):
        json_dictionary = Base.to_json_string(None)
        expected = '[]'
        obj1 = json.loads(expected)
        obj2 = json.loads(json_dictionary)
        self.assertTrue(obj1 == obj2)
        self.assertIs(type(json_dictionary), str)

    def test_dict_3(self):
        json_dictionary = Base.to_json_string([])
        expected = '[]'
        obj1 = json.loads(expected)
        obj2 = json.loads(json_dictionary)
        self.assertTrue(obj1 == obj2)
        self.assertIs(type(json_dictionary), str)

    def test_dict_4(self):
        r1 = Rectangle(10, 7, 2, 8, 3)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        expected = '{"x": 2, "width": 10, "id": 3, "height": 7, "y": 8}'
        obj1 = json.loads(expected)
        obj2 = json.loads(json_dictionary)
        self.assertTrue(obj1 == obj2)
        self.assertIs(type(json_dictionary), str)

    def test_dict_5(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_dict_6(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

class Test_Save_To_File(unittest.TestCase):
    """unittests for testing save_to_file method of Base class"""

    @classmethod
    def tearDown(self):
        """Delete any created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_to_file_1(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_to_file_2(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_to_file_3(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_to_file_4(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_to_file_5(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_to_file_6(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_to_file_7(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_to_file_8(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_to_file_9(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_to_file_10(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class Test_from_json_string(unittest.TestCase):
    """Unittests of the static method from_json_string"""
    def test_dict_0(self):
        r1 = Rectangle(10, 7, 2, 8)
        lis_dictionary = list(r1.to_dictionary())
        json_dictionary = Rectangle.to_json_string(lis_dictionary)
        list_output = Rectangle.from_json_string(json_dictionary)
        self.assertEqual(lis_dictionary, list_output)
        self.assertIs(type(list_output), list)
    
    def test_dict_1(self):
        r1 = Rectangle(10, 7, 2, 8, 3)
        s1 = Square(10, 2, 1, 4)
        a_list = [r1.to_dictionary(), s1.to_dictionary()]
        json_dictionary = Base.to_json_string(a_list)
        list_output = Base.from_json_string(json_dictionary)
        self.assertEqual(a_list, list_output)
        self.assertIs(type(list_output), list)

    def test_dict_2(self):
        json_dictionary = Base.to_json_string(None)
        list_output = Base.from_json_string(json_dictionary)
        self.assertEqual([], list_output)
        self.assertIs(type(list_output), list)

    def test_dict_3(self):
        json_dictionary = Base.to_json_string([])
        list_output = Base.from_json_string(json_dictionary)
        self.assertEqual([], list_output)
        self.assertIs(type(list_output), list)

    def test_dict_4(self):
        with self.assertRaises(TypeError):
            json_dictionary = Rectangle.to_json_string()

    def test_dict_5(self):
        with self.assertRaises(TypeError):
            Rectangle.to_json_string([], 1)

class Test_create(unittest.TestCase):
    """unittests for the class method create of the class Base"""
    def test_create_1(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r2), str(r1))

    def test_create_1_1(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_create_2(self):
        s1 = Square(7, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s2), str(s1))

    def test_create_2_1(self):
        s1 = Square(7, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()
