#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys.

    :param a_dictionary: Dictionary to be printed.

    :return: None.
    """
    if a_dictionary is not None:
        # for key in sorted(a_dictionary.keys()):
        #     print('{}: {}'.format(key, a_dictionary[key]))
        [print('{}: {}'.format(key, a_dictionary[key]))for key in
         sorted(a_dictionary.keys())]
