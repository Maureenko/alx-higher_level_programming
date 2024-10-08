#!/usr/bin/python3
"""function that adds integers"""


def add_integer(a, b=98):
    """adds two integers
    Args:
    a(int/float)
    b(int/float)

    Return:
    int: values of a + b
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
