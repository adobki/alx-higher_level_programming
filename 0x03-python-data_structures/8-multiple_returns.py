#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns tuple with length of string and its first character.

    :param sentence: Given string.

    :return: Tuple with length and first character of given string.
    """
    return len(sentence), sentence[0] if len(sentence) >= 1 else None
