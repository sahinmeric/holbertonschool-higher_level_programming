#!/usr/bin/python3
"""initialization"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """that prints the list, but sorted"""
        for elem in self:
            if elem is not isinstance(self, int):
                raise TypeError("list elements must be integer")
        print(sorted(self))
