#!/usr/bin/python3
def print_tebahpla():
    """Prints the alphabets backwards in toggled case.\
    """

    alphabets = list(range(97, 123))
    alphabets.reverse()
    for letter in alphabets:
        if letter % 2:
            letter -= 32
        print("{}".format(chr(letter)), end="")


print_tebahpla()
