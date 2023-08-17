#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds all unique integers in a list

    parameters
    ---------
    my_list : list
        list of elements

    Return: the result of the addition

    """

    result = 0
    for i in set(my_list):
        result += i
    return (result)
