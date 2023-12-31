#!/usr/bin/python3
"""a Python script that takes in a URL."""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


def intranet_hbtn_email():
    """sends a POST request to the passed URL with the
       email as a parameter, and displays the body of the
       response (decoded in utf-8).
    """
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    intranet_hbtn_email()
