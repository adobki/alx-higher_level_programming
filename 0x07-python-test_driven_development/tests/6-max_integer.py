#!/usr/bin/python3
"""Module to find the max integer in a my_list."""


def max_integer(my_list=None):
    """Function to find and return the max integer in a list of integers.
    If the list is empty, the function returns None."""

    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        return None
    result = my_list[0]
    i = 1
    while i < len(my_list):
        if my_list[i] > result:
            result = my_list[i]
        i += 1
    return result
