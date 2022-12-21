#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square:
    """An empty class that defines a square."""
    pass


def main():
    """Tests the code."""

    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)
    print(my_square.__doc__)


if __name__ == "__main__":
    main()
