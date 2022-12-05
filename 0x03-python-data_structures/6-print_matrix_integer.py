#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers.

    :param matrix: Given matrix to be printed.

    :return: None.
    """
    rows, cols = len(matrix), len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            print('{:d}'.format(matrix[row][col]), end='')
            if col < cols - 1:
                print(' ', end='')
        print()
