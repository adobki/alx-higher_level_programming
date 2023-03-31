#!/usr/bin/python3
"""Module is an introduction to networking with urllib in Python."""
import sys
import urllib.request as request


def url_fetch():
    """Prints X-Request-Id from header of the response from given url."""

    if len(sys.argv) < 2:
        return

    with request.urlopen(sys.argv[1]) as html:
        return html.headers['X-Request-Id']


if __name__ == '__main__':
    my_str = url_fetch()
    if my_str:
        print(my_str)
