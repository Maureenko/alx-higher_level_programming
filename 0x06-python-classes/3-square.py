#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size(int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""

        return (self.__size * self.__size)
