#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    a function that returns a new dictionary with all values multiplied by 2
    """
    return ({a: a_dictionary[a] * 2 for a in a_dictionary})
