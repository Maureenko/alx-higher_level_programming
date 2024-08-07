#!/usr/bin/python3
"""mod documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the width and length of the rectangle."""

        self.integer_validator("width", width)
        self.integer_validator("length", height)
        self.__width = width
        self.__length = height
