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
        """ Constructor for Square class"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Returns the description of the Square instance"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
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
        """ update method"""
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self._Rectangle__x = args[2]
                if i == 3:
                    self._Rectangle__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self._Rectangle__x = value
                if key == 'y':
                    self._Rectangle__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'size': self.size, 'x': self._Rectangle__x,
                'y': self._Rectangle__y, 'id': self.id}
