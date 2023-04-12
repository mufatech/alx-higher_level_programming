#!/usr/bin/python3
"""
Defines the class BaseGeometry
"""


class BaseGeometry:
    """Represent Base Geometry"""

    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
