#!/usr/bin/python3
"""Function that defines a text"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file,
    after each line containing a specific string

    Args:
        params: filename (str):
        params: search_string (str):
        params: new_string (str):
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
