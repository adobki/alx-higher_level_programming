#!/usr/bin/python3
"""This is a Square class module with some extra code for testing."""


class Square():
    """A Square with a size attribute/field."""

    def __init__(self, size=None):
        """
        Initialises a new instance of Square and sets its size.

        :param size: Size of the Square.
        """
        self.__size = size


def main():
    """Tests the code."""

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
    print(my_square.__init__.__doc__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
