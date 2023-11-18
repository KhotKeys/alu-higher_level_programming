#!/usr/bin/python3
"""Define a rectangle"""

'''
file name = 3-rectangle.py
created = 18-11-2023
Author = Gabriel Khot Keys Goodwin Pawuoi
size = large
project = 0x08-python-more_classes
status = Not Submitted
'''

class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        """
        initialize a new rectangle.

        Args:
        width(int): The width of the new rectangle
        height(int): The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value,int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
    def __str__(self):
        """Return the printable of the representation of the rectangle.
        Represent the rectangle with the #charater"""
        if width == 0 or height == 0:
            return ("")
        
        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        """ Return the representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

