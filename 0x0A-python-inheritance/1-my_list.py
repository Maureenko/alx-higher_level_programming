#!/usr/bin/python3
"""" Defines a class MyList that inherits from list."""


class MyList(list):
    """Inherits from list class"""

    def print_sorted(self):
        """print a list in ascending order."""
        listOb = sorted(self)
        print(listOb)
