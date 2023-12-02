#!/usr/bin/python3
"""a Python script that takes in a URL."""

from urllib.request import urlopen
from sys import argv


def intranet_hbtn_header():
    """sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response.
    """
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    intranet_hbtn_header()
