#!/usr/bin/python3
"""a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """it returns the available attributes and methods an object has"""
    return (dir(obj))
