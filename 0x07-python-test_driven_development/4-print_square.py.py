#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def print_square(size):
    """Prints a square with the character #."""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for num in range(size):
            for num2 in range(size):
                print('#', end='')
            print()


def main():
    """Tests the code."""

    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")


if __name__ == "__main__":
    main()
