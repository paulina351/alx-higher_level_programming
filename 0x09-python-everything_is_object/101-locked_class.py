#!/usr/bin/python3
"""a locked class with no class or attribute"""


class LockedClass:
    """no class or attribute from the user"""
    __slot__ = ["first_name"]
