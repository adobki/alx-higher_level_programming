#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary.

    :param a_dictionary: Dictionary to be updated.
    :param key: Key to delete from dictionary.

    :return: Copy of given dictionary with key/value pair deleted.
    """
    if a_dictionary is not None:
        if key in a_dictionary.keys():
            a_dictionary.pop(key)
    return a_dictionary
