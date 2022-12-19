#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Prints an integer.

    :param fct: Pointer to a function.
    :param args: Arguments to be passed to fct.

    :return: Result of fct on success.
             None on error.
    """
    try:
        # errors = [ValueError(1), IndexError(2), SystemError(3), OSError(4)]
        return fct(*args)
    except Exception as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        return None


def main():
    """Tests the code."""

    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))

    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))

    def print_list(my_list, len):
        i = 0
        while i < len:
            print(my_list[i])
            i += 1
        return len

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))


if __name__ == "__main__":
    main()
