#!/usr/bin/python3
"""

"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and
    returns the number of characters written:
    @filename: filename
    @text: text
    """
    with open(filename, 'w') as f:
        return(f.write(text))
