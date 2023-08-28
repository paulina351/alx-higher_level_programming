#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    function that prints an integer
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
