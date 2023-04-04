#!/usr/bin/python3

""" 
Defines a class Rectangle
"""

class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the rectangle"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    
    def __init__(self, lenght=0, breath=0):
        """Initializes area and perimeter of rectangle"""
        self.lenght = lenght
        self.breath = breath

    def area(self):
        """returns the area of the rectangle"""
        return self.__lenght * self.__breath

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__lenght == 0 or self.__breath == 0:
            return 0
        return (self.__lenght * 2) + (self.__breath *2)



