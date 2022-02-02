#!/usr/bin/python3
"""initialize"""


class Student:
    """creates class student"""

    def __init__(self, first_name, last_name, age):
        """initializate atrributes
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """ retrieves a dictionary """
        if attr is None:
            return self.__dict__
        ret_attr = {}
        for key, val in self.__dict__.items():
            if key in attr:
                ret_attr[key] = val
        return ret_attr
