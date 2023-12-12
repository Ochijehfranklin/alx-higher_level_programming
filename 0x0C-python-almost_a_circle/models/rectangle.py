#!/usr/bin/python3
# models/rectangle.py
"""This is for the rectangle"""
from models.base import Base


class Rectangle(Base):
    """This defines the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the class Rectangle

        Args:
            width (int): defines width of rectangle
            height (int): defines height of rectangle
            x (int): The x-axis of rectangle
            y (int): The y-axis of rectangle
            id (int): identity of rectangle.
        Raises:
            TypeError: If either of width or height is not an int
            ValueError: If either of width or height <= 0
            TypeError: If either of x or y is not an int
            ValueError: If either of x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width Setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

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
        """Print the Rectangle using the `#` character."""
        for w in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )

        def update(self, *args, **kwargs):
            """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st arg = id attribute
                - 2nd arg = width attribute
                - 3rd arg = height attribute
                - 4th arg = x attribute
                - 5th arg = y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                elif k == 1:
                    self.width = v
                elif k == 2:
                    self.height = v
                elif k == 3:
                    self.x = v
                else:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
