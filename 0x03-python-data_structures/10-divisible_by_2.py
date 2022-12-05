#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    :param my_list: Given list.

    :return: Truth table with values for if element divisible by 2.
    """
    return [x % 2 == 0 for x in my_list]
