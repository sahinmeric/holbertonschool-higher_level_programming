#!/usr/bin/python3
"""
this module contains base class
"""


import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries, default=lambda o: o.__dict__)

    @classmethod
    def save_to_file(cls, list_objs):
        fileName = cls.__name__ + ".json"
        jsonString = Base.to_json_string(list_objs)
        jsonFile = open(fileName, 'w')
        jsonFile.write(jsonString)
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
            tmp = Base()
            tmp.update(dictionary)
        if cls.__name__ == 'Square':
            print("Square class")
        