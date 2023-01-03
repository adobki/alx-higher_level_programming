#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""

    err1 = 'matrix must be a matrix (list of lists) of integers/floats'
    err2 = 'Each row of the matrix must have the same size'
    err3 = 'div must be a number'
    err4 = 'division by zero'
    if not isinstance(matrix, list):
        raise TypeError(err1)
    # if not isinstance(num, int) and not isinstance(num, float):
    #     raise TypeError(err2)
    # else:
    #     a, b = int(a), int(b)
    #     return int(a + b)
    return matrix


def main():
    """Tests the code."""

    pass


if __name__ == "__main__":
    main()
