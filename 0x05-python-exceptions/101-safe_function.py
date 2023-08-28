#!/usr/bin/python3
def safe_function(fct, *args):
    """
    function that executes a function safely.
    """

    try:
        a = fct(*args)
        return a
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
