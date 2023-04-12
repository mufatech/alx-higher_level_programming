#!/usr/bin/python3
"""
Defines a subclass or MyList class
"""


class MyList(list):
    """This is a subclass of the list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
