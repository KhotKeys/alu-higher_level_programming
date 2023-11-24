#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry '''

    def __init__(self, width, height):
        '''Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
