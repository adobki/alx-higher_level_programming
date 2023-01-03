#!/usr/bin/python3
"""This is a program that solves the N queens problem."""


def n_queens(n=None):
    """
    Solves the N queens chess puzzle.

    :param n: Integer value of N for given puzzle.

    :return: A 2D array which is the solution to the N queens puzzle.
    """
    if n is None:
        print('Usage: nqueens N')
    elif not isinstance(n, int):
        print('N must be a number')
    elif n < 4:
        print('N must be at least 4')
    else:
        print('[', end='')
        for num in range(n):
            print('[{},{}]'.format(num, num + 1), end='')
            if num != n - 1:
                print(', ', end='')
        print(']')


def main():
    """Tests the code."""
    n_queens(6)


main()
