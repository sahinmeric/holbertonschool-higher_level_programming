#!/usr/bin/python3
""" module has a function that checks
whether given object is exactly
an instance of specified class same class or not
@obj: object
@a_class: class
"""


def is_same_class(obj, a_class):
    """returns True if the objects belongs to same class,
    else False"""
    return(type(obj) is a_class)
