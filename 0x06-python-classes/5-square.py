#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """Private instance attribute: size"""

    def __init__(self, size=0):
        """
        Private instance attribute: size:
        Instantiation with optional size: def __init__(self, size=0):
        Public instance method: def area(self):
        Public instance method: def my_print(self):
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
