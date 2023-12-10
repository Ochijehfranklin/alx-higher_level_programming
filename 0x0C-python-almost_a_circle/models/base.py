#!/usr/bin/python3
"""This would be the base task"""


class Base:
    """Defines the class base


    Attributes:
        __nb__objects__ (int): number of bases created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialzes the base class

        Args:
            id (int): identity of base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

