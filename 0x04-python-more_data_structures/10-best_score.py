#!/usr/bin/python3
def best_score(a_dictionary):
    """

    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    reutn = list(a_dictionary.keys())[0]
    biggest = a_dictionary[reutn]
    for a, b in a_dictionary.items():
        if b > biggest:
            biggest = b
            reutn = a
    return (reutn)
