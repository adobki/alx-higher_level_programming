#!/usr/bin/python3
"""This is a Rectangle class module with some extra code for testing."""


class Rectangle:
    """An empty class that defines a Rectangle."""
    pass


def main():
    """Tests the code."""

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)


if __name__ == "__main__":
    main()
