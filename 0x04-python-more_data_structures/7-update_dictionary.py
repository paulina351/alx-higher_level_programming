#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary
    ...
    params
    ------
    a_dictionary : dictionary
        the given dictionary
    key : value
        argument is string
    value : any type
        argument will be any type

    Return:
        the dictionary with the new inserted value


    """
    a_dictionary[key] = value
    return (a_dictionary)
