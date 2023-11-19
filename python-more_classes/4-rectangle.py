#!/usr/bin/python3

    """
    Defines a rectangle with width and height attributes.
    """

    '''
    file name = 4-rectangle.py
    created = 19-11-2023
    Author = Gabriel Khot Garang Pawuoi
    size = undefine
    project = 0x08-python-more_classes
    status = not submitted
    '''
    class Rectangle:
         """
    # Write a class Rectangle that defines a rectangle by:
    # ....(based on 8-rectangle.py)
    # Instantiation with optional width and height:
    # ....def __init__(self, width=0, height=0):
    # VARIABLE(" "):
    # Rectangle_Area/Perimeter(int): String representation
    # Return: Always 0, (Success).
    """

    """ 'class rectangle' defines the class is like a blueprint or template...
    for creating objects...
    while the 'pass' is used as a placeholder when you don't want to add...
    any code in a block and this is just a sample of a 2D Polygon with a ...
    ...4-Perpendicular Sides."""
    """ The '__str__(0' method provides a string representation of the...
    rectangle using the 'print_symbol', and the '__repr__()' method...
    returns a string representation that can be used to....
    recreate a new instance using 'eval()"""
    """ rectangle with private instance attributes width and height """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The value to set as the width.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The value to set as the height.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height) if self.__width != 0 and self.__height != 0 else 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        result = ""
        for i in range(self.__height):
            result += "#" * self.__width + "\n"
        return result.rstrip()

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation using eval().

        Returns:
            str: The string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
