#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    function that computes the square value of all integers of a matrix
    ...

    Parameters
    ----------
    matrix : list (of lists)
        the list of elements

    Return:
        a new matrix:
            same size as matrix
            each balue should be the square of the value of the input
    """

    return ([list(map(lambda x: x * x, row)) for row in matrix])
