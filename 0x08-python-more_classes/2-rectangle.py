#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """the Rectangle class"""
    def __init__(self, width=0, height=0):
        """instances of width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) is not int:
            raise TypeError("width must be a integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) is not int:
            raise TypeError("height must be a integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area"""
        return self.height * self.width

    def perimeter(self):
        """return perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.width + self.height) * 2