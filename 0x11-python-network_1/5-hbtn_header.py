#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
import requests


def url_fetch():
    """Prints X-Request-Id from header of the response from given url."""

    if len(sys.argv) < 2:
        return

    with requests.get(sys.argv[1]) as html:
        try:
            return html.headers['X-Request-Id']
        except KeyError:
            return None


if __name__ == '__main__':
    my_str = url_fetch()
    if my_str:
        print(my_str)
