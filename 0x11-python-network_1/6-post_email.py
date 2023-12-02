#!/usr/bin/python3
"""a Python script that takes in a URL."""
import requests
from sys import argv


def intranet_hbtn_email_1():
    """a Python script that takes in a URL and an
       email address, sends a POST request to the passed
       URL with the email as a parameter, and finally
       displays the body of the response.
    """
    post_email = {'email': argv[2]}
    response = requests.post(argv[1], data=post_email)
    print(response.text)


if __name__ == "__main__":
    intranet_hbtn_email_1()
