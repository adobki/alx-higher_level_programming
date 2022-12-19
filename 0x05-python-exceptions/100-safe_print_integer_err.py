#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer.

    :param value: Integer to be printed.

    :return: True on success (value was printed).
             False on error (value wasn't printed).
    """
    try:
        print('{:d}'.format(value))
        return True
    except Exception as err:
        sys.stderr.write('Exception: {}\n'.format(err))
        return False


def main():
    """Tests the code."""

    # value = [89]
    # print(safe_print_integer_err(value))

    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))


if __name__ == "__main__":
    main()
