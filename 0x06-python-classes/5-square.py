#!/usr/bin/python3
"""A class Square that defines a square based on 4-square.py."""


class Square:
    """Method definitions for class Square."""

    def __init__(self, size):
        """Initialize a new square.

        Attribute:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
