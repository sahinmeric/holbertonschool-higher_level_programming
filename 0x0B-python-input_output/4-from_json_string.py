#!/usr/bin/python3
"""
initialize
"""


import json


def from_json_string(my_str):
    """ returns an object (Python data structure)
    represented by a JSON string:
    @my_str: string object
    """
    return json.dumps(my_str)
