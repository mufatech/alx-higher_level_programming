#!/usr/bin/python3
"""
This module defines a class-checking function is_same_class.
"""


def is_same_class(obj, a_class):
    """Checks if object is an instance of a class,
    return true if obj is an instance of a class a_class, otherwise false"""
    return (type(obj) == a_class)
