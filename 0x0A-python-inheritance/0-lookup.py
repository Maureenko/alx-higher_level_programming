#!/usr/bin/python3
"""" Provides function to list all arguments and methods of an object."""

def lookup(obj):
    """Returns the list of available attributes and methods of an object.
    Args:
        obj = object to be assessed.
    """
    return dir(obj)

