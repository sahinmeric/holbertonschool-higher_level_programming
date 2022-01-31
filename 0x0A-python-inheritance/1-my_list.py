#!/usr/bin/python3
"""initialization"""


from xml.dom.minidom import Element


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """that prints the list, but sorted"""
        for item in self:
            if not isinstance(item, int):
                raise TypeError("list items must be integer")
        print(sorted(self))
