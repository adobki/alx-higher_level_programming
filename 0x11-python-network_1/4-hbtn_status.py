#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import requests


def url_fetch():
    """Fetches a url and prints the response."""
    with requests.get('https://alx-intranet.hbtn.io/status') as html:
        html = html.text
        response = 'Body response:''\n\t' \
                   '- type: {}'    '\n\t' \
                   '- content: {}'.format(type(html), html)
    return response


if __name__ == '__main__':
    print(url_fetch())
