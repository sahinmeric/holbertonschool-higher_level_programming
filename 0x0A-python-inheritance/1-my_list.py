#!/usr/bin/python3
"""initialization"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """that prints the list, but sorted"""
        print(sorted(self))
