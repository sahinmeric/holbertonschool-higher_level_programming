#!/usr/bin/python3
"""
this module has a function that
appends given text to an existing text file
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    @filename: file
    @text: text
    """
    with open(filename, 'a') as f:
        return(f.write(text))
