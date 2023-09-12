#!/usr/bin/python3
"""function that reads a text file and returns it to standard output"""


def read_file(filename=""):
    """A function that read a text file (UTF8)"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
