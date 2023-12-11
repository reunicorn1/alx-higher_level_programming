#!/usr/bin/python3
"""Unittest for the class Rectangle
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class test_instantation(unittest.TestCase):
    """Define unittest for the class Rectangle"""
    def test_1(self):
        """This function tests the basic usage of Rectangle class"""
        rect = Rectangle(10, 5, 2, 3)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_2(self):
        """This function tests the default values of Rectangle class"""
        rect1 = Rectangle(1, 1)
        self.assertEqual(rect1.height, 1)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)

    def test_3(self):
        """This function creates a rectangle with non-zero x and y values"""
        rect2 = Rectangle(5, 3, 2, 4)
        self.assertEqual(rect2.width, 5)
        self.assertEqual(rect2.height, 3)
        self.assertEqual(rect2.x, 2)
        self.assertEqual(rect2.y, 4)

    def test_4(self):
        """Thie function tests setters for width, height, x and y"""
        rect4 = Rectangle(3, 4, 1, 2)
        rect4.width = 7
        rect4.height = 9
        rect4.x = 5
        rect4.y = 6
        self.assertEqual(rect4.width, 7)
        self.assertEqual(rect4.height, 9)
        self.assertEqual(rect4.x, 5)
        self.assertEqual(rect4.y, 6)

class test_error(unittest.TestCase):
    """This class tests the functionality of setter, getter as well as having no args"""
    def test_negative_width(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, -2, 0)

    def test_zero_height(self):
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 2, 0)

    def test_negative_x(self):
        self.assertRaisesRegex(ValueError, "x must be >= 0", Rectangle, 2, 3, -3, 4)

    def test_negative_y(self):
        self.assertRaisesRegex(ValueError, "y must be >= 0", Rectangle, 2, 3, 4, -5)
    
    def test_not_int_width(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, "2", 3)
    
    def test_not_int_height(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 2, "3")
    
    def test_not_int_x(self):
        self.assertRaisesRegex(TypeError, "x must be an integer", Rectangle, 2, 3, "4", 5)
    
    def test_not_int_y(self):
        self.assertRaisesRegex(TypeError, "y must be an integer", Rectangle, 2, 3, 4, "5")

    def test_width_inf(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, float('inf'), 3)

    def test_width_nan(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, float('nan'), 3)

    def test_width_zero(self):
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, 0, 2)

    def test_width_none(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, None, 3)

    def test_width_float(self):
        self.assertRaisesRegex(TypeError, "width must be an integer", Rectangle, 3.4, 3)

    def test_height_inf(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 2, float('inf'))

    def test_height_nan(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 2, float('nan'))

    def test_height_negative(self):
        self.assertRaisesRegex(ValueError, "height must be > 0", Rectangle, 2, -4)

    def test_height_none(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 2, None)

    def test_height_float(self):
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 2, 4.6)

    def test_subclass(self):
        """This function tests that Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_less_args(self):
        """This function tests when function is given less positional args"""
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 3)


class test_area(unittest.TestCase):
    def test_area_1(self):
        """This function tests the area public method of Rectangle"""
        rect1 = Rectangle(2, 3)
        self.assertEqual(rect1.area(), 6)

    def test_area_2(self):
        rect2 = Rectangle(5, 5)
        self.assertEqual(rect2.area(), 25)
        
    def test_area_3(self):
        rect3 = Rectangle(10, 2)
        self.assertEqual(rect3.area(), 20)
        
    def test_area_4(self):
        rect4 = Rectangle(3, 5)
        self.assertEqual(rect4.area(), 15)
        
    def test_area_5(self):
        rect5 = Rectangle(4, 6)
        self.assertEqual(rect5.area(), 24)
        
    def test_area_6(self):
        rect6 = Rectangle(8, 7)
        self.assertEqual(rect6.area(), 56)

    def test_area_large(self):
        """This function tests large width and height values"""
        rect1 = Rectangle(100, 1000)
        self.assertEqual(rect1.area(), 100000)

class test_display(unittest.TestCase):
    """This class prints the display of the rectangle"""
    def test_display_1(self):
        """This function prints the display of the rectangle"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 3)
            r1.display()
            output = "##\n##\n##\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_display_2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(10, 3)
            r2.display()
            output = "##########\n##########\n##########\n"
            self.assertEqual(fake_out.getvalue(), output)
        
    def test_display_3(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3 = Rectangle(1, 1)
            r3.display()
            output = "#\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_display_coordinates_1(self):
        """This function prints the display with coordinates"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(5, 3, 2, 1)
            r1.display()
            output = "\n  #####\n  #####\n  #####\n"
            self.assertEqual(fake_out.getvalue(), output)
        
    def test_display_coordinates_2(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(3, 4, 1, 2)
            r2.display()
            output = "\n\n ###\n ###\n ###\n ###\n"
            self.assertEqual(fake_out.getvalue(), output)
        
    def test_display_coordinates_3(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3 = Rectangle(3, 2, 1, 0)
            r3.display()
            output = " ###\n ###\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_print(self):
        """This function tests the string representation of instances"""
        Base._Base__nb_objects = 0
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(1, 1)
            print(r1)
            output = "[Rectangle] (1) 0/0 - 1/1\n"
            self.assertEqual(fake_out.getvalue(), output)

    def test_str_1(self):
        r2 = Rectangle(5, 3, 2, 4)
        self.assertEqual(str(r2), "[Rectangle] (2) 2/4 - 5/3")

    def test_str_2(self):
        r3 = Rectangle(3, 6, id=10)
        self.assertEqual(str(r3), "[Rectangle] (10) 0/0 - 3/6")
    
    def test_str_3(self):
        r4 = Rectangle(5, 5)
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 5/5")

class test_display(unittest.TestCase):
    """This class contains all tests related to the display function"""
    def test_update(self):
        """This function tests the update function"""
        rect1 = Rectangle(5, 10, 2, 3, 1)
        rect1.update()
        self.assertEqual(str(rect1), "[Rectangle] (1) 2/3 - 5/10")
        rect1.update(100)
        self.assertEqual(str(rect1), "[Rectangle] (100) 2/3 - 5/10")
        rect1.update(100, 4)
        self.assertEqual(str(rect1), "[Rectangle] (100) 2/3 - 4/10")
        rect1.update(100, 5, 8)
        self.assertEqual(str(rect1), "[Rectangle] (100) 2/3 - 5/8")
        rect1.update(100, 5, 8, 4)
        self.assertEqual(str(rect1), "[Rectangle] (100) 4/3 - 5/8")
        rect1.update(100, 5, 8, 4, 1)
        self.assertEqual(str(rect1), "[Rectangle] (100) 4/1 - 5/8")

    def test_update_setter(self):
        """This function tests the functionality of setters and getters in update"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        self.assertRaisesRegex(TypeError, "width must be an integer", r1.update, 89, "2")
        self.assertRaisesRegex(ValueError, "height must be > 0", r1.update, 89, 2, 0)
        self.assertRaisesRegex(ValueError, "width must be > 0", r1.update, 89, -3)
        self.assertRaisesRegex(TypeError, "height must be an integer", r1.update, 89, 2, "3")
        self.assertRaisesRegex(ValueError, "height must be > 0", r1.update, 89, 2, 0)
        self.assertRaisesRegex(ValueError, "x must be >= 0", r1.update, 89, 2, 4, -2)
        self.assertRaisesRegex(TypeError, "x must be an integer", r1.update, 89, 2, 4, "2")
        self.assertRaisesRegex(ValueError, "y must be >= 0", r1.update, 89, 2, 4, 3, -10)
        self.assertRaisesRegex(TypeError, "y must be an integer", r1.update, 89, 2, 4, 3, "7")

    def test_update_kwargs_1(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(8, 12, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 8/12")
        r1.update(id=100, width=5, height=5)
        self.assertEqual(str(r1), "[Rectangle] (100) 2/3 - 5/5")
        r1.update(x=3, height=8, id=42)
        self.assertEqual(str(r1), "[Rectangle] (42) 3/3 - 5/8")

    def test_update_kwargs_2(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(8, 8, 3, 3)
        self.assertEqual(str(r1), "[Rectangle] (1) 3/3 - 8/8")
        r1.update(nonexistant=100, random=5, wrong=5)
        self.assertEqual(str(r1), "[Rectangle] (1) 3/3 - 8/8")
        r1.update(34, 5, 1, x=5)
        self.assertEqual(str(r1), "[Rectangle] (34) 3/3 - 5/1")
        r1.update(y=5)
        self.assertEqual(str(r1), "[Rectangle] (34) 3/5 - 5/1")

    def test_update_kwargs_3(self):
        r1 = Rectangle(8, 8, 3, 3)
        self.assertEqual(str(r1), "[Rectangle] (2) 3/3 - 8/8")
        r1.update(y=4, id=5, word=5, width=7)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/4 - 7/8")

    def test_update_kwargs_4(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        self.assertRaisesRegex(TypeError, "width must be an integer", r1.update, 3, (4, 5), x=5)
        self.assertRaisesRegex(TypeError, "height must be an integer", r1.update, height=[6])
        self.assertRaisesRegex(ValueError, "height must be > 0", r1.update, height=-5)
        self.assertRaisesRegex(ValueError, "width must be > 0", r1.update, y=3, width=-3)
        self.assertRaisesRegex(ValueError, "x must be >= 0", r1.update, y=6, id=34, x=-2)
        self.assertRaisesRegex(ValueError, "y must be >= 0", r1.update, 89, 2, 4, 3, -10)
        self.assertRaisesRegex(TypeError, "x must be an integer", r1.update, x={5})
        self.assertRaisesRegex(TypeError, "y must be an integer", r1.update, width=8, y=None)

class test_dictionary(unittest.TestCase):
    """This class collects all functions related to testing dicts"""
    def test_dict_function(self):
        """This tests the functionality of to_dictionary function"""
        r1 = Rectangle(1, 2)
        self.assertRaises(TypeError, r1.to_dictionary, 2)
    
    def test_dict_1(self):
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1)
        expected = {'x': 0, 'y': 0, 'id': 1, 'height': 1, 'width': 1}
        self.assertDictEqual(expected, r1.to_dictionary())

    def test_dict_2(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertFalse(r1 == r2)

    def test_dict_3(self):
        r1 = Rectangle(5, 10, 2, 4, 1)
        expected = {'x': 2, 'y': 4, 'id': 1, 'height': 10, 'width': 5}
        self.assertDictEqual(expected, r1.to_dictionary())


if __name__ == '__main__':
    unittest.main()
