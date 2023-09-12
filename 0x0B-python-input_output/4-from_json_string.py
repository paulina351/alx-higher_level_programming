#!/usr/bin/python3
"""A function that returns an object by json string."""
import json


def from_json_string(my_str):
    """A function that returns an objects (Python data structure)
    represented by a JSON string
    """
    return json.loads(my_str)
