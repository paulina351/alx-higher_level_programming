#!/bin/bash
# a Bash script that makes a request
curl -sX PUT -L -d "user_id=89" --header "origin: You got me!" 0.0.0.0:5000/catch_me
