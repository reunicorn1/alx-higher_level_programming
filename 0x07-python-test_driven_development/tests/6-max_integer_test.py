#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittest for max_integer([..]"""

    def test_regular_list(self):
        """This function test regular lists with different values"""
        test_list = [2, 8, 5, 10, 1]
        self.assertEqual(max_integer(test_list), 10)

    def test_max_first(self):
        """This function tests a regular list with max at the beginning"""
        test_list = [12, 8, 5, 9, 1]
        self.assertEqual(max_integer(test_list), 12)
    def test_negative_list(self):
        """This function tests a list containing negative numbers"""
        test_list = [-5, -9, -3, -1, -7]
        self.assertEqual(max_integer(test_list), -1)

    def test_duplicate_num(self):
        """This function tests a list containing duplicate max values"""
        test_list = [3, 7, 5, 10, 7, 10, 8]
        self.assertEqual(max_integer(test_list), 10)

    def test_floats_num(self):
        """This function tests list containing floats and ints"""
        test_list = [-2, 0.0, 5, -10, 8.3, -4.5]
        self.assertEqual(max_integer(test_list), 8.3)

    def test_strings_list(self):
        """This function tests a string as a list"""
        test_list = "reem osama"
        self.assertEqual(max_integer(test_list), 's')

    def test_list_string(self):
        """This function tests a list of string"""
        test_list = ["art", "tech", "medicine", "love"]
        self.assertEqual(max_integer(test_list), "tech")

    def test_empty_string(self):
        """This function tests a string which is empty"""
        self.assertIsNone(max_integer(""))

    def test_empty_list(self):
        """This Function tests if the function returns None in empty list"""
        test_list = []
        self.assertIsNone(max_integer(test_list))

    def test_one_element(self):
        """This function tests a list with one element"""
        test_list = [42]
        self.assertEqual(max_integer(test_list), 42)

    def test_large_list(self):
        """This function tests a large list"""
        test_list = list(range(1, 1000001))
        self.assertEqual(max_integer(test_list), 1000000)

    def test_zeros_list(self):
        """This function test a list of al zeros"""
        test_list = [0, 0, 0, 0, 0]
        self.assertEqual(max_integer(test_list), 0)


if __name__ == '__main__':
    unittest.main()
