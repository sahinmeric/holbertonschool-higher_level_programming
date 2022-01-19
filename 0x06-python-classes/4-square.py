#!/usr/bin/python3
""" This module contains a class that defines a square
In the Square class we initialize each object by the __init_ method"""


class Square:
    """A class that defines square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    def area(self):
        """ calculate the area of given value"""
        return self.size ** 2
