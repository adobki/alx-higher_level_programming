#!/usr/bin/python3
"""Module is an introduction to networking with urllib in Python."""
import sys
from urllib import request
from urllib.error import HTTPError


def url_fetch():
    """Prints response from given url or the response code on error."""

    if len(sys.argv) < 2:
        return

    try:
        with request.urlopen(sys.argv[1]) as html:
            return html.read().decode('utf-8')
    except HTTPError as err:
        print('Error code: {}'.format(err.code))


if __name__ == '__main__':
    my_str = url_fetch()
    if my_str:
        print(my_str)
