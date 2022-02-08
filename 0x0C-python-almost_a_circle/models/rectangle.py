#!/usr/bin/python3
"""
this module contains a rectangle class that inherited grom base class
"""


from sys import argv
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for Rectangle class"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        if height > 0:
            self.__height = height

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        if width > 0:
            self.__width = width

        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if y < 0:
            raise ValueError("y must be >= 0")
        else:
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
        if isinstance(value, int):
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y"""
        if isinstance(value, int):
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ calculates and returns the area of rectangle"""
        return int(self.__width) * int(self.__height)

    def display(self,):
        """ prints rectangle with #"""
        for m in range(self.__y):
            print("")
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Returns the description of the Rectangle instance """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ update method"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y, 'id': self.id}
