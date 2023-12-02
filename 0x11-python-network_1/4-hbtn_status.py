#!/usr/bin/python3
"""a Python script that fetches."""

import requests


def intranet_hbtn_status_1():
    """a Python script that fetches using request."""
    status_req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(status_req.text), status_req.text))


if __name__ == "__main__":
    intranet_hbtn_status_1()
