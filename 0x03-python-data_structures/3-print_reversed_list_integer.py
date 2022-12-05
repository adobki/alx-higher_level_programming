#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers in a given list in reverse.

    :param my_list: List of integers to be printed in reverse.

    :return: None
    """
    if my_list is not None:
        for num in reversed(my_list):
            print('{:d}'.format(num))
