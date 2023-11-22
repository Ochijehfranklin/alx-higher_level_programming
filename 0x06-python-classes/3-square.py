#!/usr/bin/python3
""" a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """class Square"""
    def __init__(self, size=0):
        """initialize a class for Square

        Attribute:
            size (int): Size of a new quare
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return area of this defined square"""
        return (self.__size ** 2)
