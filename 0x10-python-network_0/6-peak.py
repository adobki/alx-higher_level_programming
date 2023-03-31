#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(my_list=[]):
    """Function finds a peak in a list of unsorted integers."""
    if type(my_list) != list or my_list == []:
        return

    result = my_list[-1]
    for num in range(len(my_list)-1):
        result = my_list[num] if my_list[num] > result else result

    return result


if __name__ == '__main__':
    print(find_peak([2, 5, 2, 1]))
    print(find_peak('wood'))
    print(find_peak())
