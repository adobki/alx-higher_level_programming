#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    :param my_list: List with element to be replaced.
    :param idx: Element's index.

    :return: Given list [without element if index is valid].
    """
    if 0 <= idx <= len(my_list) - 1:
        my_list.__delitem__(idx)
    return my_list
