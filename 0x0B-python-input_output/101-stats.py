#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning
"""


def print_status(size, status_code):
    """print the computed metries.

    Args:
        size (int): the read file
        status_code (dict): the status code
    """
    print("File size: {}".format(size))
    for ky in sorted(status_code):
        print("{}: {}".format(ky, status_code[ky]))


if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    true_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_status(size, status_code)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in true_code:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] - 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_status(size, status_code)
    except KeyboardInterrupt:
        print_status(size, status_code)
        raise
