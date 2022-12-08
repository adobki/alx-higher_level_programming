#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral [between 1 and 3999] to an integer.

    :param roman_string: Number in roman numeral.

    :return: Integer value of given roman numeral.
    """
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    previous = integer = 0

    for num in list(roman_string):
        if num in numerals.keys():
            if previous == 'I' and num != 'I':
                integer += numerals[num] - 2
            elif previous == 'X' and num in ('L', 'C'):
                integer += numerals[num] - 20
            elif previous == 'C' and num in ('D', 'M'):
                integer += numerals[num] - 200
            else:
                integer += numerals[num]
            previous = num
        else:
            return 0
    return integer
