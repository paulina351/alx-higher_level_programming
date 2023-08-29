#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """
    Private instance attribute: size
    """

    def __init__(self, size=0):
        """
        Private instance attribute: size
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method: def area(self):
        """
        self.__size = size

        @property
        def size(self):

            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size

        def area(self):
            return (self.__size ** 2)
