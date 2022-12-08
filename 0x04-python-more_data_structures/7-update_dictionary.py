#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    :param a_dictionary: Dictionary to be updated.
    :param key: Key to find in/add to dictionary.
    :param value: Value to be assigned to the given key.

    :return: Copy of given dictionary with new key/value pair.
    """
    if a_dictionary is not None:
        a_dictionary[key] = value
        return a_dictionary
