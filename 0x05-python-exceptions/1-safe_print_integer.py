#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    :param value: Integer value to be printed.

    :return: True on success (value is an integer)
             False on error (value not an integer)
    """
    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True


def main():
    """Tests the code."""

    my_list = [1, '2', 3, '4', 5]
    [safe_print_integer(val) for val in my_list]
    print()

    # Example from project: #
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))


if __name__ == "__main__":
    main()
