#!/usr/bin/python3
def raise_exception():
    """Raises a type exception."""
    raise TypeError


def main():
    """Tests the code."""
    try:
        raise_exception()
    except TypeError as te:
        print('Exception raised')


if __name__ == '__main__':
    main()
