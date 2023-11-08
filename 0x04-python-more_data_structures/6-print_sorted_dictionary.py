#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dic = sorted(a_dictionary)
    for x in new_dic:
        print("{}: {}".format(x, a_dictionary[x]))
