#!/usr/bin/python3
"""
this module contains base class
"""
from os import path
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for Base class"""
        if id is not None:
            if type(id) is int:
                self.id = id
            else:
                raise TypeError("id must be an integer")
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries:"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries, default=lambda o: o.__dict__)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file:"""
        fileName = cls.__name__ + ".json"
        dict_ = []
        if list_objs is not None:
            dict_ = [a.to_dictionary() for a in list_objs]
        jsonFile = open(fileName, 'w')
        jsonFile.write(cls.to_json_string(dict_))
        jsonFile.close()

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        pyt_obj = json.loads(json_string)
        if pyt_obj is None or pyt_obj == []:
            return []
        return pyt_obj

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        if cls.__name__ == 'Square':
            tmp = cls(1)
        cls.update(tmp, **dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        fileName = cls.__name__ + ".json"
        if path.isfile(fileName):
            with open(fileName, 'r') as f:
                myList = cls.from_json_string(f.read())
            return [cls.create(**a) for a in myList]
        return []
