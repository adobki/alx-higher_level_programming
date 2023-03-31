#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
import requests


def url_fetch():
    """Sends POST to a website with given letter as a passed parameter."""

    letter = sys.argv[1] if len(sys.argv) == 2 else ''
    header = {'q': letter}
    with requests.post('http://0.0.0.0:5000/search_user', header) as html:
        try:
            if len(sys.argv) < 2 or "id" not in html.json().keys() or\
                    "name" not in html.json().keys():
                return 'No result'
            else:
                return '[{}] {}'.format(html.json()['id'],
                                        html.json()['name'])
        except Exception:
            return 'Not a valid JSON'


if __name__ == '__main__':
    print(url_fetch())
