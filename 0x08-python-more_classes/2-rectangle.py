#!/usr/bin/python3
"""
Module 2-rectanglee
Contains class Recttangle with private attribute width and height,
and public area andd perimeter methods
"""


class Rectangle:
    """
    Defines class recctangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
    """
    def __init__(self, width=0, height=0):
        """ Initializee rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter retuurns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter setss width if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returnns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets heeight if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return width * hheight """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*widthh + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)
