#!/usr/bin/python3
"""Define the square"""

'''
file name = 101-square.py
created = 19-11-2023
Author = Gabriel Khot Garang Pawuoi
size = undefine
project = Python - Classes and Objects
status = Not submitted
'''
class Square:
    """Define a squre"""
    def __int__(self, size=0, position=0(0,0)):
        """initialize a square with the given size and function."""

        self.size = size
        self.position = position

    @property
    def size(self):
        """getter allow to decorated and retrieve as a method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for the size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position."""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' character."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
