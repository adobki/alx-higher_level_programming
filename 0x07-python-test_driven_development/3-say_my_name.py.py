#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def say_my_name(first_name, last_name=''):
    """Prints 'My name is <first name> <last name>'."""

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        # if last_name != '':
        #     last_name = ' {}'.format(last_name)
        print('My name is {} {}'.format(first_name, last_name))


def main():
    """Tests the code."""

    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
