#!/usr/bin/python3

"""Rectangle module"""

class Rectangle:
    """Define a rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor:
        Args:
        width: width of the rectangle
        height: height of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

# Test Cases
# Test Case 1
try:
    r = Rectangle(-1, 5)
except ValueError as e:
    print(f"[Expected]\n{e}")
except TypeError as e:
    print(f"[Expected]\n{e}")

# Test Case 2
try:
    r = Rectangle(10, "abc")
except ValueError as e:
    print(f"[Expected]\n{e}")
except TypeError as e:
    print(f"[Expected]\n{e}")

# Test Case 3
try:
    r = Rectangle(-3, -4)
except ValueError as e:
    print(f"[Expected]\n{e}")
except TypeError as e:
    print(f"[Expected]\n{e}")

# Add more test cases as needed
