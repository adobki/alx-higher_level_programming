#!/usr/bin/python3
def raise_exception_msg(message=""):
    """Raises a NameError exception with a custom message.

    :param message: Message to be displayed in exception.
    """
    raise NameError(message)


def main():
    """Tests the code."""
    # raise_exception_msg('C is fun')
    try:
        raise_exception_msg('C is fun')
    except NameError as ne:
        print('{}'.format(ne))


if __name__ == '__main__':
    main()
