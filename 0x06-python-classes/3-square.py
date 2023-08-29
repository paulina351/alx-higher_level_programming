#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """
    Private instance attribute: size
    Public instance method: def area(self):
    """

    def __init__(self, size=0):
        """
        Private instance attribute: size
        Public instance method: def area(self):
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):

        return (self.__size ** 2)
