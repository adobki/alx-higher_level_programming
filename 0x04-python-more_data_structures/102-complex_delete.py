#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value in a dictionary.

    :param a_dictionary: Dictionary to be edited.
    :param value: Value (and its key) to be deleted from dictionary.

    :return: Given dictionary [with all instances of value deleted].
    """

    if a_dictionary is not None:
        del_keys = []
        for key in a_dictionary.keys():
            if a_dictionary[key] is value:
                del_keys.append(key)

        for key in del_keys:
            del a_dictionary[key]

    return a_dictionary
