#!/usr/bin/python3
"""
Module for square
"""


class Square(Rectangle):
    """
    The Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string to use in override
        """
        return "[Square] ({})) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )
