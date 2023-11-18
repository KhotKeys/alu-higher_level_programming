#!/src/bin/python3
"""Rectangle module"""

class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor:
        Args:
        size: length and width of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < o:
            raise ValueError("Width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if  not isinstance(value, int):
            raise TypeError("height is an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

