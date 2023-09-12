#!/usr/bin/python3
"""A function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """A function that appends a string at the end of the file

    Args:
        filename (str): the file name to append to
        text (str): the string to append to
    Returns:
        The number of characters
    """
    with open(filename, mode="a", encoding="utf=8") as f:
        return f.write(text)
