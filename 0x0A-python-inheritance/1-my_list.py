#!/usr.bin/python3
# 1-my_list.py
"""Write a class MyList that inherits from list:"""


class MyList(list):
    """prints elements of a list"""


    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
