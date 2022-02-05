#!/usr/bin/python3
"""
this module contains a class named square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ getter for size"""
        return self.__size

    @size.setter
    def size(self, size):
        """ setter for size"""
        if isinstance(size, int):
            if size > 0:
                self.width = size
                self.height = size
            else:
                raise ValueError("size must be > 0")
        else:
            raise TypeError("width must be an integer")
