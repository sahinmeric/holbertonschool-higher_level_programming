#!/usr/bin/python3
""" A python script defines a class named Square"""


class Square:
    """A class that defines square"""

    def __init__(self, size=0):
        if type(size) != int:
            print("size must be an integer")
            raise TypeError
        elif size < 0:
            print("size must be >= 0")
            raise ValueError
        else:
            self.__size = size
