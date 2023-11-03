#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for values in my_list:
        if isinstance(values, int):
            print("{:d}".format(values))
