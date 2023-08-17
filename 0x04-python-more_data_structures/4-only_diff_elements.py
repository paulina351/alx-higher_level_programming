#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in one set
    ...
    parameters
    ---------
    set_1: set
        first element
    set_2 : set
        second element

    Return:
        the result of the operation (&)
    """
    return (set_1 ^ set_2)
