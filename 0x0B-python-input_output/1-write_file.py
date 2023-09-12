#!/0usr/bin/python3
"""A function that writes to a file"""


def write_file(filename="", text=""):
    """Function that writes a UTF=8 file

    Args:
        filename (str): the file name to write
        text (str): the text to write
    Returns:
        the characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        len = f.write(text)

    return len
