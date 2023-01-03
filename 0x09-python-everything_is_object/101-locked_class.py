#!/usr/bin/python3
"""This Defines a Class named LockedClass."""


class LockedClass:
    """Class with no attributes that prevents dynamic creation\
    of attributes, except if new attribute is 'first_name'."""

    __slots__ = ['first_name']

    # def __setattr__(self, attribute, data):
    #     """Sets LockedClass instance attributes dynamically."""
    #     err = "'LockedClass' object has no attribute '{}'".format(attribute)
    #     if attribute != 'first_name':
    #         raise AttributeError(err)
    #     object.__setattr__(self, attribute, data)


def main():
    """Tests the code."""

    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))


if __name__ == "__main__":
    main()
