#!/usr/bin/python3
# 2-is_same_class.py


def is_same_class(obj, a_class):
    """returns True if object is intance and false if not


    Args:
        obj: The object to check
        a_class: The class to CHECK IF same with obj
    """

    return isinstance(obj, a_class)
