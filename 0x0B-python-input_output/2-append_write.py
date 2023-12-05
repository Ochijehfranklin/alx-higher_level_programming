#!/usr/bin/python3
# -append_write.py
"""project for appending file"""


def append_write(filename="", text=""):
    """append a string to the end of text file

    Args:
        filename (str): The name of the file to append to
        text (str): The string to append to file
    Return:
           The number of characters appended.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
