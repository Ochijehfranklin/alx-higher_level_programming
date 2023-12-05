#!/usr/bin/python3
# 1-write_file.py
"""project to write string to a file"""


def write_file(filename="", text=""):
    """writes string to a file


    Args:
        filename (str): The name of the file to write
        text (str): The text to write to the file
    Return:
            the number of charsacters
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
