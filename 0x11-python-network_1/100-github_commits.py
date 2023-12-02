#!/usr/bin/python3
"""Holberton School staff."""
from sys import argv
import requests


def intranet_github_commit():
    rep = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(argv[2], argv[1]))
    commits = rep.json()
    for commit in commits[:10]:
        print(commit.get("sha"), end=": ")
        print(commit.get("commit").get("author").get("name"))


if __name__ == "__main__":
    intranet_github_commit()
