#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element in a list.

    :param my_list: Given list.
    :param search: Element to search for/replace in list.
    :param replace: Element to replace search with.

    :return: Copy of my_list with search element replaced.
    """
    if my_list is not None:
        return list(map((lambda num: replace if num is search else num),
                        my_list))
