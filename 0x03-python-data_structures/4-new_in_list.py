#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a copy of a list at
    specific position
    ...

    parameters
    __________
    my_list : list
      the lists of elements
    idx: integer
        the given position
    element: the new element

    Return:
        the copy of the list if idx is negative or
        if idx out of range (> len(my_list))

    """

    list_copy = my_list.copy()
    if idx >= 0 and idx <= (len(my_list) - 1):
        list_copy[idx] = element
    return list_copy
