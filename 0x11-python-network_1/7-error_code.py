#!/usr/bin/python3
"""a Python script that takes in a URL."""
import requests
from sys import argv


def intranet_hbtn_error_1():
    """a Python script that takes in a URL, sends a
       request to the URL and displays the body of the response.
    """
    body = requests.get(argv[1])
    if body.status_code >= 400:
        print("Error code: {}".format(body.status_code))
    else:
        print(body.text)


if __name__ == "__main__":
    intranet_hbtn_error_1()
