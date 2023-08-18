#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print a dictionary by ordered list
    ...
    params
    ------
    a_dictionary : dictionary
        the given dictionary

    Return:
        nothing
    """

    [print("{}: {}".format(a, a_dictionary[a])) for a in sorted(a_dictionary)]
