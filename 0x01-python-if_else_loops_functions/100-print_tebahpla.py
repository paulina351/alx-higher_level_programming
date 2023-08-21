#!/usr/bin/python3
rever = 0
for r in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(r - rever)), end="")
    rever = 32 if rever == 0 else 0
