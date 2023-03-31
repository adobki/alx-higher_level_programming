#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
import requests


def url_fetch():
    """Displays id for given GitHub credentials using the GitHub API."""

    if len(sys.argv) < 2:
        return

    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    with requests.get(url) as html:
        try:
            return html.json()['id']
        except KeyError:
            return


if __name__ == '__main__':
    print(url_fetch())
