#!/usr/bin/python3
"""module documentation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialies the size of the square"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calculates the area of the square"""

        return self.__size * self.__size

    def __str__(self):
        """string representation"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
