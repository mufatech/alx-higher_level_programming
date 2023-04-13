#!/usr/bin/python3
"""
Defines a fucntion that returns dict description with simple data "class_to_json" function
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object"""
    return obj.__dict__
