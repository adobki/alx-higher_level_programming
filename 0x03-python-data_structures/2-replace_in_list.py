#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Securely replaces list element at given index like in C.

    :param my_list: List with element to be replaced.
    :param idx: Element's index.
    :param element: New data to be stored at given index.

    :return: Given list [with modified data if index is valid].
    """
    if 0 <= idx <= len(my_list) - 1:
        my_list[idx] = element
    return my_list
