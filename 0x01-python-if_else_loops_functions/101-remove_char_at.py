#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Copies a string and removes the character at a given position.
    Given position, n, corresponds to C type index, not Python type.\
    """

    if n >= 0:
        new_str = str[:n] + str[n+1:]
    else:
        new_str = str
    print(new_str, end="")

    return ""
