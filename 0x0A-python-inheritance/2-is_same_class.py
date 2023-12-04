#!/usr/bin/python3
# 2-is_same_class.py


def is_same_class(obj, a_class):
    """returns True if object is intance and false if not


    Args:
        obj (any): The object to check
        a_class (type): The class to CHECK IF same with obj
    """

    if isinstance(obj, a_class):
        return True
    return False
