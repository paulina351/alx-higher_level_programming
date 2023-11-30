#!/bin/bash
# a Bash script that takes in a URL, sends a request to that Url
curl -s "$1" | wc -c
