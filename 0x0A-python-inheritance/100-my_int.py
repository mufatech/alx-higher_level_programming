#!/usr/bin/python3

"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """rebel version of an integer operator == and !="""

    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, value):
        """what was != what is now =="""
        return int(self) != value

    def __ne__(self, value):
        """what was == what is now !="""
        return int(self) == value
