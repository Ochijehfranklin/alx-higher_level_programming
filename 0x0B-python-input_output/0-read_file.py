#!/usr/bin/python3
# 0-read_file.py
"""Project that reads a text file"""


def read_file(filename=""):
    """function to read text file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
