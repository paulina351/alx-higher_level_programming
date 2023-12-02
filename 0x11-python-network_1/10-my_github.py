#!/usr/bin/python3
"""a Python script."""
import sys
import requests


def intranet_github():
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(
            "https://api.github.com/user", auth=(username, password))
    token = res.json()
    print(token.get("id"))


if __name__ == "__main__":
    intranet_github()
