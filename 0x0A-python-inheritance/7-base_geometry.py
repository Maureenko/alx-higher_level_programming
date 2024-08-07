#!/usr/bin/python3
"""mod documentation"""


class BaseGeometry():
    """class BaseGeometry based on the selected class"""

    def area(self):
        """function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation function"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
