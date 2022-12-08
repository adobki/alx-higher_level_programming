#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set.

    :param set_1: First list/set.
    :param set_2: Second list/set.

    :return: List of elements that exist in only one set, but not the other.
    """
    if set_1 and set_2 is not None:
        # return list(set_1.difference(set_2)) + list(set_2.difference(set_1))
        return set_1.symmetric_difference(set_2)
    elif set_1 is not None:
        return set_2
    else:
        return set_1
