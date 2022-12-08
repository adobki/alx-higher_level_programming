#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers of a matrix.

    :param matrix: A two-dimensional array.

    :return: New array with the square of each value in matrix.
    """
    if matrix is not None:
        return [(list(map((lambda num: num * num), x))) for x in matrix]
