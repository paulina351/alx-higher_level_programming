#!/usr/bin/python3
"""Writes and defines a class Student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Intialization

        Args:
            first_name (str): the student first name
            last_name (str): the student last name
            age (int): the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ that retrieves a dictionary representation of a Student instance

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved

        Args:
            attrs (list): the attributes to represent
        """
        elemt = {}
        if attrs is None:
            return self.__dict__
        for t in attrs:
            if hasattr(self, t):
                elemt[t] = getattr(self, t)
        return elemt
