#!/usr/bin/python3
'''Class Square that inherits from Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits Rectangle'''

    def __init__(self, size):
        '''A function that creates a square '''
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        '''Return the print() and str() representation of a Square '''
        return "[Square] {}/{}".format(self.width, self.height)


if __name__ == "__main__":
    # Example Usage
    s = Square(5)
    print(s)
    print(s.area())
