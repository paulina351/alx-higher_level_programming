#!/usr/bin/python3
"""a function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited
from, the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ a function that returns True if the object is an instance
    of, or if the object is an instance of a class that inherited
    from, the specified class ; otherwise False.

    Args:
        obj (any): The object to check if its an instance or inherited
        a_class (type): the class to connect the type
    Returns:
        if obj is an instance or inherited instance of a_class - True
        otherwise - False
    """
    return isinstance(obj, a_class)
