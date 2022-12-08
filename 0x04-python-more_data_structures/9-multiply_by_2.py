#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2

    :param a_dictionary: Dictionary to be updated.

    :return: Copy of given dictionary with values doubled.
    """
    if a_dictionary is not None:
        return dict((key, a_dictionary[key] * 2) for key in
                    a_dictionary.keys())
