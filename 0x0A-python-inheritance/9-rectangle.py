#!/usr/bin/python3
"""module documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the length and width of a rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("length", height)

        self.__width = width
        self.__height = height

    def area(self):
        """calculates the area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
