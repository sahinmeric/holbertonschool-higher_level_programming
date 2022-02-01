#!/usr/bin/python3
"""
initialize
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation:
    @my_obj: object
    @filename: file
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
