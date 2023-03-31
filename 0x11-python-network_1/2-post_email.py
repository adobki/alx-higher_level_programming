#!/usr/bin/python3
"""Module is an introduction to networking with urllib in Python."""
import sys
import urllib.request as request


def url_fetch():
    """Prints response from POST request with parameters to a given url."""

    if len(sys.argv) < 3:
        return

    url = sys.argv[1]
    header = {'email': sys.argv[2]}
    my_request = request.Request(url, header)
    with request.urlopen(my_request) as html:
        return html.read().decode('utf-8')


if __name__ == '__main__':
    my_str = url_fetch()
    if my_str:
        print(my_str)
