#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
import requests


def url_fetch():
    """Prints response from given url or the response code on error."""

    if len(sys.argv) < 2:
        return

    with requests.get(sys.argv[1]) as html:
        if html.status_code == 200:
            return html.text
        else:
            return 'Error code: {}'.format(html.status_code)


if __name__ == '__main__':
    print(url_fetch())
