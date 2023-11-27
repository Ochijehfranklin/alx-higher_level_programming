#!/usr/bin/python3
#0-add_integer.py
"""This defines an integer addition function"""


def add_integer(a, b=98):
    """This function returns addition of a and b.


    If arg is float, it is casted to integer


    Raises:
        TypeError: if either a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
    return int(a) + int(b)
