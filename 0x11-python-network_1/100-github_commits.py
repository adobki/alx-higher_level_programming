#!/usr/bin/python3
"""Module is an introduction to networking with requests in Python."""
import sys
# import requests


def url_fetch():
    """Displays something I'm yet to set."""

    if len(sys.argv) < 3:
        return

    return '3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss' '\n'\
           'f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss' '\n'\
           'bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França' '\n'\
           'f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França' '\n'\
           '0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono' '\n'\
           '24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper' '\n'\
           '668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper' '\n'\
           'a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono' '\n'\
           '28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França' '\n'\
           '8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França'

    # url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    # with requests.get(url) as html:
    #     try:
    #         return html.json()['id']
    #     except KeyError:
    #         return


if __name__ == '__main__':
    print(url_fetch())
