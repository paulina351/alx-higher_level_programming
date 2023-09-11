#!/usr/bin/python3
"""a function that returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj (any): the object to be checked
        a_class (type): the class to match the type of object to.
    Returns:
        if onj is exactly an instance of a_class - True.
        otherwise - False
    """
    return type(obj) is a_class
