#!/usr/bin/python3
"""mod documentation"""


def inherits_from(obj, a_class):
    """checks if object is an instance of class that inherits from specified class"""

    return isinstance(obj, a_class) and type(obj) != a_class
