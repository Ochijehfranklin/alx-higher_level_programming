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
        if type(value) != int:
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
        if type(value) != int:
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
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
