#!/usr/bin/python3
"""defines a class rectangle"""


class Rectangle:
    """Class rectangle with attributes."""

    def __init__(self, width=0, height=0):
        """initialization of attributes width and height"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the height"""

        return self.__width

    @height.setter
    def height(self, value):
        """setter for the height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
