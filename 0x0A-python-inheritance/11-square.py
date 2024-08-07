#!/usr/bin/python3
"""module dcumentation"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits its attributes from class Rectangle"""

    def __init__(self, size):
        """Initialies the size of the square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""

        return self.__size * self.__size

    def __str__(self):
        """string representation"""
        return "[Square] {}/{}".format(self.__size, self.__size)
