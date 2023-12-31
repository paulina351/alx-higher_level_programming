#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)"""


class Rectangle:
    """rectangular class"""

    def __init__(self, width=0, height=0):
        """Intializing a new rectangle.

        Args:
            width(int): The width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getting the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the width property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height property"""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
