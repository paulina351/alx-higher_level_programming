#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all character c and C

    """
    return ("".join([c for c in my_string if c not in ['c', 'C']]))
