#!/usr/bin/python3
def check_tuple(my_tuple, size=2):
    """Checks len(tuple)==2, fills zero in empty space(s) if not.

    :param my_tuple: Tuple to be checked.
    :param size: Desired size for given tuple.

    :return: Given tuple with zeroes filled in empty spaces, if any.
    """
    if len(my_tuple) != size:
        if len(my_tuple) == 0:
            my_tuple = (0, 0)
        elif len(my_tuple) == 1:
            my_tuple = (my_tuple[0], 0)

    return my_tuple


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds the first two elements of two tuples.

    :param tuple_a: First tuple to be added.
    :param tuple_b: Second tuple to be added.

    :return: Tuple with two integers (sum(a[0], b[0]), sum(a[1], b[1])).
    """
    tuple_a, tuple_b = check_tuple(tuple_a), check_tuple(tuple_b)

    a, b = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]

    return a, b
