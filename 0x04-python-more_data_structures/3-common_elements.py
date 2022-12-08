#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a set of common elements in two sets.

    :param set_1: First list/set.
    :param set_2: Second list/set.

    :return: List of elements that exist in both sets.
    """
    if set_1 and set_2 is not None:
        return set_1.intersection(set_2)
    return {}
