#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the biggest integer value.

    :param a_dictionary: Dictionary to be checked.

    :return: Key with highest integer value in given dictionary.
    """
    if a_dictionary is not None and len(a_dictionary) >= 1:
        biggest = sorted(a_dictionary.values())[-1]
        return [key for key, val in a_dictionary.items() if val is biggest][0]
