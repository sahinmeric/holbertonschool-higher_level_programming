#!/usr/bin/python3
""" module has a function that checks
wheter given objects are from same class or not
@obj: object
@a_class: class
"""


def is_same_class(obj, a_class):
    """returns True if the objects belongs to same class,
    else False"""
    return(type(obj, a_class))
