#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    :param my_list: Given list.

    :return: Biggest number in list => max(my_list).
    """
    if len(my_list) <= 0:
        return None
    max_int = my_list[0]
    for num in my_list:
        max_int = num if num > max_int else max_int
    return max_int
