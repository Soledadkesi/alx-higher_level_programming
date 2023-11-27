#!/usr/bin/python3
"""
Module 2-rectanglee
Contains class Rectaangle
with private attributte width and height
"""


class Rectangle:
    """
    Defines class recttangle with private attribute width and height

    Args:
        width (int): width
        height (int): height

    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initializee rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter returrns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter sets wwidth if int > 0 """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter returnss height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets heiight if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
