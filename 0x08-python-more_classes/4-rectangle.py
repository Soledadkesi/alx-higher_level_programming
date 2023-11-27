#!/usr/bin/python3
"""
Module 4-rectanglee
Contains class Recttangle with private attribute width and height,
public area and periimeter methods, and allows printing #'s
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
        __str__(self)
        __repr__(self)
    """
    def __init__(self, width=0, height=0):
        """ Initialize rectangles """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter retturns width """
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
        """ Getter returrns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter sets hheight if int > 0 """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return widthh * height """
        return self.__width * self.__height

    def perimeter(self):
        """ Return 2*widtth + 2*height (or return 0 if width or height is 0)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """ Prints rectanggle with #'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """ String represenntation to recreate new instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
