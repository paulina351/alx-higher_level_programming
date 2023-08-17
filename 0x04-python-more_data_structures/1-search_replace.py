#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    function that replacesan elements
    ...

    parameters
    ---------
    my_list : list
        initial lists of elements
    search : integer
        the element to replace
    replace : integer
        the new element

    Return:
    a new list with the new elements


    """

    new_list = my_list[:]
    for j in range(len(new_list)):
        if new_list[j] == search:
            new_list[j] = replace
    return (new_list)
