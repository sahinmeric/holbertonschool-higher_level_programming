#!/usr/bin/python3
"""
This module includes a function that
reads a file and prints context to stdout.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:
    @filename: file that will be read
    """
    with open(filename) as f:
        print(f.read(), end="")
        f.close()
