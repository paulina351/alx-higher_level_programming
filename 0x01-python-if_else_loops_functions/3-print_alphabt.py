#!/usr/bin/python3
for characters in range(97, 123):
    if chr(characters) != 'q' and chr(characters) != 'e':
        print("{}".format(chr(characters)), end="")
