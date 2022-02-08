#!/usr/bin/python3
"""
unit tests for base class and its methods
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for checking functionality of Base class"""
    def test_too_many_args(self):
        """test too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_non_int_arg(self):
        """test with non integer argument"""
        with self.assertRaises(TypeError):
            b1 = Base('a')

    def test_non_arg(self):
        """test with non argument"""
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_int_arg(self):
        """test with int argument"""
        b3 = Base(99)
        self.assertEqual(b3.id, 99)

    def test_set_id_after(self):
        """test an instance by setting with new id """
        b4 = Base()
        b4.id = 89
        self.assertEqual(b4.id, 89)


class TestBaseDocs(unittest.TestCase):
    """ test class for testing Base class documentation"""
    if __name__ == '__main__':
        unittest.main()
