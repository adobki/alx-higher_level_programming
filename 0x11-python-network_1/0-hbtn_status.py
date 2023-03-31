#!/usr/bin/python3
"""Module is an introduction to networking with urllib in Python."""
import urllib.request as request


def url_fetch():
    """Fetches a url and prints the response."""
    with request.urlopen('https://alx-intranet.hbtn.io/status') as html:
        html = html.read()
        response = 'Body response:''\n\t' \
                   '- type: {}'    '\n\t' \
                   '- content: {}' '\n\t' \
                   '- utf8 content: {}'
        response = response.format(type(html), html, html.decode('utf-8'))
    return response


if __name__ == '__main__':
    print(url_fetch())
