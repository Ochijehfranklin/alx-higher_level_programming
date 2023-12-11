#!/usr/bin/python3
# models/rectangle.py
"""This is for the rectangle"""
from base import Base


class Rectangle(Base):
    """This defines the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class Rectangle"""

        super().__init__(id)
        """takes identitity from the base class"""

        """
        Args:
            width (int): defines width of rectangle
            height (int): defines height of rectangle
            x (int): The x-axis of rectangle
            y (int): The y-axis of rectangle
            id (int): identity of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """Height Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X-axis Getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """X-axis Setter."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y-axis Getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y-axis Setter."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Update are of the Rectangle."""
        return self.width * self.height
    
    def display(self):
        """
        function to print rectangle size
        """
        for x in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
