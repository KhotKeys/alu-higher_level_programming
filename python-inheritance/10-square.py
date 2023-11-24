#!/usr/bin/python3
'''Class Square that inherits from Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits Rectangle'''

    def __init__(self, size):
        '''A function that creates a square '''
        self.integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        '''Function to return the area of the square'''
        return self.width * self.height
