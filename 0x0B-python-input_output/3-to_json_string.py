#!/usr/bin/python3
"""
Initialize
"""


import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string):
    @my_obj: object
    """
    return(json.dumps(my_obj))
