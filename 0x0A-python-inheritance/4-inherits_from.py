#!/usr/bin/python3
"""mod documentation"""


def inherits_from(obj, a_class):
    """checkif object is instance of class that inherits from specific class"""

    return isinstance(obj, a_class) and type(obj) != a_class
