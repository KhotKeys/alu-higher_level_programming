#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''


class Rectangle:
    '''Rectangle class that inherits BaseGeometry'''

    def __init__(self, width=0, height=0):
        '''A function that creates a rectangle '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Function to return the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Return the print() and str() representation of a Rectangle '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def integer_validator(self, name, value):
        '''Validate the input'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    # Test cases
    print(dir(Rectangle))

    r = Rectangle(1, 4)
    print(r.area())

    r = Rectangle(1411, 781)
    print(r.area())

    r = Rectangle(5, 5)
    print(r.area())

    try:
        r = Rectangle(1411, 781)
        print(r.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(1, 4)
        print(r.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(5, 5)
        print(r.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle()
        r = Rectangle(1)
        r = Rectangle(1, [12, 52])
        r = Rectangle(4, 5)
        r = Rectangle(4, 5)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
