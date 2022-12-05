#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints all integers in a given list.

    :param my_list: List to be printed.

    :return: None
    """
    for num in my_list:
        print('{:d}'.format(num))
