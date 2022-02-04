#!/usr/bin/python3
"""
this module contains a rectangle class that inherited grom base class
"""


from multiprocessing.sharedctypes import Value
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if isinstance(value, int):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height"""
        if isinstance(value, int):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x"""
        if value >= 0:
            self.__x = value
        else:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y"""
        if value >= 0:
            self.__y = value
        else:
            raise ValueError("y must be >= 0")

    def area(self):
        """ calculates and returns the area of rectangle"""
        return int(self.__width) * int(self.__height)
