#!/usr/bin/python3
"""a Python script that takes in a URL."""

from urllib.request import urlopen
from urllib.request import  Request
from sys import argv
import urllib.error


def intranet_hbtn_error():
    """sends a request to the URL and displays
        the body of the response (decoded in utf-8).
    """
    url = arg[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as error:
            print("Error code: {}".format(error.code))


if __name__ == "__main__":
    intranet_hbtn_error():
