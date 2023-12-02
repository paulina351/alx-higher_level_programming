#!/usr/bin/python3
"""a Python script that takes in a letter."""
from sys import argv
import requests


def intranet_hbtn_jsonapi():
    try:
        q = argv[1]
    except:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}
    ap = requests.post(url, payload)
    try:
        json = ap.json()
        if len(json) == 0:
            print("No result")
        else:
            json_id = json.get("id")
            json_name = json.get("name")
            print("[{}] {}".format(json_id, json_name))
        except:
            print("Not a valid JSON")


if __name__ == "__main__":
    intranet_hbtn_jsonapi()
