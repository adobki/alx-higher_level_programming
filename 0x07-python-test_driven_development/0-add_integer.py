#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def add_integer(a, b=98):
    """Adds two integers and returns the result."""

    try:
        if type(a) not in (int, float):
            raise TypeError('a must be an integer')
        elif type(b) not in (int, float):
            raise TypeError('b must be an integer')
        else:
            a, b = int(a), int(b)
            return int(a + b)
    except Exception as err:
        return err


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests\\0-add_integer.txt', verbose=True)
