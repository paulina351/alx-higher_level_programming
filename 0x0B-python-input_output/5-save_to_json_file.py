#!/usr/bin/python3
"""A function writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """A JSON Representation"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
