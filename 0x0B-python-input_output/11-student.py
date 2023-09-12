#!/usr/bin/python3
"""Write and defines a class Student"""


class Student:
    """Defines a class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representation of a student

        If attrs is a list of strings, only attributes name
        contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved

        Args:
            attrs (list): represents the attributes
        """
        elemt = {}
        if attrs is None:
            return self.__dict__
        for t in attrs:
            if hasattr(self, t):
                elemt[t] = getattr(self, t)
        return elemt

    def reload_from_json(self, json):
        """Replaces all attributes of student

        Args:
            json (dict): the key/value pairs to replace
        """
        for ky, vl in json.items():
            if hasattr(self, ky):
                setattr(self, ky, vl)
