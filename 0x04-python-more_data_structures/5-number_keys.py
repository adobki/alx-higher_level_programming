#!/usr/bin/python3
def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary.

    :param a_dictionary: A dictionary.

    :return: Number of keys stored in given dictionary.
    """
    if a_dictionary is not None:
        return len(a_dictionary.keys())
    # else:
    #     return 0
