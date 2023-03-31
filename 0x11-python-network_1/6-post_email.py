#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
import requests


def url_fetch():
    """Prints response from POST request with parameters to a given url."""

    if len(sys.argv) < 3:
        return

    url = sys.argv[1]
    header = {'email': sys.argv[2]}
    with requests.post(url, header) as html:
        return html.text


if __name__ == '__main__':
    print(url_fetch())
