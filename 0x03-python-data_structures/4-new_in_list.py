#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Copies list, securely replaces element at given index like in C.

    :param my_list: List with element to be replaced.
    :param idx: Element's index.
    :param element: New data to be stored at given index.

    :return: New list [with modified data if index is valid].
    """
    new_list = my_list[:]
    if 0 <= idx <= len(my_list) - 1:
        new_list[idx] = element
    return new_list
