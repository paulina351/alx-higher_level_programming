#!/usr/bin/python3
"""A function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the
specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False

    Args:
        obj (any): to check the object
        a_class (type): the class to connect the type
    Return:
        if obj is inherited - True
        Otherwise - False
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
