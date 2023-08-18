#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Write a function that returns the weighted average of all
    integers tuple (<score>, <weight>)

    """
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    averg = 0
    size = 0
    for tup in my_list:
        averg += (tup[0] * tup[1])
        size += tup[1]
    return (averg / size)
