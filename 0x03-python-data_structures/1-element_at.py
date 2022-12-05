#!/usr/bin/python3
def element_at(my_list, idx):
    """Securely retrieves an element from list using index like in C.

    :param my_list: List to be printed.
    :param idx: Element's index.

    :return: Value at given index in given list.
    """
    return my_list[idx] if 0 <= idx <= len(my_list) - 1 else None
