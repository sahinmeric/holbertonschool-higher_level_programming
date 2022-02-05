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

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
