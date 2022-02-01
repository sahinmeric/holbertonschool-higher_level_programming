#!/usr/bin/python3
"""
initialize
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    @filename: file
    """
    with open(filename, 'w') as f:
        f.write(json.loads(json.dumps(filename)))
