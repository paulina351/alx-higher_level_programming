#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    addition = 0
    for a in range(len(sys.argv) - 1):
        addition += int(sys.argv[a + 1])
    print("{}".format(addition))
