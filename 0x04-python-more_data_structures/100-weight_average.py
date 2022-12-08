#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple (<score>, <weight>).
        ((a1 * a2) + (b1 * b2) + (c1 * c2) + . . .) / (a2 + b2 + c2 + . . .)

    :param my_list: List to enumerate.

    :return: Weighted average of integers in given list of tuples.
    """
    if my_list is None or len(my_list) == 0:
        return 0

    numerator = denominator = 0
    for tup in my_list:
        numerator += tup[0] * tup[1]
        denominator += tup[1]

    return numerator/denominator
