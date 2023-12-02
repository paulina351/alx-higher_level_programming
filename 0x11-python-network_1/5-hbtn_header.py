#!/usr/bin/python3
"""a Python script that takes in a URL."""
import requests
from sys import argv


def intranet_hbtn_header_1():
    """a Python script that takes in a URL, sends a
       request to the URL and displays the value of the
       variable X-Request-Id in the response header.
    """
    reqts = requests.get(argv[1])
    print(reqts.headers.get('X-Request-Id'))


if __name__ == "__main__":
    intranet_hbtn_header_1()
