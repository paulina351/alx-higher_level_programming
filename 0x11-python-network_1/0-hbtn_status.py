#!/usr/bin/python3
"""A python script that fetches using urllib."""


from urllib.request import urlopen


def intranet_htbn_status():
    """Function that uses the package urllib."""
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        utf8 = html.decode("utf-8")
        print("Body response:\n\t- type: {}".format(type(html)))
        print("\t- content: {}\n\t- utf8 content: {}".
                format(html, utf8, end=""))


if __name__ == "__main__":
    intranet_hbtn_status()
