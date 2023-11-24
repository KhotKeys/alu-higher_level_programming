#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits BaseGeometry'''

    def __init__(self, width, height):
        '''A function that creates a rectangle '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        '''Function to return the area of the rectangle'''
        return self.__height * self.__width

    def __str__(self):
        '''Return the print() and str() representation of a Rectangle '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


if __name__ == "__main__":
    # Case: print(dir(Rectangle))
    print(dir(Rectangle))

    # Case: r = Rectangle(1, 4) print(r.area())
    r = Rectangle(1, 4)
    print(r.area())

    # Case: r = Rectangle(1411, 781) print(r.area())
    r = Rectangle(1411, 781)
    print(r.area())

    # Case: r = Rectangle(5, 5) print(r.area())
    r = Rectangle(5, 5)
    print(r.area())

    # Case: r = Rectangle(1411, 781) print®
    try:
        r = Rectangle(1411, 781)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Case: r = Rectangle(1, 4) print®
    try:
        r = Rectangle(1, 4)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Case: r = Rectangle(5, 5) print®
    try:
        r = Rectangle(5, 5)
        print(r)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    # Case: r = Rectangle() r = Rectangle(1) r = Rectangle(1, [12, 52]) r = Rectangle(4, 5) r = Rectangle(4, 5)
    try:
        r = Rectangle()
        r = Rectangle(1)
        r = Rectangle(1, [12, 52])
        r = Rectangle(4, 5)
        r = Rectangle(4, 5)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

