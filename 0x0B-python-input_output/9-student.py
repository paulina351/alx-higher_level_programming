#!/usr/bin/python3
"""Writes and defines a class student"""


class Student:
    """Defines a class Student"""

    def __init__(self, first_name, last_name, age):
        """initialization

        Args:
            first_name (str): the students first name
            last_name (str): the student last name
            age (int): the student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__
