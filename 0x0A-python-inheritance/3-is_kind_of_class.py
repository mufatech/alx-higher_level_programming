#!/usr/bin/python3
"""
Defines a class and inherited class-checking function is_kind_of_class.

"""


def is_kind_of_class(obj, a_class):
    """if object is an instance of a class
    or a class that the class inherits from a_class, return True, otherwise False"""
    if isinstance(obj, a_class):
        return True
    return False
