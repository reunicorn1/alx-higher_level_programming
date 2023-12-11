#!/usr/bin/python3
"""Unittest for the class Rectangle
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class test_instantation(unittest.TestCase):
    """Define unittest for the class Square"""
    def test_1(self):
        """This function tests the basic usage of Square class"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        s4 = Square(7, 1, 6, 100)
        self.assertEqual(str(s4), "[Square] (100) 1/6 - 7")

    def test_2(self):
        """testing giving zero args, more than it should arguments"""
        self.assertRaises(TypeError, Square)
        self.assertRaises(TypeError, Square, 2, 3, 4, 5, 6)

    def test_isinstance(self):
        """testing if Square is an instance of Rectangle and Base"""
        s1 = Square(5)
        self.assertIsInstance(s1, Rectangle)
        self.assertIsInstance(s1, Base)

    def test_issubclass(self):
        """testing if Square is a subclass of Rectangle and Base"""
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_size_private(self):
        """testing if we can access a private attribute"""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)


class test_getters_setters(unittest.TestCase):
    """This function tests using the getters and setters functions in Square"""
    def test_getter_width(self):
        s1 = Square(3, 1, 3)
        self.assertEqual(s1.width, 3)

    def test_getter_height(self):
        s1 = Square(3, 1, 3)
        self.assertEqual(s1.height, 3)

    def test_getter_x(self):
        s1 = Square(2, 2)
        self.assertEqual(s1.x, 2)

    def test_getter_y(self):
        s1 = Square(4, 6, 2)
        self.assertEqual(s1.y, 2)

    def test_id(self):
        s1 = Square(5, 6, 1, 0)
        self.assertEqual(s1.id, 0)

    def test_setter_width(self):
        s1 = Square(3, 1, 3)
        s1.width = 10
        self.assertEqual(s1.width, 10)

    def test_setter_height(self):
        s1 = Square(3, 1, 3)
        s1.height = 7
        self.assertEqual(s1.height, 7)

    def test_setter_x(self):
        s1 = Square(2, 2)
        s1.x = 9
        self.assertEqual(s1.x, 9)

    def test_setter_y(self):
        s1 = Square(4, 6, 2)
        s1.y = 10
        self.assertEqual(s1.y, 10)

    def test_negative_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, -2)

    def test_zero_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Square, 0)

    def test_negative_x(self):
        self.assertRaisesRegex(ValueError, "x must be >= 0", Square, 2, -3, 4)

    def test_negative_y(self):
        self.assertRaisesRegex(ValueError, "y must be >= 0", Square, 2, 4, -5)

    def test_not_int_width(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, "2", 3)

    def test_not_int_x(self):
        self.assertRaisesRegex(TypeError, "x must be an integer", Square, 2, "4", 5)

    def test_not_int_y(self):
        self.assertRaisesRegex(TypeError, "y must be an integer", Square, 2, 3, "5")

    def test_width_inf(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, float('inf'), 3)

    def test_width_nan(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, float('nan'), 3)

    def test_width_none(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, None, 3)

    def test_width_float(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Square, 3.4, 3)

class test_size(unittest.TestCase):
    """This class contain the functions that tests the size getters and setters"""
    def test_size_getter(self):
        s1 = Square(5, 2, 3, 9)
        self.assertEqual(s1.size, 5)

    def test_size_setter(self):
        s1 = Square(4, 1, 9, 2)
        self.assertEqual(s1.size, 4)

    def test_size_not_int(self):
        s1 = Square(4, 1, 9, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "3"

    def test_size_negative(self):
        s1 = Square(4, 1, 9, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -10

class test_area(unittest.TestCase):
    """This class contains functions which tests the area of a square"""
    def test_area_1(self):
        """This function tests the area public method of a Square"""
        r = Square(1)
        self.assertEqual(r.area(), 1)

    def test_area_2(self):
        r = Square(100000)
        self.assertEqual(r.area(), 10000000000)

    def test_area_3(self):
        r = Square(5, 3, 4, 100)
        self.assertEqual(r.area(), 25)

class test_display(unittest.TestCase):
    """This class prints the display of the Square"""
    def test_display_1(self):
        """This function prints the display of the Square"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(5)
            s1.display()
            output = "#####\n#####\n#####\n#####\n#####\n"
            self.assertEqual(fake_out.getvalue(), output)
        
    def test_display_2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(2)
            s1.display()
            output = "##\n##\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_display_3(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(1)
            s1.display()
            output = "#\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_display_coordinates_1(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(3, 2, 1)
            s1.display()
            output = "\n  ###\n  ###\n  ###\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_display_coordinates_2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(4, 1, 2, 3)
            s1.display()
            output = "\n\n ####\n ####\n ####\n ####\n"
            self.assertEqual(fake_out.getvalue(), output)
    
    def test_display_coordinates_3(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(2, 1)
            s1.display()
            output = " ##\n ##\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_print(self):
        """This function tests the string representation of instances"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(1, 1)
            print(s1)
            output = "[Square] (1) 1/0 - 1\n"
            self.assertEqual(fake_out.getvalue(), output)
    
    def test_str_1(self):
        s1 = Square(5, 3, 2, 4)
        self.assertEqual(str(s1), "[Square] (4) 3/2 - 5")

    def test_str_2(self):
        s1 = Square(3, id=10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 3")

    def test_str_3(self):
        Base._Base__nb_objects = 0
        s1 = Square(1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 1")

class test_display(unittest.TestCase):
    """This class contains all tests related to the display function"""
    def test_update_1(self):
        """This function tests the update function"""
        s1 = Square(5, 10, 2, 100)
        s1.update()
        self.assertEqual(str(s1),"[Square] (100) 10/2 - 5")

    def test_update_2(self):
        s1 = Square(5, 10, 2, 100)
        s1.update(500)
        self.assertEqual(str(s1),"[Square] (500) 10/2 - 5")

    def test_update_3(self):
        s1 = Square(5, 10, 2, 100)
        s1.update(500, 4)
        self.assertEqual(str(s1),"[Square] (500) 10/2 - 4")

    def test_update_4(self):
        s1 = Square(5, 10, 2, 100)
        s1.update(500, 5, 8)
        self.assertEqual(str(s1),"[Square] (500) 8/2 - 5")

    def test_update_5(self):
        s1 = Square(5, 10, 2, 100)
        s1.update(500, 5, 8, 4)
        self.assertEqual(str(s1),"[Square] (500) 8/4 - 5")

    def test_update_6(self):
        s1 = Square(5, 10, 2, 00)
        s1.update(500, 5, 8, 4, 1)
        self.assertEqual(str(s1),"[Square] (500) 8/4 - 5")

    def test_update_setter(self):
        """This function tests the functionality of setters and getters in update"""
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        self.assertRaisesRegex(TypeError, "width must be an integer", s1.update, 89, "2")
        self.assertRaisesRegex(ValueError, "width must be > 0", s1.update, 89, -3)
        self.assertRaisesRegex(ValueError, "x must be >= 0", s1.update, 89, 2, -2)
        self.assertRaisesRegex(TypeError, "x must be an integer", s1.update, 89, 2, "2")
        self.assertRaisesRegex(ValueError, "y must be >= 0", s1.update, 89, 2, 4, -10)
        self.assertRaisesRegex(TypeError, "y must be an integer", s1.update, 89, 2, 4, "7")

    def test_update_kwargs_1(self):
        s1 = Square(8, 12, 2, 3)
        self.assertEqual(str(s1), "[Square] (3) 12/2 - 8")
        s1.update(id=100, size= 10, width=5, height=5)
        self.assertEqual(str(s1), "[Square] (100) 12/2 - 10")

    def test_update_kwargs_2(self):
        s1 = Square(8, 12, 2, 3)
        s1.update(x=3, size=8, id=42)
        self.assertEqual(str(s1), "[Square] (42) 3/2 - 8")

    def test_update_kwargs_3(self):
        s1 = Square(8, 8, 3, 3)
        self.assertEqual(str(s1), "[Square] (3) 8/3 - 8")
        s1.update(nonexistant=100, random=5, wrong=5)
        self.assertEqual(str(s1), "[Square] (3) 8/3 - 8")

    def test_update_kwargs_4(self):
        s1 = Square(8, 8, 3, 3)
        s1.update(34, 5, 1, x=7)
        self.assertEqual(str(s1), "[Square] (34) 1/3 - 5")

    def test_update_kwargs_5(self):
        s1 = Square(8, 8, 3, 3)
        s1.update(y=5)
        self.assertEqual(str(s1), "[Square] (3) 8/5 - 8")

    def test_update_kwargs_6(self):
        s1 = Square(8, 8, 3, 3)
        self.assertEqual(str(s1), "[Square] (3) 8/3 - 8")
        s1.update(y=4, id=5, a=5, b=1, size=7)
        self.assertEqual(str(s1), "[Square] (5) 8/4 - 7")

    def test_update_kwargs_errors(self):
        s1 = Square(10, 10, 10, 10)
        self.assertRaisesRegex(TypeError, "width must be an integer", s1.update, 3, (4, 5), x=5)
        self.assertRaisesRegex(ValueError, "width must be > 0", s1.update, y=3, width=-3, size=0)
        self.assertRaisesRegex(ValueError, "x must be >= 0", s1.update, y=6, id=34, x=-2)
        self.assertRaisesRegex(ValueError, "y must be >= 0", s1.update, 89, 2, 4, -10)
        self.assertRaisesRegex(TypeError, "x must be an integer", s1.update, x={5})
        self.assertRaisesRegex(TypeError, "y must be an integer", s1.update, size=8, y=None)

class test_dictionary(unittest.TestCase):
    """This class collects all functions related to testing dicts"""
    def test_dict_function(self):
        """This tests the functionality of to_dictionary function"""
        s1 = Square(1, 2)
        self.assertRaises(TypeError, s1.to_dictionary, 2)

    def test_dict_1(self):
        Base._Base__nb_objects = 0
        s1 = Square(1, 1)
        expected = {'x': 1, 'y': 0, 'id': 1, 'size': 1}
        self.assertDictEqual(expected, s1.to_dictionary())

    def test_dict_2(self):
        s1 = Square(10, 2, 9)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertFalse(s1 == s2)

    def test_dict_3(self):
        s1 = Square(5, 10, 2, 4)
        expected = {'x': 10, 'y': 2, 'id': 4, 'size': 5}
        self.assertDictEqual(expected, s1.to_dictionary())



if __name__ == '__main__':
    unittest.main()
